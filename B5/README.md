# B5 - Web API with FastAPI

The classes of the project already hold the rules. B5 puts a web API in front
of them: the website and the admin of the festival talk to it in JSON.

## Examples

| File                                                      | Content                                                                       |
| --------------------------------------------------------- | ----------------------------------------------------------------------------- |
| [01_http_json.ipynb](examples/01_http_json.ipynb)         | request and response, methods, status codes, JSON, a first app, `TestClient`  |
| [02_routes.ipynb](examples/02_routes.ipynb)               | path and query parameters, conversion and `422`, `HTTPException`, route order |
| [03_bodies_errors.ipynb](examples/03_bodies_errors.ipynb) | `BaseModel` bodies, `201` / `204`, exception handlers, `create_app`           |
| [hello_api.py](examples/hello_api.py)                     | a server to start, then `/docs` in the browser                                |
| [api.md](api.md)                                          | running a server, writing routes, status codes, testing an API                |

```bash
uv run python B5/examples/hello_api.py      # then http://127.0.0.1:8000/docs
```

## Exercises

| Folder                                                   | Exercises                                    |
| -------------------------------------------------------- | -------------------------------------------- |
| [01_first_routes](exercises/01_first_routes/README.md)   | hello_api, jokes_api                         |
| [02_bodies_errors](exercises/02_bodies_errors/README.md) | venues_api, bookings `[ext.]`                |
| [03_festival_api](exercises/03_festival_api/README.md)   | an API around a programme, like the project  |
| [04_project](exercises/04_project/README.md)             | the API of your project, then the submission |

## Checking

```bash
uv run pytest B5 -k first_routes
uv run pytest B5 -k festival_api -v
uv run ruff format B5 && uv run ruff check B5
```
