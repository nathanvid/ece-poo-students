"""A small family of shapes."""

import math


class Shape:
    """Any shape: a name and an area. Subclasses replace area()."""

    def __init__(self, name: str) -> None:
        raise NotImplementedError

    def area(self) -> float:
        raise NotImplementedError

    def describe(self) -> str:
        """Name and area, e.g. "rectangle: 12.00" (area() of the subclass)."""
        raise NotImplementedError


class Rectangle(Shape):
    def __init__(self, width: float, height: float) -> None:
        raise NotImplementedError

    def area(self) -> float:
        raise NotImplementedError


class Square(Rectangle):
    def __init__(self, side: float) -> None:
        raise NotImplementedError


class Circle(Shape):
    def __init__(self, radius: float) -> None:
        raise NotImplementedError

    def area(self) -> float:
        raise NotImplementedError


def total_area(shapes: list[Shape]) -> float:
    raise NotImplementedError


def main() -> None:
    shapes = [Rectangle(4, 3), Square(2), Circle(1)]
    for shape in shapes:
        print(shape.describe())
    print(f"total: {total_area(shapes):.2f}")


if __name__ == "__main__":
    main()
