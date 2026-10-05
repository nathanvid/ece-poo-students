# 04 - Decorators and libraries

Check: `uv run pytest B2 -k decorators_libraries`

## stats.py `[core]`

`describe(values)` uses `mean` and `median` from the `statistics` module:

```python
describe([120, 75, 90, 60, 130])
# "count 5, mean 95.0, median 90.0, min 60.0, max 130.0"
```

An empty list raises `ValueError("No values to describe.")`.

## programme_table.py `[core]`

Show [programme.json](programme.json) as a table in the terminal, with
[rich](https://rich.readthedocs.io/en/stable/tables.html).

| Function              | Does                                                                                                                                                 |
| --------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| `start_key(show)`     | `"2027-06-10 20:30"`: text that sorts in chronological order                                                                                         |
| `sort_shows(shows)`   | a new sorted list, with `sorted(..., key=start_key)`                                                                                                 |
| `format_price(price)` | `0.0` → `"free"`, `22.0` → `"22.00 EUR"`                                                                                                             |
| `build_table(shows)`  | a `Table` titled `"Deauville Festival du Rire"`, columns `Day`, `Time`, `Venue`, `Title`, `Artist`, `Price`, one row per show in chronological order |

```bash
uv run python B2/exercises/04_decorators_libraries/programme_table.py
```

Add colours or styles if you like: the tests only read the text.

## decorators.py `[ext.]`

Write two decorators, on the model of `announce` in the example notebook.

`logged` prints the call and the result:

```python
@logged
def ticket_total(price, count):
    return price * count


ticket_total(22.0, 3)
# ticket_total called with (22.0, 3)
# ticket_total returned 66.0
```

`shouted` puts the text returned by the function in capitals and adds `!`:
`greet("Nora")` returns `"WELCOME NORA!"`.
