# B1 - Python basics

## Examples

Notebooks (`.ipynb`) open in VS Code; outputs are already saved in them.
Run a cell with `Shift+Enter`, change it, run it again.
The two `.py` examples are run in the terminal.

| File | Content |
|---|---|
| [01_hello.py](examples/01_hello.py) | running a file, `print` |
| [02_variables_types.ipynb](examples/02_variables_types.ipynb) | variables, `int` `float` `str` `bool`, operators, f-strings, conversions |
| [03_strings.ipynb](examples/03_strings.ipynb) | indexes, slices, methods, `in`, `split`, `join` |
| [04_input_output.py](examples/04_input_output.py) | `input()`, conversions, asking again until the answer is valid |
| [05_conditions.ipynb](examples/05_conditions.ipynb) | `if / elif / else`, comparisons, `and / or / not` |
| [06_loops.ipynb](examples/06_loops.ipynb) | `for`, `range`, accumulators, `while`, `break`, `continue` |
| [07_lists.ipynb](examples/07_lists.ipynb) | lists: reading, changing, looping, building, nested lists |
| [08_dicts.ipynb](examples/08_dicts.ipynb) | dicts: reading, changing, looping, counting, list of dicts |

## Exercises

Each folder has a `README.md` with the instructions and one `.py` file per
exercise.

| Folder                                                 | Exercises                                              |
| ------------------------------------------------------ | ------------------------------------------------------ |
| [01_variables_io](exercises/01_variables_io/README.md) | rectangle, seconds, receipt                            |
| [02_conditions](exercises/02_conditions/README.md)     | even_odd, leap_year, ticket_price                      |
| [03_loops](exercises/03_loops/README.md)               | countdown, times_table, running_total, lineup_duration |
| [04_lists](exercises/04_lists/README.md)               | grades, words, running_order, seat_map `[ext.]`        |
| [05_dicts](exercises/05_dicts/README.md)               | word_count, phone_book, programme                      |

`05_dicts/programme.py` is due before B2.

## Checking

```bash
uv run pytest B1 -k conditions   # one folder
uv run pytest B1 -k ticket       # one exercise
uv run ruff format B1            # before sharing your code
```

A failing test shows the text it was looking for and what your program
printed.
