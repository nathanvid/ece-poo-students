"""Times of the festival with datetime objects."""

from datetime import date, datetime, timedelta

DAY_CHANGE = timedelta(hours=6)


def parse_start(text: str) -> datetime:
    """Example: "2027-06-11 20:30" -> datetime(2027, 6, 11, 20, 30)."""
    raise NotImplementedError


def end_of(start: datetime, duration: int) -> datetime:
    """Moment the show ends."""
    raise NotImplementedError


def festival_day(start: datetime) -> date:
    """Day of the programme: a festival day ends at 06:00 the next morning."""
    raise NotImplementedError


def minutes_between(first: datetime, second: datetime) -> int:
    """Whole minutes from `first` to `second`."""
    raise NotImplementedError


def format_slot(start: datetime, duration: int) -> str:
    """Example: "Fri 11 Jun 20:30-21:45"."""
    raise NotImplementedError


def main() -> None:
    start = parse_start("2027-06-12 00:30")
    print(end_of(start, 60))
    print(festival_day(start))
    print(format_slot(start, 60))


if __name__ == "__main__":
    main()
