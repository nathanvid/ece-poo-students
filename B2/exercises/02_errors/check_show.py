"""Check a show before it enters the programme."""

FIELDS = ["title", "artist", "venue", "day", "start", "duration", "price"]
TEXT_FIELDS = ["title", "artist", "venue", "day"]
MAX_DURATION = 360


def parse_clock(text: str) -> int:
    """Minutes since midnight: "20:30" -> 1230.

    Raises:
        ValueError: not a valid HH:MM time.
    """
    raise NotImplementedError


def check_show(show: dict) -> None:
    """Raise ValueError with a clear message for the first problem found."""
    raise NotImplementedError


def valid_shows(shows: list[dict]) -> list[dict]:
    """The shows that pass check_show; the others are skipped with a message."""
    raise NotImplementedError


def main() -> None:
    shows = [
        {
            "title": "Opening Gala",
            "artist": "Paul Kerbrat",
            "venue": "Grand Casino",
            "day": "2027-06-10",
            "start": "20:30",
            "duration": 120,
            "price": 35.0,
        },
        {
            "title": "Too Late",
            "artist": "Max Pellerin",
            "venue": "Le Kiosque",
            "day": "2027-06-10",
            "start": "24:30",
            "duration": 60,
            "price": 12.0,
        },
    ]
    print(f"{len(valid_shows(shows))} valid show(s).")


if __name__ == "__main__":
    main()
