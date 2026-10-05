"""The festival programme: shows and the rules between them.

This module is given complete. It knows nothing about the web: api.py turns
its objects into JSON and its errors into HTTP status codes.
"""

import json
import unicodedata
from dataclasses import dataclass
from datetime import date, datetime, timedelta
from pathlib import Path

DAY_CHANGE = timedelta(hours=6)
"""A festival day runs from 06:00 to 06:00."""

CHANGEOVER = timedelta(minutes=30)
"""Time a venue, or an artist, needs between two shows."""

MAX_DURATION = 360


class FestivalError(Exception):
    """Base class of every error of this module."""


class InvalidDataError(FestivalError):
    """A value breaks a rule: empty title, duration out of range..."""


class NotFoundError(FestivalError):
    """No show with this id."""


class ConflictError(FestivalError):
    """A venue or an artist would be booked twice at the same time."""


def slugify(name: str) -> str:
    """ "Théâtre des Planches" -> "theatre-des-planches"."""
    ascii_name = unicodedata.normalize("NFKD", name).encode("ascii", "ignore")
    words = ascii_name.decode("ascii").lower().split()
    return "-".join(words)


@dataclass
class Show:
    title: str
    artist: str
    venue: str
    start: datetime
    duration: int
    price: float = 0.0

    def __post_init__(self) -> None:
        self.title = self.title.strip()
        self.artist = self.artist.strip()
        self.venue = self.venue.strip()
        if self.title == "":
            raise InvalidDataError("A show needs a title.")
        if self.artist == "" or self.venue == "":
            raise InvalidDataError("A show needs an artist and a venue.")
        if not 1 <= self.duration <= MAX_DURATION:
            raise InvalidDataError(
                f"Invalid duration: {self.duration} (1 to {MAX_DURATION} minutes)."
            )
        if self.price < 0:
            raise InvalidDataError(f"Invalid price: {self.price}.")

    @property
    def id(self) -> str:
        """Venue and start: "le-kiosque-2027-06-11-2330"."""
        return f"{slugify(self.venue)}-{self.start:%Y-%m-%d-%H%M}"

    @property
    def end(self) -> datetime:
        return self.start + timedelta(minutes=self.duration)

    @property
    def festival_day(self) -> date:
        """The day of the programme: 00:30 on 12 June belongs to 11 June."""
        return (self.start - DAY_CHANGE).date()

    def slot(self) -> str:
        """ "Fri 23:30-00:30"."""
        return f"{self.start:%a %H:%M}-{self.end:%H:%M}"

    def overlaps(self, other: "Show", gap: timedelta = timedelta(0)) -> bool:
        """True if the two shows are closer than `gap`."""
        return self.start < other.end + gap and other.start < self.end + gap

    def to_dict(self) -> dict:
        return {
            "title": self.title,
            "artist": self.artist,
            "venue": self.venue,
            "start": self.start.isoformat(timespec="minutes"),
            "duration": self.duration,
            "price": self.price,
        }


class Programme:
    """The shows of the festival, with the rules checked at each addition."""

    def __init__(self, name: str) -> None:
        self.name = name
        self._shows: list[Show] = []

    def shows(self) -> list[Show]:
        """Every show, by start then venue."""
        return sorted(self._shows, key=lambda show: (show.start, show.venue))

    def get(self, show_id: str) -> Show:
        for show in self._shows:
            if show.id == show_id:
                return show
        raise NotFoundError(f"Unknown show: {show_id}.")

    def find_clash(self, new_show: Show) -> str | None:
        """Message of the first conflict with the programme, or None."""
        for show in self._shows:
            if slugify(show.venue) == slugify(new_show.venue) and show.overlaps(
                new_show, CHANGEOVER
            ):
                return f"{show.venue} is busy with {show.title} ({show.slot()})."
            if slugify(show.artist) == slugify(new_show.artist) and show.overlaps(
                new_show, CHANGEOVER
            ):
                return (
                    f"{show.artist} is already on stage in {show.title} "
                    f"({show.slot()})."
                )
        return None

    def add(self, show: Show) -> None:
        """Raises ConflictError if the venue or the artist is busy."""
        clash = self.find_clash(show)
        if clash is not None:
            raise ConflictError(clash)
        self._shows.append(show)

    def remove(self, show_id: str) -> Show:
        """Remove the show and return it. Raises NotFoundError."""
        show = self.get(show_id)
        self._shows.remove(show)
        return show

    def of_day(self, day: date) -> list[Show]:
        """Shows of one festival day, the night after midnight included."""
        result = []
        for show in self.shows():
            if show.festival_day == day:
                result.append(show)
        return result

    def now_playing(self, at: datetime) -> list[Show]:
        """Shows on stage at this moment."""
        result = []
        for show in self.shows():
            if show.start <= at < show.end:
                result.append(show)
        return result


def show_from_dict(data: dict) -> Show:
    return Show(
        data["title"],
        data["artist"],
        data["venue"],
        datetime.fromisoformat(data["start"]),
        data["duration"],
        data.get("price", 0.0),
    )


def load_programme(path: Path) -> Programme:
    with open(path, encoding="utf-8") as file:
        data = json.load(file)
    programme = Programme(data["name"])
    for show_data in data["shows"]:
        programme.add(show_from_dict(show_data))
    return programme
