"""A dataclass holding a list."""

from dataclasses import dataclass, field


@dataclass
class Playlist:
    name: str
    songs: list[str] = field(default_factory=list)

    @property
    def count(self) -> int:
        raise NotImplementedError

    def add(self, song: str) -> None:
        """Add a song at the end, unless it is already there."""
        raise NotImplementedError


def main() -> None:
    warm_up = Playlist("Warm-up")
    warm_up.add("Opening theme")
    warm_up.add("Drum roll")
    warm_up.add("Opening theme")
    print(warm_up, warm_up.count)


if __name__ == "__main__":
    main()
