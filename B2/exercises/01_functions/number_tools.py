"""Small functions on lists of numbers."""


def average(values: list[float]) -> float:
    """Average of the values, 0.0 for an empty list."""
    raise NotImplementedError


def largest(values: list[float]) -> float:
    """Largest value of a list that is not empty."""
    raise NotImplementedError


def count_between(values: list[float], low: float, high: float) -> int:
    """How many values are between low and high, both included."""
    raise NotImplementedError


def main() -> None:
    grades = [12.0, 15.5, 8.0, 17.0]
    print(average(grades))
    print(largest(grades))
    print(count_between(grades, 10, 16))


if __name__ == "__main__":
    main()
