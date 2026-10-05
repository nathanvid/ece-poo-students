"""A prepaid festival wallet: its balance only changes through its methods."""


class Wallet:
    """Money loaded on a festival wristband, spent at the bars.

    The balance is private (`_balance`): read it with the `balance` property,
    change it with `top_up` and `pay`, which check every amount.
    """

    def __init__(self, owner: str) -> None:
        raise NotImplementedError

    @property
    def balance(self) -> float:
        raise NotImplementedError

    def top_up(self, amount: float) -> None:
        """Add money. Raises ValueError if amount is not positive."""
        raise NotImplementedError

    def pay(self, amount: float) -> None:
        """Spend money. Raises ValueError if amount is wrong or too high."""
        raise NotImplementedError

    def history(self) -> list[float]:
        """Every operation, + for a top-up, - for a payment. A copy."""
        raise NotImplementedError


def main() -> None:
    wallet = Wallet("Lina")
    wallet.top_up(20)
    wallet.pay(4.5)
    print(wallet.balance, wallet.history())


if __name__ == "__main__":
    main()
