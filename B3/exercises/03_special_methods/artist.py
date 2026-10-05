"""An artist, compared by name whatever the spaces and upper case."""


class Artist:
    def __init__(self, name: str, bio: str = "") -> None:
        raise NotImplementedError

    def slug(self) -> str:
        """Example: "  Nora  LEBRUN " -> "nora-lebrun"."""
        raise NotImplementedError

    def __str__(self) -> str:
        raise NotImplementedError

    def __repr__(self) -> str:
        raise NotImplementedError

    def __eq__(self, other: object) -> bool:
        raise NotImplementedError

    def __lt__(self, other: "Artist") -> bool:
        raise NotImplementedError


def main() -> None:
    artists = [Artist("Sacha Diallo"), Artist("max pellerin"), Artist("Nora Lebrun")]
    print(sorted(artists))
    print(Artist("NORA  lebrun") in artists)
    for artist in sorted(artists):
        print(artist)


if __name__ == "__main__":
    main()
