# 01 - Variables, types, input and output

Check: `uv run pytest B1 -k variables_io`

## rectangle.py `[core]`

Ask the width then the height of a rectangle (decimal numbers allowed) and print
its area and perimeter with 2 decimals.

```
Width: 5
Height: 2.5
Area: 12.50
Perimeter: 15.00
```

## seconds.py `[core]`

Ask a number of seconds and print it in hours, minutes and seconds.

```
Seconds: 3725
1 h 2 min 5 s
```

```
Seconds: 59
0 h 0 min 59 s
```

Hint: one hour is 3600 seconds. `//` and `%` do all the work.

## receipt.py `[core]`

The festival box office sells two kinds of tickets:

| Ticket     | Price     |
| ---------- | --------- |
| full price | 22.00 EUR |
| reduced    | 12.00 EUR |

Each ticket also costs 1.50 EUR of booking fees.

Ask how many tickets of each kind are bought, then print the receipt.

```
Full-price tickets: 2
Reduced tickets: 1
Tickets: 3
Subtotal: 56.00 EUR
Booking fees: 4.50 EUR
Total: 60.50 EUR
```

The prices are already stored in constants at the top of the file (names in
CAPITALS). Use them instead of writing `22.0` in your calculations.
