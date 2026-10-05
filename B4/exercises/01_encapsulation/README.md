# 01 - Encapsulation

Check: `uv run pytest B4 -k encapsulation`

## wallet.py `[core]`

A festival wallet: money loaded on a wristband, spent at the bars.

`Wallet(owner)` keeps its balance in `self._balance` (starting at 0.0) and the
list of operations in `self._history`.

| Member           | Does                                                                                          |
| ---------------- | --------------------------------------------------------------------------------------------- |
| `balance`        | property, read-only: `wallet.balance = 1000` raises `AttributeError`                          |
| `top_up(amount)` | adds money; `amount <= 0` raises `ValueError("Invalid amount: 0.")`                           |
| `pay(amount)`    | spends money; wrong amount: same error; too high: `ValueError("Balance too low: 10.00 EUR.")` |
| `history()`      | a **copy** of the operations: `[20, -4.5]`                                                    |

## lineup.py `[core]`

`Lineup(title, host)`: the host introduces the acts, in order.

| Member             | Does                                                                 |
| ------------------ | -------------------------------------------------------------------- |
| `host`             | property, read-only                                                  |
| `acts`             | property, read-only, gives a copy of the list                        |
| `add_act(name)`    | adds at the end, name without spaces around it                       |
| `remove_act(name)` | removes; unknown: `ValueError("Max Pellerin is not in the lineup.")` |
| `move_up(name)`    | swaps with the act before; nothing if first; unknown: same error     |
| `len(lineup)`      | number of acts                                                       |
| `str(lineup)`      | `"Opening Gala, hosted by Paul Kerbrat: Nora Lebrun, Max Pellerin"`  |

`add_act` refuses, with a `ValueError`, in this order:

- an empty name: `An act needs a name.`
- the host (any case): `paul kerbrat is the host.`
- an act already there (any case): `NORA LEBRUN is already in the lineup.`
- a seventh act: `The lineup is full (6 acts).`

Hint: a private method `_position(name)` returning the position of an act, or
`None`, is useful three times.
