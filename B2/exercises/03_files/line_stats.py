"""Statistics on a text file."""

from pathlib import Path

REVIEW_FILE = Path(__file__).parent / "data" / "review.txt"


def file_stats(path: Path) -> dict:
    """Number of lines and words, and the longest line (without its "\\n")."""
    raise NotImplementedError


def number_lines(source: Path, target: Path) -> None:
    """Copy `source` into `target`, each line starting with its number: "1. "."""
    raise NotImplementedError


def main() -> None:
    stats = file_stats(REVIEW_FILE)
    print(f"Lines: {stats['lines']}")
    print(f"Words: {stats['words']}")
    print(f"Longest line: {stats['longest']}")


if __name__ == "__main__":
    main()
