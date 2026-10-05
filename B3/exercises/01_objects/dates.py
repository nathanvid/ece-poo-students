"""Dates with the datetime module."""

from datetime import date


def days_until(today: date, event: date) -> int:
    """Days from today to the event (negative when it is over)."""
    raise NotImplementedError


def weekday_name(day: date) -> str:
    """date(2027, 6, 10) -> "Thursday"."""
    raise NotImplementedError


def age_on(birth: date, day: date) -> int:
    """Age of a person born on `birth`, on the given day."""
    raise NotImplementedError


def main() -> None:
    today = date.today()
    festival = date(2027, 6, 10)
    print(f"{days_until(today, festival)} days to go")
    print(weekday_name(festival))
    print(age_on(date(2008, 11, 3), festival))


if __name__ == "__main__":
    main()
