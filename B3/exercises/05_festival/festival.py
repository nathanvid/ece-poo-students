"""Deauville Festival du Rire - programme manager, B3 version: classes.

Instructions in README.md.
"""

import json
from dataclasses import dataclass
from datetime import date, datetime, timedelta
from pathlib import Path

DATA_FILE = Path(__file__).parent / "programme.json"

DAY_CHANGE = timedelta(hours=6)
MAX_DURATION = 360
VENUE_CHANGEOVER = 30
ARTIST_REST = 30


def slugify(text: str) -> str:
    """Example: "  Nora  LEBRUN " -> "nora-lebrun"."""
    raise NotImplementedError


# --- Artists and venues ----------------------------------------------------------


@dataclass
class Artist:
    """A comedian. Two artists with the same slug are the same artist."""

    name: str
    bio: str = ""

    def __post_init__(self) -> None:
        raise NotImplementedError

    @property
    def slug(self) -> str:
        raise NotImplementedError

    def __eq__(self, other: object) -> bool:
        raise NotImplementedError

    def __lt__(self, other: "Artist") -> bool:
        raise NotImplementedError

    def __str__(self) -> str:
        raise NotImplementedError


@dataclass
class Venue:
    """A venue. Two venues with the same slug are the same venue."""

    name: str
    capacity: int

    def __post_init__(self) -> None:
        raise NotImplementedError

    @property
    def slug(self) -> str:
        raise NotImplementedError

    def __eq__(self, other: object) -> bool:
        raise NotImplementedError

    def __str__(self) -> str:
        raise NotImplementedError


# --- Shows -----------------------------------------------------------------------


@dataclass
class Show:
    """A show. Two shows are equal when they share venue and start."""

    title: str
    artist: Artist
    venue: Venue
    start: datetime
    duration: int
    price: float = 0.0

    def __post_init__(self) -> None:
        raise NotImplementedError

    @property
    def end(self) -> datetime:
        raise NotImplementedError

    @property
    def festival_day(self) -> date:
        """A day ends at 06:00: a show at 00:30 belongs to the evening before."""
        raise NotImplementedError

    def overlaps(self, other: "Show", gap: int = 0) -> bool:
        """True if the two shows are closer than `gap` minutes."""
        raise NotImplementedError

    def to_dict(self) -> dict:
        """Data saved in the JSON file: artist and venue by name."""
        raise NotImplementedError

    def __eq__(self, other: object) -> bool:
        raise NotImplementedError

    def __lt__(self, other: "Show") -> bool:
        raise NotImplementedError

    def __str__(self) -> str:
        raise NotImplementedError


# --- The programme ---------------------------------------------------------------


class Programme:
    """Venues, artists and shows of the festival, with the scheduling rules."""

    def __init__(self, name: str) -> None:
        raise NotImplementedError

    def add_venue(self, venue: Venue) -> None:
        raise NotImplementedError

    def add_artist(self, artist: Artist) -> None:
        raise NotImplementedError

    def find_venue(self, name: str) -> Venue:
        """The venue with this name, whatever the spaces and upper case."""
        raise NotImplementedError

    def find_artist(self, name: str) -> Artist:
        """The artist with this name, whatever the spaces and upper case."""
        raise NotImplementedError

    def find_clash(self, new_show: Show) -> str | None:
        """Describe the first show that prevents `new_show`, or None if it fits."""
        raise NotImplementedError

    def add_show(self, show: Show) -> None:
        """Add a show if its venue and artist are known and free.

        Raises:
            ValueError: unknown venue or artist, or a clash.
        """
        raise NotImplementedError

    def shows_of_day(self, day: date) -> list[Show]:
        """Shows of one festival day, in order."""
        raise NotImplementedError

    def to_dict(self) -> dict:
        raise NotImplementedError

    def save(self, path: Path) -> None:
        raise NotImplementedError


def programme_from_dict(data: dict) -> Programme:
    """Build a programme from the data of the JSON file.

    Every show goes through add_show: the rules are checked again.
    """
    raise NotImplementedError


def load_programme(path: Path) -> Programme:
    """Read a programme saved by Programme.save."""
    raise NotImplementedError


# --- Program ---------------------------------------------------------------------


def print_day(programme: Programme, day: date) -> None:
    print(f"Programme for {day:%A %d %B}:")
    shows = programme.shows_of_day(day)
    if len(shows) == 0:
        print("No show that day.")
    for show in shows:
        print(show)


def ask_show(programme: Programme) -> Show:
    """Ask the fields of a new show.

    Raises:
        ValueError: unknown artist or venue, wrong date, number or value.
    """
    title = input("Title: ")
    artist = programme.find_artist(input("Artist: "))
    venue = programme.find_venue(input("Venue: "))
    start = datetime.fromisoformat(input("Start (YYYY-MM-DD HH:MM): ").strip())
    duration = int(input("Duration (min): "))
    price = float(input("Price (EUR): "))
    return Show(title, artist, venue, start, duration, price)


def main() -> None:
    try:
        programme = load_programme(DATA_FILE)
    except (OSError, ValueError, KeyError) as error:
        print(f"Cannot read {DATA_FILE.name}: {error}")
        return
    print(f"{programme.name}: {len(programme.shows)} shows loaded.")

    while True:
        command = input("Command (day/add/quit): ").strip().lower()
        if command == "quit":
            break
        elif command == "day":
            try:
                day = date.fromisoformat(input("Day (YYYY-MM-DD): ").strip())
            except ValueError as error:
                print(f"Error: {error}")
                continue
            print_day(programme, day)
        elif command == "add":
            try:
                programme.add_show(ask_show(programme))
            except ValueError as error:
                print(f"Error: {error}")
                continue
            programme.save(DATA_FILE)
            print(f"Saved: {len(programme.shows)} shows.")
        else:
            print("Unknown command.")


if __name__ == "__main__":
    main()
