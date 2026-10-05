"""A show of the festival, as a dataclass."""

from dataclasses import dataclass
from datetime import date, datetime, timedelta

DAY_CHANGE = timedelta(hours=6)
MAX_DURATION = 360


@dataclass
class Show:
    """A show in a venue. Two shows are equal when they share venue and start."""

    title: str
    artist: str
    venue: str
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

    def __str__(self) -> str:
        raise NotImplementedError

    def __eq__(self, other: object) -> bool:
        raise NotImplementedError

    def __lt__(self, other: "Show") -> bool:
        raise NotImplementedError


def main() -> None:
    late = Show(
        "Late Laughs", "Nora Lebrun", "Le Kiosque", datetime(2027, 6, 12, 0, 30), 60
    )
    print(late)
    print(late.end, late.festival_day)


if __name__ == "__main__":
    main()
