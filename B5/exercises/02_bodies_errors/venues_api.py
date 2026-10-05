"""The venues of the festival: read, add, delete and book them through an API.

uv run python B5/exercises/02_bodies_errors/venues_api.py
"""

import unicodedata
from dataclasses import dataclass

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel


class NotEnoughSeatsError(Exception):
    """A booking asks for more seats than there are left."""


def slugify(name: str) -> str:
    """ "Théâtre des Planches" -> "theatre-des-planches"."""
    ascii_name = unicodedata.normalize("NFKD", name).encode("ascii", "ignore")
    words = ascii_name.decode("ascii").lower().split()
    return "-".join(words)


@dataclass
class Venue:
    """A venue with seats, some of them sold. Raises ValueError if invalid."""

    name: str
    capacity: int
    address: str = ""
    sold: int = 0

    def __post_init__(self) -> None:
        self.name = self.name.strip()
        if self.name == "":
            raise ValueError("A venue needs a name.")
        if self.capacity < 1:
            raise ValueError(f"A venue needs at least one seat, got {self.capacity}.")

    @property
    def slug(self) -> str:
        return slugify(self.name)

    def seats_left(self) -> int:
        return self.capacity - self.sold

    def book(self, seats: int) -> None:
        """Sell `seats` seats. Raises ValueError or NotEnoughSeatsError."""
        if seats < 1:
            raise ValueError(f"A booking is at least one seat, got {seats}.")
        if seats > self.seats_left():
            raise NotEnoughSeatsError(f"Not enough seats: {self.seats_left()} left.")
        self.sold += seats

    def to_dict(self) -> dict:
        return {
            "slug": self.slug,
            "name": self.name,
            "capacity": self.capacity,
            "address": self.address,
            "seats_left": self.seats_left(),
        }


class VenueIn(BaseModel):
    """Body of POST /venues."""

    name: str
    capacity: int
    address: str = ""


class BookingIn(BaseModel):
    """Body of POST /venues/{slug}/bookings."""

    seats: int


def create_app() -> FastAPI:
    """A new application, with its own empty dict of venues."""
    app = FastAPI(title="Venues")
    venues: dict[str, Venue] = {}  # noqa: F841 (used by the routes you write)

    def find_venue(slug: str) -> Venue:
        """The venue with this slug. Raises HTTPException (404) if unknown."""
        raise NotImplementedError

    # 1. The exception handlers: ValueError -> 422, NotEnoughSeatsError -> 409.
    # 2. The routes: GET /venues, GET /venues/{slug}, POST /venues,
    #    DELETE /venues/{slug}, then [ext.] POST /venues/{slug}/bookings.

    return app


def main() -> None:
    import uvicorn

    uvicorn.run(create_app(), host="127.0.0.1", port=8000)


if __name__ == "__main__":
    main()
