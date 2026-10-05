"""A length of time, printed and compared like a value."""


class Duration:
    def __init__(self, minutes: int) -> None:
        raise NotImplementedError

    def __str__(self) -> str:
        """Under one hour "45 min", otherwise "1h35"."""
        raise NotImplementedError

    def __repr__(self) -> str:
        raise NotImplementedError

    def __eq__(self, other: object) -> bool:
        raise NotImplementedError

    def __lt__(self, other: "Duration") -> bool:
        raise NotImplementedError

    def __add__(self, other: "Duration") -> "Duration":
        raise NotImplementedError


def main() -> None:
    acts = [Duration(20), Duration(95), Duration(45)]
    print(sorted(acts))
    print(max(acts))
    print(Duration(20) + Duration(45))


if __name__ == "__main__":
    main()
