"""Three kinds of performances sharing a common base class."""

from datetime import date, datetime, timedelta

DAY_CHANGE = timedelta(hours=6)
MAX_DURATION = 360


class Performance:
    """What every performance has: title, venue, start, duration.

    Subclasses give artists() and summary().
    """

    kind = "performance"

    def __init__(self, title: str, venue: str, start: datetime, duration: int) -> None:
        raise NotImplementedError

    @property
    def end(self) -> datetime:
        raise NotImplementedError

    @property
    def festival_day(self) -> date:
        raise NotImplementedError

    def artists(self) -> list[str]:
        """Everyone on stage, in order of appearance."""
        raise NotImplementedError

    def summary(self) -> str:
        """Who is on stage, in one line."""
        raise NotImplementedError

    def involves(self, artist: str) -> bool:
        raise NotImplementedError

    def __str__(self) -> str:
        raise NotImplementedError


class SoloShow(Performance):
    kind = "solo"

    def __init__(
        self,
        title: str,
        venue: str,
        start: datetime,
        duration: int,
        artist: str,
        min_age: int = 0,
    ) -> None:
        raise NotImplementedError

    def artists(self) -> list[str]:
        raise NotImplementedError

    def summary(self) -> str:
        raise NotImplementedError


class Lineup(Performance):
    kind = "lineup"

    def __init__(
        self,
        title: str,
        venue: str,
        start: datetime,
        duration: int,
        host: str,
        acts: list[str],
    ) -> None:
        raise NotImplementedError

    def artists(self) -> list[str]:
        raise NotImplementedError

    def summary(self) -> str:
        raise NotImplementedError


class Workshop(Performance):
    kind = "workshop"

    def __init__(
        self,
        title: str,
        venue: str,
        start: datetime,
        duration: int,
        teacher: str,
        max_participants: int,
    ) -> None:
        raise NotImplementedError

    @property
    def participants(self) -> list[str]:
        raise NotImplementedError

    def places_left(self) -> int:
        raise NotImplementedError

    def register(self, name: str) -> None:
        """Raises ValueError if the workshop is full or the name registered."""
        raise NotImplementedError

    def artists(self) -> list[str]:
        raise NotImplementedError

    def summary(self) -> str:
        raise NotImplementedError


def performances_of(performances: list[Performance], artist: str) -> list[str]:
    """Titles of the performances where the artist is on stage."""
    raise NotImplementedError


def main() -> None:
    programme = [
        SoloShow(
            "Late Laughs",
            "Le Kiosque",
            datetime(2027, 6, 11, 23, 30),
            60,
            "Nora Lebrun",
            16,
        ),
        Lineup(
            "Opening Gala",
            "Grand Casino",
            datetime(2027, 6, 10, 20, 30),
            120,
            "Paul Kerbrat",
            ["Nora Lebrun", "Max Pellerin"],
        ),
        Workshop(
            "Improv Lab",
            "Le Kiosque",
            datetime(2027, 6, 11, 15, 0),
            120,
            "Inès Moreau",
            12,
        ),
    ]
    for performance in programme:
        print(performance)
    print(performances_of(programme, "Nora Lebrun"))


if __name__ == "__main__":
    main()
