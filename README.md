# Object-Oriented Programming in Python

ECE Paris - 2026-2027

**Practice repository.** The course follows the project track: you build the
festival platform step by step, in your own repository. This repository is
optional: more examples (notebooks) and exercises with tests, block by block,
when a notion needs practice. Each sheet of the track points to the matching
part. The `05_festival` and `05_project` / `04_project` exercises are older
versions of the project: the track replaces them.

| Block              | Topic                                   |
| ------------------ | --------------------------------------- |
| [B1](B1/README.md) | Python basics                           |
| [B2](B2/README.md) | Functions, files, errors, Git           |
| [B3](B3/README.md) | Using and writing classes               |
| [B4](B4/README.md) | Inheritance, abstract classes, packages |
| [B5](B5/README.md) | Web API with FastAPI                    |

## Course project

The Deauville Festival du Rire is a new comedy festival (10-13 June 2027). It
needs a platform to publish its artists, venues and shows, with rules that a
generic CMS such as WordPress does not handle: a venue cannot host two shows at
the same time, an artist cannot be on two stages at once, a show at 00:30
belongs to the previous evening's programme.

The project is graded on three levels:

| Level | Status   | Criteria                                                    |
| ----- | -------- | ----------------------------------------------------------- |
| P1    | required | the program works, handles its errors, is readable          |
| P2    | expected | the code is organised in coherent classes                   |
| P3    | bonus    | tooling, tests, documentation, installable package, web API |

Submission: a Git repository.

## Setup

1. Install uv:
   - macOS / Linux: `curl -LsSf https://astral.sh/uv/install.sh | sh`
   - Windows (PowerShell):
     `powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"`

   Close the terminal, open a new one, check with `uv --version`.

2. Install VS Code with the extensions _Python_ and _Jupyter_ (Microsoft) and _Ruff_ (Astral).
   Keep the course folder outside OneDrive.
3. Open this folder in VS Code, then a terminal (`Terminal > New Terminal`).
4. `uv sync` installs Python 3.12 and the tools in `.venv/`.
5. `uv run python B1/examples/01_hello.py`
6. Open `B1/examples/02_variables_types.ipynb`, click _Select Kernel_ (top right),
   choose `.venv`, then _Run All_.

Always start commands with `uv run`: it uses the project's Python and tools.

## Useful commands

```bash
uv run python B1/exercises/02_conditions/ticket_price.py   # run a script
uv run pytest B1                                           # test all B1 exercises
uv run pytest B1 -k ticket                                 # only the tests about "ticket"
uv run ruff format B1                                      # format the code
```

Exercise labels: `[core]` for everyone, `[ext.]` for going further.
