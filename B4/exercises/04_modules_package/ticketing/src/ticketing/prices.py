"""Price of each category of ticket."""

PRICES = {"full": 22.0, "reduced": 12.0, "child": 8.0, "guest": 0.0}


def price_of(category: str) -> float:
    """Price of one ticket. Raises ValueError for an unknown category."""
    if category not in PRICES:
        raise ValueError(f"Unknown category: {category}.")
    return PRICES[category]
