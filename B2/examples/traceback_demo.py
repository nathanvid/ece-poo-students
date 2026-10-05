"""Crashes on purpose: read the traceback from the bottom up.

uv run python B2/examples/traceback_demo.py
"""

PROGRAMME = [
    {"title": "Opening Gala", "start": "20:30", "duration": 120},
    {"title": "Late Laughs", "start": "23:30", "duration": 60},
    {"title": "Improv Lab", "start": "15:00", "length": 90},
]


def to_minutes(clock: str) -> int:
    hours, minutes = clock.split(":")
    return int(hours) * 60 + int(minutes)


def end_minutes(show: dict) -> int:
    return to_minutes(show["start"]) + show["duration"]


def print_programme(shows: list[dict]) -> None:
    for show in shows:
        end = end_minutes(show)
        print(f"{show['title']}: ends at minute {end}")


def main() -> None:
    print_programme(PROGRAMME)


if __name__ == "__main__":
    main()
