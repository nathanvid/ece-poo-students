"""A cart of tickets."""

from ticketing.prices import price_of

BOOKING_FEE = 1.5


class Cart:
    """Tickets chosen by one customer, by category."""

    def __init__(self) -> None:
        raise NotImplementedError

    def add(self, category: str, count: int = 1) -> None:
        """Add tickets. Raises ValueError for an unknown category or count < 1."""
        raise NotImplementedError

    def count(self) -> int:
        """Number of tickets in the cart."""
        raise NotImplementedError

    def total(self) -> float:
        """Price of the tickets, plus BOOKING_FEE for the whole cart (none if empty)."""
        raise NotImplementedError

    def lines(self) -> list[str]:
        """One line per category, in the order they were added: "2 x full"."""
        raise NotImplementedError
