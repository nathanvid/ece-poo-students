"""The `ticketing` command: ticketing full reduced child"""

import sys

from ticketing.cart import Cart


def main() -> int:
    cart = Cart()
    try:
        for category in sys.argv[1:]:
            cart.add(category)
    except ValueError as error:
        print(f"Error: {error}")
        return 1
    for line in cart.lines():
        print(line)
    print(f"Total: {cart.total():.2f} EUR")
    return 0


if __name__ == "__main__":
    sys.exit(main())
