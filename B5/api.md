# Web APIs with FastAPI

## Start a server

```bash
uv run python B5/examples/hello_api.py
```

```
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```

The terminal is busy while the server runs: open a second one for other
commands. `Ctrl+C` stops the server; start it again after changing the code.

| Open in the browser                             | Gives                                   |
| ----------------------------------------------- | --------------------------------------- |
| <http://127.0.0.1:8000/venues>                  | the JSON of the route                   |
| <http://127.0.0.1:8000/venues?min_capacity=200> | with a query parameter                  |
| <http://127.0.0.1:8000/docs>                    | every route, with a _Try it out_ button |

A browser only sends `GET` requests from its address bar. For `POST`, `PUT`
and `DELETE`, use _Try it out_ in `/docs`.

`127.0.0.1` is your own computer: nobody else can reach this server.

## Write a route

```python
@app.get("/venues/{slug}")  # method and path
def read_venue(slug: str) -> dict:  # {slug} in the path -> parameter
    ...
    return venue  # dict or list -> JSON, status 200
```

| Where the value comes from     | How it is written                                         |
| ------------------------------ | --------------------------------------------------------- |
| the path: `/venues/le-kiosque` | `{slug}` in the path, `slug: str` in the function         |
| the query: `?day=2027-06-11`   | a parameter not in the path: `day: date \| None = None`   |
| the body (JSON)                | a parameter annotated with a `BaseModel`: `body: VenueIn` |

FastAPI converts each value to its annotation (`int`, `date`, `datetime`...)
and answers `422` by itself when it cannot.

## Status codes

| Code | Meaning               | Written as                                                      |
| ---- | --------------------- | --------------------------------------------------------------- |
| 200  | OK                    | default                                                         |
| 201  | created               | `@app.post("/venues", status_code=201)`                         |
| 204  | done, nothing to send | `@app.delete("/venues/{slug}", status_code=204)`, return `None` |
| 404  | not found             | `raise HTTPException(status_code=404, detail="...")`            |
| 409  | conflict              | same, or an exception handler                                   |
| 422  | invalid data          | automatic for a wrong type; a handler for your rules            |
| 500  | bug in the server     | an exception nobody caught                                      |

## Errors of your classes: one handler

The rules stay in the classes, which raise their own exceptions. One handler
turns them into HTTP answers for every route:

```python
@app.exception_handler(FestivalError)
def handle_festival_error(request: Request, error: FestivalError) -> JSONResponse:
    return JSONResponse(status_code=http_status(error), content={"detail": str(error)})
```

Declare the handlers inside `create_app`, with the routes: a handler added
after the first request is ignored.

## Test an API

`TestClient` sends requests without starting a server:

```python
from fastapi.testclient import TestClient


def test_unknown_venue(client):
    response = client.get("/venues/nowhere")
    assert response.status_code == 404
    assert response.json() == {"detail": "Unknown venue: nowhere."}


def test_create_venue(client):
    response = client.post("/venues", json={"name": "Le Kiosque", "capacity": 120})
    assert response.status_code == 201
```

`params={"day": "2027-06-11"}` adds a query string, `json={...}` sends a body.
Build a new application in a fixture for each test, with `create_app`: tests
must not share their data.

## From another program

The website of the project (`web/public/app.js`) calls the API with
JavaScript's `fetch`. From a terminal, `curl` does the same, here with
`venues_api.py` of exercise 02 running:

```bash
curl http://127.0.0.1:8000/venues
curl -X POST http://127.0.0.1:8000/venues -H "Content-Type: application/json" -d '{"name": "La Cabane", "capacity": 40}'
```

On Windows PowerShell, use `curl.exe`, or `/docs`.
