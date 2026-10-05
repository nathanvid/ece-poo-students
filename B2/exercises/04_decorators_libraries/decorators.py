"""Two decorators written by hand."""


def logged(function):
    """Print the call and the result each time the function is called."""
    return function  # replace with a wrapper function


def shouted(function):
    """The text returned by the function, in capitals, followed by "!"."""
    return function  # replace with a wrapper function


@logged
def ticket_total(price: float, count: int) -> float:
    return price * count


@shouted
def greet(name: str) -> str:
    return f"welcome {name}"


def main() -> None:
    ticket_total(22.0, 3)
    print(greet("Nora"))


if __name__ == "__main__":
    main()
