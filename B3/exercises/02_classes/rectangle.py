"""A first class."""


class Rectangle:
    """A rectangle defined by its width and height."""

    def __init__(self, width: float, height: float) -> None:
        raise NotImplementedError

    def area(self) -> float:
        raise NotImplementedError

    def perimeter(self) -> float:
        raise NotImplementedError

    def is_square(self) -> bool:
        raise NotImplementedError

    def scale(self, factor: float) -> None:
        """Multiply both sides by `factor` (changes the rectangle)."""
        raise NotImplementedError


def main() -> None:
    stage = Rectangle(12, 8)
    print(stage.area(), stage.perimeter(), stage.is_square())
    stage.scale(0.5)
    print(stage.width, stage.height)


if __name__ == "__main__":
    main()
