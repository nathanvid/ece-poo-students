"""Deauville Festival du Rire - programme manager, B2 version.

Instructions in README.md.
"""

import json
from pathlib import Path

DATA_FILE = Path(__file__).parent / "programme.json"

FIELDS = ["title", "artist", "venue", "day", "start", "duration", "price"]
TEXT_FIELDS = ["title", "artist", "venue", "day"]
MAX_DURATION = 360
VENUE_CHANGEOVER = 30
ARTIST_REST = 30


# --- Files ---------------------------------------------------------------------


def load_programme(path: Path) -> list[dict]:
    """Read the shows saved in a JSON file.

    Returns an empty list if the file does not exist yet.

    Raises:
        ValueError: the file is not valid JSON.
    """
    raise NotImplementedError


def save_programme(shows: list[dict], path: Path) -> None:
    """Write the shows to a JSON file, indented, accents kept as they are."""
    raise NotImplementedError


# --- Times ---------------------------------------------------------------------


def to_minutes(clock: str) -> int:
    """Minutes since midnight: "20:30" -> 1230.

    Raises:
        ValueError: not a valid HH:MM time.
    """
    raise NotImplementedError


def to_clock(minutes: int) -> str:
    """1230 -> "20:30", 1500 -> "01:00"."""
    raise NotImplementedError


def end_time(show: dict) -> str:
    """Time at which the show ends, e.g. "22:30"."""
    raise NotImplementedError


# --- Rules ---------------------------------------------------------------------


def check_show(show: dict) -> None:
    """Raise ValueError with a clear message for the first problem found."""
    raise NotImplementedError


def too_close(show_a: dict, show_b: dict, gap: int) -> bool:
    """True if two shows of the same day are less than `gap` minutes apart."""
    raise NotImplementedError


def find_clash(shows: list[dict], new_show: dict) -> str | None:
    """Describe the first show that prevents `new_show`, or None if it fits."""
    raise NotImplementedError


def add_show(shows: list[dict], new_show: dict) -> None:
    """Add a show after checking it.

    Raises:
        ValueError: a field is wrong, or the venue or the artist is busy.
    """
    raise NotImplementedError


# --- Programme -----------------------------------------------------------------


def start_of(show: dict) -> int:
    """Sorting key: start of the show, in minutes since midnight."""
    raise NotImplementedError


def shows_of_day(shows: list[dict], day: str) -> list[dict]:
    """The shows of one day, sorted by start time."""
    raise NotImplementedError


def print_day(shows: list[dict], day: str) -> None:
    print(f"Programme for {day}:")
    day_shows = shows_of_day(shows, day)
    if len(day_shows) == 0:
        print("No show that day.")
    for show in day_shows:
        print(
            f"{show['start']}-{end_time(show)} | {show['venue']} | "
            f"{show['title']} ({show['artist']})"
        )


# --- Program -------------------------------------------------------------------


def ask_show() -> dict:
    """Ask the fields of a new show.

    Raises:
        ValueError: the duration or the price is not a number.
    """
    show = {}
    for field in TEXT_FIELDS:
        show[field] = input(f"{field.capitalize()}: ").strip()
    show["start"] = input("Start (HH:MM): ").strip()
    show["duration"] = int(input("Duration (min): "))
    show["price"] = float(input("Price (EUR): "))
    return show


def main() -> None:
    try:
        shows = load_programme(DATA_FILE)
    except ValueError as error:
        print(f"Error: {error}")
        return
    print(f"{len(shows)} shows loaded.")

    while True:
        command = input("Command (day/add/quit): ").strip().lower()
        if command == "quit":
            break
        elif command == "day":
            print_day(shows, input("Day (YYYY-MM-DD): ").strip())
        elif command == "add":
            try:
                add_show(shows, ask_show())
            except ValueError as error:
                print(f"Error: {error}")
                continue
            save_programme(shows, DATA_FILE)
            print(f"Saved: {len(shows)} shows.")
        else:
            print("Unknown command.")


if __name__ == "__main__":
    main()
