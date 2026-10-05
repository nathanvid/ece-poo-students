"""Methods of str and list, one after the other."""


def clean_name(text: str) -> str:
    """Example: "  nORA   lebrun " -> "Nora Lebrun"."""
    raise NotImplementedError


def hashtag(text: str) -> str:
    """Example: "Deauville festival du rire" -> "#DeauvilleFestivalDuRire"."""
    raise NotImplementedError


def unique_words(text: str) -> list[str]:
    """Words of the text, in lower case, without repetition, sorted."""
    raise NotImplementedError


def main() -> None:
    print(clean_name("  nORA   lebrun "))
    print(hashtag("Deauville festival du rire"))
    print(unique_words("Ha ha the show the end"))


if __name__ == "__main__":
    main()
