"""Instance attributes and a class attribute."""


class Counter:
    """Counts something, e.g. the people entering a venue."""

    created = 0
    """Number of counters created so far: shared by all counters."""

    def __init__(self, name: str) -> None:
        raise NotImplementedError

    def increment(self, step: int = 1) -> None:
        raise NotImplementedError

    def reset(self) -> None:
        raise NotImplementedError


def main() -> None:
    door_a = Counter("Door A")
    door_b = Counter("Door B")
    door_a.increment()
    door_a.increment(3)
    door_b.increment()
    print(door_a.value, door_b.value, Counter.created)


if __name__ == "__main__":
    main()
