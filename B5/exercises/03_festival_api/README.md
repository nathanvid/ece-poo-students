# 03 - An API around the programme `[core]`

Check: `uv run pytest B5 -k festival_api`

```bash
uv run python B5/exercises/03_festival_api/api.py
```

This is the project in small: an API around classes that know nothing about
the web, as your project's API will be.

[shows.py](shows.py) is given complete: `Show`, `Programme` and their errors,
all inheriting from `FestivalError`. Read it first. It knows nothing about
the web. You write [api.py](api.py), which knows nothing about the rules.

## The functions

| Function               | Does                                                                                    |
| ---------------------- | --------------------------------------------------------------------------------------- |
| `http_status(error)`   | status of the first class of `HTTP_STATUS` the error is an instance of; `400` otherwise |
| `show_view(show)`      | `show.to_dict()` plus `id`, `end` and `festival_day`, as texts                          |
| `shows_view(shows)`    | `show_view` of each                                                                     |
| `show_from_body(body)` | a `Show` built from a `ShowIn`                                                          |

```python
{
    "title": "Late Laughs",
    "artist": "Nora Lebrun",
    "venue": "Le Kiosque",
    "start": "2027-06-11T23:30",
    "duration": 60,
    "price": 12.0,
    "id": "le-kiosque-2027-06-11-2330",
    "end": "2027-06-12T00:30",
    "festival_day": "2027-06-11",
}
```

## create_app(programme)

One handler for every `FestivalError`: `{"detail": str(error)}` with
`http_status(error)`. Then the routes, each a few lines:

| Request                         | Calls                   | Success                         |
| ------------------------------- | ----------------------- | ------------------------------- |
| `GET /api/shows`                | `programme.shows()`     | `200`, list                     |
| `GET /api/shows?day=2027-06-11` | `programme.of_day(day)` | `200`, list, the night included |
| `GET /api/shows/{show_id}`      | `programme.get(id)`     | `200`, the show                 |
| `POST /api/shows`               | `programme.add(show)`   | `201`, the show                 |
| `DELETE /api/shows/{show_id}`   | `programme.remove(id)`  | `204`                           |

Errors come from `shows.py` and go through the handler: an unknown id is a
`404`, a clash a `409` (`Le Kiosque is busy with After Hours (Sat 01:00-02:00).`),
a duration of 400 a `422`. `day=June 11` is refused by FastAPI (`422`).

## `[ext.]`

- `PUT /api/shows/{show_id}` replaces a show (its id may change). If the new
  version clashes, the old one is put back: nothing changes, `409`.
- `GET /api/now?at=2027-06-11T21:15` gives
  `{"at": "2027-06-11T21:15", "now_playing": [...]}`; without `at`, the
  current time.
