"""Multiple inheritance: small classes adding one ability each."""


class ToDictMixin:
    """Adds to_dict(): the public attributes of the object."""

    def to_dict(self) -> dict:
        raise NotImplementedError


class ReprMixin:
    """Adds a __repr__ listing the public attributes: Ticket(category='full')."""

    def __repr__(self) -> str:
        raise NotImplementedError


class Ticket(ToDictMixin, ReprMixin):
    def __init__(self, category: str, price: float, code: str) -> None:
        raise NotImplementedError


class Announcer:
    def describe(self) -> str:
        raise NotImplementedError


class Performer:
    def describe(self) -> str:
        raise NotImplementedError


class Host(Announcer, Performer):
    """A host announces and performs: which describe() wins?"""


def mro_names(cls: type) -> list[str]:
    """Names of the classes Python searches, in order: Host, Announcer, ..."""
    raise NotImplementedError


def main() -> None:
    ticket = Ticket("full", 22.0, "X7Q2")
    print(ticket, ticket.to_dict())
    print(Host().describe(), mro_names(Host))


if __name__ == "__main__":
    main()
