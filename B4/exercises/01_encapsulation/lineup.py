"""A lineup whose running order can only change through its methods."""

MAX_ACTS = 6


class Lineup:
    """A host and the acts they introduce, in order.

    The acts are private: `acts` gives a copy, the methods check the rules.
    """

    def __init__(self, title: str, host: str) -> None:
        raise NotImplementedError

    @property
    def host(self) -> str:
        raise NotImplementedError

    @property
    def acts(self) -> list[str]:
        raise NotImplementedError

    def add_act(self, name: str) -> None:
        """Add an act at the end.

        Raises:
            ValueError: empty name, the host, already in the lineup, or full.
        """
        raise NotImplementedError

    def remove_act(self, name: str) -> None:
        """Raises ValueError if the act is not in the lineup."""
        raise NotImplementedError

    def move_up(self, name: str) -> None:
        """Swap the act with the one before it (nothing if it is first)."""
        raise NotImplementedError

    def _position(self, name: str) -> int | None:
        """Position of an act, ignoring case, or None."""
        raise NotImplementedError

    def __len__(self) -> int:
        raise NotImplementedError

    def __str__(self) -> str:
        raise NotImplementedError


def main() -> None:
    gala = Lineup("Opening Gala", "Paul Kerbrat")
    for name in ["Nora Lebrun", "Max Pellerin", "Léa Fontaine"]:
        gala.add_act(name)
    gala.move_up("Léa Fontaine")
    print(gala)


if __name__ == "__main__":
    main()
