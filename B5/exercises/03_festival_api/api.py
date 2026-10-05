"""The web API of the programme, around the classes of shows.py.

Every route is a few lines: read the request, call the programme, answer.
The rules live in shows.py, not here.

    uv run python B5/exercises/03_festival_api/api.py
"""

from datetime import date, datetime
from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from shows import (
    ConflictError,
    FestivalError,
    InvalidDataError,
    NotFoundError,
    Programme,
    Show,
    load_programme,
)

DATA_FILE = Path(__file__).parent / "programme.json"

HTTP_STATUS = [
    (NotFoundError, 404),
    (ConflictError, 409),
    (InvalidDataError, 422),
]


class ShowIn(BaseModel):
    """Body of POST and PUT /api/shows: the fields of Show."""

    title: str
    artist: str
    venue: str
    start: datetime
    duration: int
    price: float = 0.0


def http_status(error: FestivalError) -> int:
    """HTTP status code matching an error of the festival (400 if not listed)."""
    raise NotImplementedError


def show_view(show: Show) -> dict:
    """The saved fields of the show, plus id, end and festival_day."""
    raise NotImplementedError


def shows_view(shows: list[Show]) -> list[dict]:
    raise NotImplementedError


def show_from_body(body: ShowIn) -> Show:
    raise NotImplementedError


def create_app(programme: Programme) -> FastAPI:
    """Build the application around a programme."""
    app = FastAPI(title=programme.name)

    # 1. The handler: every FestivalError -> {"detail": message}, http_status(error).
    # 2. The routes: GET /api/shows, GET /api/shows/{show_id}, POST /api/shows,
    #    DELETE /api/shows/{show_id}, then [ext.] PUT /api/shows/{show_id}
    #    and GET /api/now.

    return app


def main() -> None:
    import uvicorn

    uvicorn.run(create_app(load_programme(DATA_FILE)), host="127.0.0.1", port=8000)


if __name__ == "__main__":
    main()
