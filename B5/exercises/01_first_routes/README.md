# 01 - First routes

Check: `uv run pytest B5 -k first_routes`

Try by hand: start the file, then open <http://127.0.0.1:8000/docs>.

```bash
uv run python B5/exercises/01_first_routes/hello_api.py
```

## hello_api.py `[core]`

`GET /` is written. Add three routes:

| Request                   | Answer                                  |
| ------------------------- | --------------------------------------- |
| `GET /hello/Nora`         | `{"message": "Hello, Nora!"}`           |
| `GET /hello/Nora?lang=fr` | `{"message": "Bonjour, Nora!"}`         |
| `GET /hello/Max?lang=xx`  | unknown language: `"Hello, Max!"`       |
| `GET /add?a=2&b=40`       | `{"a": 2, "b": 40, "sum": 42}`          |
| `GET /add?a=two&b=40`     | `422`, written by FastAPI, not by you   |
| `GET /languages`          | `["en", "es", "fr"]`: keys of GREETINGS |

## jokes_api.py `[core]`

`JOKES` is a list of dicts. Write `find_joke` and `list_jokes`, then the
other routes.

| Request                         | Answer                                                        |
| ------------------------------- | ------------------------------------------------------------- |
| `GET /jokes`                    | every joke, in id order                                       |
| `GET /jokes?artist=nora lebrun` | the jokes of one artist, whatever the case                    |
| `GET /jokes?limit=2`            | the first 2                                                   |
| `GET /jokes/2`                  | the joke with id 2                                            |
| `GET /jokes/99`                 | `404`, `{"detail": "No joke with id 99."}`                    |
| `GET /jokes/top?count=3`        | the 3 most liked, most liked first (`count` defaults to 3)    |
| `GET /stats`                    | `{"jokes": 5, "artists": [...], "likes": 92}`, artists sorted |

`find_joke` raises the `HTTPException`: the route only calls it.

Routes are tried in the order they are written: see the end of
[02_routes.ipynb](../../examples/02_routes.ipynb).
