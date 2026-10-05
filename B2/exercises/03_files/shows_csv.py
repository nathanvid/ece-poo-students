"""The programme: from a CSV file (made in a spreadsheet) to a JSON file."""

import csv
import json
from pathlib import Path

HERE = Path(__file__).parent
CSV_FILE = HERE / "data" / "programme.csv"
JSON_FILE = HERE / "programme.json"
FIELDS = ["title", "artist", "venue", "day", "start", "duration", "price"]


def load_csv(path: Path) -> list[dict]:
    """Read the shows of a CSV file; duration becomes an int, price a float."""
    raise NotImplementedError


def save_json(shows: list[dict], path: Path) -> None:
    """Write the shows to a JSON file, indented, accents kept as they are."""
    raise NotImplementedError


def load_json(path: Path) -> list[dict]:
    """Read the shows of a JSON file."""
    raise NotImplementedError


def save_csv(shows: list[dict], path: Path) -> None:
    """Write the shows to a CSV file, columns in the order of FIELDS."""
    raise NotImplementedError


def main() -> None:
    shows = load_csv(CSV_FILE)
    save_json(shows, JSON_FILE)
    print(f"{len(shows)} shows written to {JSON_FILE.name}")


if __name__ == "__main__":
    main()
