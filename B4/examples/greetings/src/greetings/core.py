"""The functions of the package."""


def greet(name: str, excited: bool = False) -> str:
    """Hello message for one person.

    >>> greet("Nora")
    'Hello Nora.'
    """
    if excited:
        return f"Hello {name}!"
    return f"Hello {name}."
