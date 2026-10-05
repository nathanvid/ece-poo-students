"""A venue of the festival, and its bookings."""


class Venue:
    """A venue with a number of seats, some of them sold."""

    MAX_PER_BOOKING = 10
    """Most tickets one person can buy at once, for every venue."""

    def __init__(self, name: str, capacity: int) -> None:
        raise NotImplementedError

    def seats_left(self) -> int:
        raise NotImplementedError

    def is_full(self) -> bool:
        raise NotImplementedError

    def occupancy(self) -> float:
        """Percentage of seats sold, e.g. 75.0."""
        raise NotImplementedError

    def book(self, count: int) -> None:
        """Sell `count` seats.

        Raises:
            ValueError: count below 1 or above MAX_PER_BOOKING, or not
                enough seats left.
        """
        raise NotImplementedError

    def cancel(self, count: int) -> None:
        """Give back `count` seats.

        Raises:
            ValueError: more seats than sold.
        """
        raise NotImplementedError


def main() -> None:
    kiosque = Venue("Le Kiosque", 120)
    kiosque.book(4)
    kiosque.book(2)
    kiosque.cancel(1)
    print(f"{kiosque.name}: {kiosque.seats_left()} left, {kiosque.occupancy():.1f}%")


if __name__ == "__main__":
    main()
