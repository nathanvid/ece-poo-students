"""Show the programme as a table in the terminal, with rich."""

import json
from pathlib import Path

from rich.console import Console
from rich.table import Table

DATA_FILE = Path(__file__).parent / "programme.json"
TITLE = "Deauville Festival du Rire"


def start_key(show: dict) -> str:
    """Sorting key: "2027-06-10 20:30"."""
    raise NotImplementedError


def sort_shows(shows: list[dict]) -> list[dict]:
    """A new list of the shows, in chronological order."""
    raise NotImplementedError


def format_price(price: float) -> str:
    """0.0 -> "free", 22.0 -> "22.00 EUR"."""
    raise NotImplementedError


def build_table(shows: list[dict]) -> Table:
    """A rich table titled TITLE, one row per show in chronological order.

    Columns: Day, Time, Venue, Title, Artist, Price.
    """
    raise NotImplementedError


def main() -> None:
    with open(DATA_FILE, encoding="utf-8") as file:
        shows = json.load(file)
    Console().print(build_table(shows))


if __name__ == "__main__":
    main()
