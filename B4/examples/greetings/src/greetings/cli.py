"""The `greet` command, declared in pyproject.toml under [project.scripts]."""

import sys

from greetings.core import greet


def main() -> None:
    for name in sys.argv[1:]:
        print(greet(name, excited=True))
