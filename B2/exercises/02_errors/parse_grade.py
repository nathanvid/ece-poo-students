"""Grades typed as text: "12", "15,5", " 8.5 "."""


def parse_grade(text: str) -> float:
    """Turn a text into a grade from 0 to 20.

    A comma is accepted as decimal separator.

    Raises:
        ValueError: not a number, or outside 0 to 20.
    """
    raise NotImplementedError


def average_of(texts: list[str]) -> float:
    """Average of the valid grades; each invalid one is skipped with a message.

    Returns 0.0 if no grade is valid.
    """
    raise NotImplementedError


def main() -> None:
    texts = input("Grades, separated by ';': ").split(";")
    print(f"Average: {average_of(texts):.2f}")


if __name__ == "__main__":
    main()
