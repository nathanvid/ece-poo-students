# 02 - Conditions and logical operators

Check: `uv run pytest B1 -k conditions`

## even_odd.py `[core]`

Ask a whole number. Print whether it is even or odd, then whether it is
positive, negative or zero.

```
Number: 7
7 is odd.
7 is positive.
```

```
Number: 0
0 is even.
0 is zero.
```

## leap_year.py `[core]`

A year is a leap year if it is divisible by 4, except years divisible by 100,
which are leap years only if they are also divisible by 400.

```
Year: 2024
2024 is a leap year.
```

```
Year: 1900
1900 is not a leap year.
```

```
Year: 2000
2000 is a leap year.
```

## ticket_price.py `[core]`

Ticket price for one visitor.

1. Ask `Age: `.
2. If the age is below 0 or above 120, print `Invalid age.` and ask nothing else.
3. Otherwise ask `Student? (y/n): `. Only `y` means yes, but `Y` and extra
   spaces must work too.
4. The price is given by the first rule that applies:

   | Rule                    | Price     |
   | ----------------------- | --------- |
   | under 12                | 8.00 EUR  |
   | 25 or under, or student | 12.00 EUR |
   | 65 or over              | 15.00 EUR |
   | everybody else          | 22.00 EUR |

5. Print `Ticket price: 12.00 EUR`.

```
Age: 30
Student? (y/n): n
Ticket price: 22.00 EUR
```

```
Age: 70
Student? (y/n): Y
Ticket price: 12.00 EUR
```

```
Age: 150
Invalid age.
```
