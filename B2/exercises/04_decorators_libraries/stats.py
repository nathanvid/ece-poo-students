"""Describe a list of numbers with the statistics module."""

from statistics import mean, median


def describe(values: list[float]) -> str:
    """One line: count, mean, median, min and max, with one decimal.

    Raises:
        ValueError: the list is empty.
    """
    raise NotImplementedError


def main() -> None:
    print(describe([120, 75, 90, 60, 130]))


if __name__ == "__main__":
    main()
