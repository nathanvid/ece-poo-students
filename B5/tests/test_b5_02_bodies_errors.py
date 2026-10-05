import pytest
from fastapi.testclient import TestClient


@pytest.fixture
def client(load_exercise):
    """A new application for each test: the venues start empty."""
    return TestClient(load_exercise("02_bodies_errors/venues_api.py").create_app())


KIOSQUE = {"name": "Le Kiosque", "capacity": 120, "address": "Beach promenade"}


def test_starts_empty(client):
    response = client.get("/venues")
    assert response.status_code == 200
    assert response.json() == []


def test_create_venue(client):
    response = client.post("/venues", json=KIOSQUE)
    assert response.status_code == 201
    assert response.json() == {
        "slug": "le-kiosque",
        "name": "Le Kiosque",
        "capacity": 120,
        "address": "Beach promenade",
        "seats_left": 120,
    }
    assert client.get("/venues/le-kiosque").json()["name"] == "Le Kiosque"


def test_venues_keep_their_order(client):
    client.post("/venues", json={"name": "Théâtre des Planches", "capacity": 300})
    client.post("/venues", json=KIOSQUE)
    slugs = []
    for venue in client.get("/venues").json():
        slugs.append(venue["slug"])
    assert slugs == ["theatre-des-planches", "le-kiosque"]


def test_unknown_venue_is_404(client):
    response = client.get("/venues/nowhere")
    assert response.status_code == 404
    assert response.json() == {"detail": "Unknown venue: nowhere."}


def test_duplicate_is_409(client):
    client.post("/venues", json=KIOSQUE)
    response = client.post("/venues", json={"name": "le kiosque", "capacity": 80})
    assert response.status_code == 409
    assert response.json() == {"detail": "Le Kiosque already exists."}
    assert len(client.get("/venues").json()) == 1


def test_invalid_venue_is_422(client):
    response = client.post("/venues", json={"name": "Nowhere", "capacity": 0})
    assert response.status_code == 422
    assert response.json() == {"detail": "A venue needs at least one seat, got 0."}
    response = client.post("/venues", json={"name": "  ", "capacity": 10})
    assert response.json() == {"detail": "A venue needs a name."}
    assert client.get("/venues").json() == []


def test_body_of_the_wrong_shape_is_422(client):
    assert client.post("/venues", json={"name": "Le Kiosque"}).status_code == 422
    response = client.post("/venues", json={"name": "X", "capacity": "many"})
    assert response.status_code == 422


def test_delete_venue(client):
    client.post("/venues", json=KIOSQUE)
    response = client.delete("/venues/le-kiosque")
    assert response.status_code == 204
    assert client.get("/venues/le-kiosque").status_code == 404
    assert client.delete("/venues/le-kiosque").status_code == 404


def test_each_app_has_its_own_venues(load_exercise):
    module = load_exercise("02_bodies_errors/venues_api.py")
    first = TestClient(module.create_app())
    second = TestClient(module.create_app())
    first.post("/venues", json=KIOSQUE)
    assert second.get("/venues").json() == []


# --- [ext.] bookings ---------------------------------------------------------------


def test_booking(client):
    client.post("/venues", json={"name": "La Cabane", "capacity": 10})
    response = client.post("/venues/la-cabane/bookings", json={"seats": 8})
    assert response.status_code == 201
    assert response.json()["seats_left"] == 2


def test_booking_errors(client):
    client.post("/venues", json={"name": "La Cabane", "capacity": 10})
    client.post("/venues/la-cabane/bookings", json={"seats": 8})
    response = client.post("/venues/la-cabane/bookings", json={"seats": 3})
    assert response.status_code == 409
    assert response.json() == {"detail": "Not enough seats: 2 left."}
    response = client.post("/venues/la-cabane/bookings", json={"seats": 0})
    assert response.status_code == 422
    response = client.post("/venues/nowhere/bookings", json={"seats": 1})
    assert response.status_code == 404
    assert client.get("/venues/la-cabane").json()["seats_left"] == 2
