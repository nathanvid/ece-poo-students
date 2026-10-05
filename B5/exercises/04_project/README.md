# 04 - The web API of the project `[P3]`

Your project gets a web server: the routes of `API.md` (at the root of your
repository), the website of `web/public/` at `/` and the admin of
`web/admin/` at `/admin/`. Build it as in `03_festival_api`, around your own
classes.

## Steps

1. `uv add fastapi uvicorn`. Choose where the API lives in your package, and
   how the server starts (a command of your CLI, a script...). Write it in
   your README.
2. A first route, `GET /api/venues`, and its test with `TestClient`. Then
   serve the two folders with `StaticFiles` (`html=True`) and open the
   website: the venues appear.
3. The conversion of your errors into HTTP statuses (table of `API.md`), in
   one exception handler: the routes never write `try`.
4. The views: what each object looks like in JSON, field by field as in
   `API.md`. Write them once and reuse them in every route.
5. The read routes, then the write routes used by the admin. After each
   change, save the data file.
6. Your tests: one fixture builds the application on a copy of the data file
   (`tmp_path`), so that tests do not change `data/festival.json` and do not
   depend on each other.

The routes stay short: read the request, call your model, save, answer. A
rule written in a route instead of the model is a rule the command line does
not check.

## Submission

The last push before the deadline is graded. Before it:

```bash
uv run ruff format . && uv run ruff check .
uv run pytest
uv build
```

- The README of the repository is yours: what the project does, how to
  install and run it, how to run the tests, your structure and why, what is
  done and what is not.
- `git status` is clean, and a fresh clone runs with `uv sync` and the
  commands of your README.
- The trainer starts your server on a fresh copy of the data and checks every
  route of `API.md` through HTTP: the website and the admin must work.
