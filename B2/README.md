# B2 - Functions, errors, files, Git

## Examples

| File                                                | Content                                                                 |
| --------------------------------------------------- | ----------------------------------------------------------------------- |
| [01_functions.ipynb](examples/01_functions.ipynb)   | `def`, parameters, `return`, default values, annotations, docstrings    |
| [02_errors.ipynb](examples/02_errors.ipynb)         | reading a traceback, `try / except`, `raise`                            |
| [traceback_demo.py](examples/traceback_demo.py)     | a program that crashes: read its traceback in the terminal              |
| [03_files.ipynb](examples/03_files.ipynb)           | `Path`, text files, CSV, JSON                                           |
| [04_decorators.ipynb](examples/04_decorators.ipynb) | functions as values, `sorted(key=...)`, reading and writing a decorator |
| [05_libraries.ipynb](examples/05_libraries.ipynb)   | `import`, standard library, `uv add`, `rich`                            |
| [git.md](git.md)                                    | Git and GitHub: first repository, commits, push                         |

```bash
uv run python B2/examples/traceback_demo.py
```

## Exercises

From B2 on, exercises are functions. Replace each `raise NotImplementedError`
with your code. The tests import your file and call the functions; `main()`,
at the bottom, is there to try them by hand:

```bash
uv run python B2/exercises/01_functions/timing.py
```

| Folder                                                                 | Exercises                                                     |
| ---------------------------------------------------------------------- | ------------------------------------------------------------- |
| [01_functions](exercises/01_functions/README.md)                       | text_tools, number_tools, timing                              |
| [02_errors](exercises/02_errors/README.md)                             | ask_number, parse_grade, check_show                           |
| [03_files](exercises/03_files/README.md)                               | line_stats, shows_csv                                         |
| [04_decorators_libraries](exercises/04_decorators_libraries/README.md) | stats, programme_table, decorators `[ext.]`                   |
| [05_festival](exercises/05_festival/README.md)                         | festival: first version of the project, in its own repository |

`05_festival` is due before B3, pushed on GitHub.

## Checking

```bash
uv run pytest B2 -k timing      # one exercise
uv run pytest B2 -k festival    # the project step
uv run ruff format B2
uv run ruff check B2            # unused variables, forgotten imports...
```
