"""Where the programme is kept: an abstract class and several storages."""

import csv
import json
from abc import ABC, abstractmethod
from pathlib import Path

FIELDS = ["title", "artist", "venue", "start", "duration", "price"]


class StorageError(Exception):
    """The programme cannot be read or written."""


class ProgrammeStorage(ABC):
    """A place where a list of shows (dicts) is loaded and saved."""

    @abstractmethod
    def load(self) -> list[dict]:
        """The saved shows. Raises StorageError if they cannot be read."""

    @abstractmethod
    def save(self, shows: list[dict]) -> None:
        """Replace the saved shows."""

    def count(self) -> int:
        """Number of saved shows."""
        raise NotImplementedError


class MemoryStorage(ProgrammeStorage):
    """Shows kept in memory: nothing is written anywhere."""

    def __init__(self, shows: list[dict] | None = None) -> None:
        raise NotImplementedError

    def load(self) -> list[dict]:
        raise NotImplementedError

    def save(self, shows: list[dict]) -> None:
        raise NotImplementedError


class JsonStorage(ProgrammeStorage):
    """Shows kept in a UTF-8 JSON file."""

    def __init__(self, path: Path) -> None:
        raise NotImplementedError

    def load(self) -> list[dict]:
        raise NotImplementedError

    def save(self, shows: list[dict]) -> None:
        raise NotImplementedError


class CsvStorage(ProgrammeStorage):
    """Shows kept in a CSV file, columns of FIELDS."""

    def __init__(self, path: Path) -> None:
        raise NotImplementedError

    def load(self) -> list[dict]:
        raise NotImplementedError

    def save(self, shows: list[dict]) -> None:
        raise NotImplementedError


def copy_programme(source: ProgrammeStorage, target: ProgrammeStorage) -> int:
    """Save the shows of `source` into `target`. Returns how many."""
    raise NotImplementedError


def main() -> None:
    memory = MemoryStorage(
        [
            {
                "title": "Late Laughs",
                "artist": "Nora Lebrun",
                "venue": "Le Kiosque",
                "start": "2027-06-11T23:30",
                "duration": 60,
                "price": 12.0,
            }
        ]
    )
    target = JsonStorage(Path("programme_copy.json"))
    print(f"{copy_programme(memory, target)} show(s) copied to {target.path}")


if __name__ == "__main__":
    main()
