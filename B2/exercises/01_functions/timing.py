"""Times of the festival, as "HH:MM" text or as minutes since midnight."""

HOST_BREAK = 3


def to_minutes(clock: str) -> int:
    """Minutes since midnight: "20:30" -> 1230."""
    raise NotImplementedError


def to_clock(minutes: int) -> str:
    """1230 -> "20:30". After midnight, starts again: 1500 -> "01:00"."""
    raise NotImplementedError


def end_time(start: str, duration: int) -> str:
    """end_time("23:30", 90) -> "01:00"."""
    raise NotImplementedError


def overlaps(
    start_a: str, duration_a: int, start_b: str, duration_b: int, gap: int = 0
) -> bool:
    """True if the two shows (same day) are closer than `gap` minutes."""
    raise NotImplementedError


def lineup_duration(act_durations: list[int], host_break: int = HOST_BREAK) -> int:
    """Total length of a lineup: the acts plus a break between two acts."""
    raise NotImplementedError


def main() -> None:
    print(to_minutes("20:30"))
    print(to_clock(1500))
    print(end_time("23:30", 90))
    print(overlaps("20:00", 60, "21:00", 30))
    print(overlaps("20:00", 60, "21:00", 30, gap=30))
    print(lineup_duration([20, 15, 25]))


if __name__ == "__main__":
    main()
