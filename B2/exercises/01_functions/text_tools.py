"""Small functions on text."""


def initials(full_name: str) -> str:
    """Initials of a name: "nora lebrun" -> "N.L."."""
    raise NotImplementedError


def count_vowels(text: str) -> int:
    """Number of vowels (a, e, i, o, u, y), upper or lower case."""
    raise NotImplementedError


def repeat(word: str, times: int = 2, separator: str = " ") -> str:
    """The word repeated: repeat("ha", 3, "-") -> "ha-ha-ha"."""
    raise NotImplementedError


def is_palindrome(text: str) -> bool:
    """True if the text reads the same both ways, ignoring spaces and case."""
    raise NotImplementedError


def main() -> None:
    print(initials("nora lebrun"))
    print(count_vowels("Deauville"))
    print(repeat("ha", 3, "-"))
    print(is_palindrome("Laval"))


if __name__ == "__main__":
    main()
