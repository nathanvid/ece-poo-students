# 04 - Modules and package

Check: `uv run pytest B4 -k modules_package`

`ticketing/` is a small project, organised like the course project will be:

```
ticketing/
├── pyproject.toml          # to complete
├── README.md
└── src/ticketing/
    ├── __init__.py         # to complete
    ├── prices.py           # given: PRICES, price_of(category)
    ├── cart.py             # Cart: to write
    └── cli.py              # given: the command
```

Model: [greetings](../../examples/greetings/README.md) and
[packaging.md](../../packaging.md).

## pyproject.toml

Complete the `[project]` table (description, `readme`, `requires-python =
">=3.12"`, no dependency), declare the command `ticketing` (function `main` of
`ticketing/cli.py`), and the build system `hatchling`.

## \_\_init\_\_.py

`import ticketing` offers `Cart`, `price_of`, `PRICES` and `__version__ =
"0.1.0"`.

## cart.py

| Method                   | Does                                                                                                    |
| ------------------------ | ------------------------------------------------------------------------------------------------------- |
| `add(category, count=1)` | adds tickets; unknown category: the error of `price_of`; `count < 1`: `ValueError("Invalid count: 0.")` |
| `count()`                | number of tickets                                                                                       |
| `total()`                | tickets + `BOOKING_FEE` once per cart; `0.0` for an empty cart                                          |
| `lines()`                | `["3 x full", "1 x child"]`, in the order the categories were first added                               |

## Try it

```bash
cd B4/exercises/04_modules_package/ticketing
uv run ticketing full reduced child child
uv build
```

```
1 x full
1 x reduced
2 x child
Total: 51.50 EUR
```

`uv run` creates a `.venv` in `ticketing/` the first time, and installs the
package in it.
