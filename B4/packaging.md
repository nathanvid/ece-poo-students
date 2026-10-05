# Modules and packages

## A module is a file

`festival.py` is the module `festival`. Another file of the same folder uses
it with `import festival` or `from festival import Show`.

When one file grows past a few hundred lines, split it by subject: one module
for artists, one for performances, one for storage. Each module imports what
it needs from the others.

## A package is a folder of modules

```
src/
└── deauville/
    ├── __init__.py        # makes the folder a package; what `import deauville` offers
    ├── artist.py          # deauville.artist
    ├── performance.py     # deauville.performance
    └── storage/
        ├── __init__.py
        └── json_storage.py   # deauville.storage.json_storage
```

Inside the package, imports start from its name:

```python
from deauville.artist import Artist
from deauville.exceptions import NotFoundError
```

Two modules must not import each other (A imports B, B imports A): Python
stops with `ImportError: cannot import name ... (most likely due to a circular
import)`. Move what they share into a third module.

`__init__.py` usually re-exports the main names, so that users write
`from deauville import Festival` without knowing which file holds it.

## pyproject.toml

```toml
[project]
name = "greetings"                 # name to install it
version = "0.1.0"
description = "Say hello to the audience"
readme = "README.md"
requires-python = ">=3.12"
dependencies = []                  # filled by `uv add rich`...

[project.scripts]
greet = "greetings.cli:main"       # command `greet` = function main of greetings/cli.py

[build-system]                     # the tool that builds the package
requires = ["hatchling"]
build-backend = "hatchling.build"
```

With a `[build-system]`, `uv sync` installs the package itself in `.venv`:
tests and commands import it from anywhere, whatever the current folder.

```bash
uv add rich          # a dependency, written into pyproject.toml
uv add --dev pytest  # a tool for developing only
uv run greet Nora    # the command declared in [project.scripts]
uv build             # dist/greetings-0.1.0-py3-none-any.whl: installable elsewhere
```

## Why `src/`

With the code in `src/`, Python can only find it once installed. The tests
therefore use the package as its users will, not the files lying next to
them. A missing file in the package shows up in the tests, not at the user's.

## Docstrings

The first line of a module, class or function, between `"""`: what it is or
does, in one sentence. Then, if useful, the parameters, the value returned,
the errors raised:

```python
def get_venue(self, slug: str) -> Venue:
    """The venue with this slug.

    Raises:
        NotFoundError: no such venue.
    """
```

VS Code shows it when the mouse is over a call; `help(get_venue)` prints it.

## README.md of the project

What the program does, how to install it, how to run it and its tests, and
what is done (P1, P2, P3). The reader has not attended the course.
