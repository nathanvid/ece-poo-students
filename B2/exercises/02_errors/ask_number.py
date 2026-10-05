"""Ask a whole number until the answer is valid."""


def ask_int(question: str, minimum: int, maximum: int) -> int:
    """Ask again until the answer is a whole number from minimum to maximum."""
    raise NotImplementedError


def main() -> None:
    age = ask_int("Age: ", 0, 120)
    tickets = ask_int("Tickets: ", 1, 10)
    print(f"{tickets} ticket(s), age {age}.")


if __name__ == "__main__":
    main()
