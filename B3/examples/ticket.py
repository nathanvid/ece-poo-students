"""Ticket prices: a small module, and its tests in test_ticket.py."""

FULL_PRICE = 22.0
REDUCED_PRICE = 12.0
CHILD_PRICE = 8.0


def ticket_price(age: int, student: bool = False) -> float:
    """Price of one ticket.

    Raises:
        ValueError: negative age.
    """
    if age < 0:
        raise ValueError(f"Invalid age: {age}.")
    if age < 12:
        return CHILD_PRICE
    if age <= 25 or student:
        return REDUCED_PRICE
    return FULL_PRICE
