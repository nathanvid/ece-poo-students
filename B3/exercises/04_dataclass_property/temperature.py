"""A dataclass with checks and computed attributes."""

from dataclasses import dataclass

ABSOLUTE_ZERO = -273.15


@dataclass
class Temperature:
    celsius: float

    def __post_init__(self) -> None:
        raise NotImplementedError

    @property
    def fahrenheit(self) -> float:
        raise NotImplementedError

    @property
    def kelvin(self) -> float:
        raise NotImplementedError


def main() -> None:
    evening = Temperature(18.5)
    print(evening)
    print(evening.fahrenheit, evening.kelvin)


if __name__ == "__main__":
    main()
