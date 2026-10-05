import pytest
from fastapi.testclient import TestClient


@pytest.fixture
def hello(load_exercise):
    return TestClient(load_exercise("01_first_routes/hello_api.py").app)


@pytest.fixture
def jokes(load_exercise):
    return TestClient(load_exercise("01_first_routes/jokes_api.py").app)


# --- hello_api ----------------------------------------------------------------------


def test_home(hello):
    response = hello.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the Deauville Festival du Rire."}


def test_hello(hello):
    assert hello.get("/hello/Nora").json() == {"message": "Hello, Nora!"}
    response = hello.get("/hello/Nora", params={"lang": "fr"})
    assert response.json() == {"message": "Bonjour, Nora!"}
    response = hello.get("/hello/Max", params={"lang": "xx"})
    assert response.json() == {"message": "Hello, Max!"}


def test_add(hello):
    assert hello.get("/add", params={"a": 2, "b": 40}).json() == {
        "a": 2,
        "b": 40,
        "sum": 42,
    }


def test_add_refuses_text(hello):
    response = hello.get("/add", params={"a": "two", "b": 40})
    assert response.status_code == 422, "FastAPI checks `a: int` by itself."
    assert hello.get("/add", params={"a": 2}).status_code == 422


def test_languages(hello):
    assert hello.get("/languages").json() == ["en", "es", "fr"]


# --- jokes_api ----------------------------------------------------------------------


def test_list_jokes(jokes):
    data = jokes.get("/jokes").json()
    assert len(data) == 5
    assert data[0]["id"] == 1


def test_list_jokes_filters(jokes):
    nora = jokes.get("/jokes", params={"artist": "nora lebrun"}).json()
    ids = []
    for joke in nora:
        ids.append(joke["id"])
    assert ids == [1, 3]
    assert jokes.get("/jokes", params={"artist": "Nobody"}).json() == []
    assert len(jokes.get("/jokes", params={"limit": 2}).json()) == 2


def test_read_joke(jokes):
    response = jokes.get("/jokes/2")
    assert response.status_code == 200
    assert response.json()["artist"] == "Max Pellerin"


def test_unknown_joke_is_404(jokes):
    response = jokes.get("/jokes/99")
    assert response.status_code == 404
    assert response.json() == {"detail": "No joke with id 99."}
    assert jokes.get("/jokes/two").status_code == 422


def test_top_jokes(jokes):
    response = jokes.get("/jokes/top")
    assert response.status_code == 200, (
        "/jokes/top must be declared before /jokes/{joke_id}."
    )
    likes = []
    for joke in response.json():
        likes.append(joke["likes"])
    assert likes == [30, 25, 18]
    assert len(jokes.get("/jokes/top", params={"count": 1}).json()) == 1


def test_stats(jokes):
    assert jokes.get("/stats").json() == {
        "jokes": 5,
        "artists": ["Inès Moreau", "Max Pellerin", "Nora Lebrun", "Sacha Diallo"],
        "likes": 92,
    }
