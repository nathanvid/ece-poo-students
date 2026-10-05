import importlib
import sys

import pytest
from fastapi.testclient import TestClient

from checks import load_module


@pytest.fixture
def modules(exercise_copy, monkeypatch):
    """(shows, api), imported from a copy of the folder.

    api.py does `from shows import ...`: the folder must be in sys.path.
    """
    folder = exercise_copy("03_festival_api")
    monkeypatch.syspath_prepend(str(folder))
    monkeypatch.delitem(sys.modules, "shows", raising=False)
    shows = importlib.import_module("shows")
    api = load_module(folder / "api.py")
    return shows, api, folder


@pytest.fixture
def client(modules):
    shows, api, folder = modules
    return TestClient(api.create_app(shows.load_programme(folder / "programme.json")))


LATE = "le-kiosque-2027-06-11-2330"

NEW_SHOW = {
    "title": "Morning Glory",
    "artist": "Sacha Diallo",
    "venue": "Le Kiosque",
    "start": "2027-06-12T11:00",
    "duration": 45,
    "price": 8,
}


# --- Views and status codes --------------------------------------------------------


def test_http_status(modules):
    shows, api, _ = modules
    assert api.http_status(shows.NotFoundError("x")) == 404
    assert api.http_status(shows.ConflictError("x")) == 409
    assert api.http_status(shows.InvalidDataError("x")) == 422
    assert api.http_status(shows.FestivalError("x")) == 400


def test_show_view(modules):
    shows, api, folder = modules
    programme = shows.load_programme(folder / "programme.json")
    assert api.show_view(programme.get(LATE)) == {
        "title": "Late Laughs",
        "artist": "Nora Lebrun",
        "venue": "Le Kiosque",
        "start": "2027-06-11T23:30",
        "duration": 60,
        "price": 12.0,
        "id": LATE,
        "end": "2027-06-12T00:30",
        "festival_day": "2027-06-11",
    }


# --- Read --------------------------------------------------------------------------


def test_list_shows(client):
    response = client.get("/api/shows")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 8
    assert data[0]["title"] == "Opening Night"
    assert "id" in data[0]


def test_shows_of_a_day_include_the_night(client):
    data = client.get("/api/shows", params={"day": "2027-06-11"}).json()
    titles = []
    for show in data:
        titles.append(show["title"])
    assert titles == [
        "Improv Lab",
        "Normal, Almost",
        "Lost But Charmed",
        "Late Laughs",
        "After Hours",
    ]
    assert client.get("/api/shows", params={"day": "June 11"}).status_code == 422


def test_read_show(client):
    response = client.get(f"/api/shows/{LATE}")
    assert response.status_code == 200
    assert response.json()["title"] == "Late Laughs"


def test_unknown_show_is_404(client):
    response = client.get("/api/shows/nothing")
    assert response.status_code == 404
    assert response.json() == {"detail": "Unknown show: nothing."}


# --- Write -------------------------------------------------------------------------


def test_create_show(client):
    response = client.post("/api/shows", json=NEW_SHOW)
    assert response.status_code == 201
    assert response.json()["id"] == "le-kiosque-2027-06-12-1100"
    assert client.get("/api/shows/le-kiosque-2027-06-12-1100").status_code == 200
    assert len(client.get("/api/shows").json()) == 9


def test_clash_is_409(client):
    clash = dict(NEW_SHOW)
    clash["start"] = "2027-06-12T01:30"
    response = client.post("/api/shows", json=clash)
    assert response.status_code == 409
    assert response.json() == {
        "detail": "Le Kiosque is busy with After Hours (Sat 01:00-02:00)."
    }
    assert len(client.get("/api/shows").json()) == 8


def test_invalid_show_is_422(client):
    too_long = dict(NEW_SHOW)
    too_long["duration"] = 400
    response = client.post("/api/shows", json=too_long)
    assert response.status_code == 422
    assert response.json() == {"detail": "Invalid duration: 400 (1 to 360 minutes)."}
    missing = dict(NEW_SHOW)
    del missing["title"]
    assert client.post("/api/shows", json=missing).status_code == 422


def test_delete_show(client):
    assert client.delete(f"/api/shows/{LATE}").status_code == 204
    assert client.get(f"/api/shows/{LATE}").status_code == 404
    assert client.delete(f"/api/shows/{LATE}").status_code == 404


# --- [ext.] ------------------------------------------------------------------------


def test_replace_show(client):
    moved = {
        "title": "Late Laughs",
        "artist": "Nora Lebrun",
        "venue": "Le Kiosque",
        "start": "2027-06-12T23:30",
        "duration": 60,
        "price": 12,
    }
    response = client.put(f"/api/shows/{LATE}", json=moved)
    assert response.status_code == 200
    assert response.json()["id"] == "le-kiosque-2027-06-12-2330"
    assert client.get(f"/api/shows/{LATE}").status_code == 404


def test_replace_with_a_clash_changes_nothing(client):
    clash = dict(NEW_SHOW)
    clash["start"] = "2027-06-12T01:30"
    response = client.put(f"/api/shows/{LATE}", json=clash)
    assert response.status_code == 409
    assert client.get(f"/api/shows/{LATE}").status_code == 200
    assert len(client.get("/api/shows").json()) == 8
    assert client.put("/api/shows/nothing", json=NEW_SHOW).status_code == 404


def test_now(client):
    data = client.get("/api/now", params={"at": "2027-06-11T21:15"}).json()
    assert data["at"] == "2027-06-11T21:15"
    titles = []
    for show in data["now_playing"]:
        titles.append(show["title"])
    assert titles == ["Normal, Almost", "Lost But Charmed"]
