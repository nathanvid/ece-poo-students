"""Several ways to send a message, one interface."""

from abc import ABC, abstractmethod


class Notifier(ABC):
    """Something that can deliver a message."""

    @abstractmethod
    def send(self, message: str) -> None:
        """Deliver one message."""

    def send_all(self, messages: list[str]) -> None:
        raise NotImplementedError


class PrintNotifier(Notifier):
    """Prints each message with a prefix: "[SMS] Doors open"."""

    def __init__(self, prefix: str) -> None:
        raise NotImplementedError

    def send(self, message: str) -> None:
        raise NotImplementedError


class MemoryNotifier(Notifier):
    """Keeps the messages in a list, e.g. to test the code that sends them."""

    def __init__(self) -> None:
        raise NotImplementedError

    def send(self, message: str) -> None:
        raise NotImplementedError


def broadcast(notifiers: list[Notifier], message: str) -> None:
    """Send the message with every notifier."""
    raise NotImplementedError


def main() -> None:
    memory = MemoryNotifier()
    broadcast([PrintNotifier("SMS"), memory], "Doors open at 20:00")
    print(memory.sent)


if __name__ == "__main__":
    main()
