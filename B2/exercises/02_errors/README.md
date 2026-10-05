# 02 - Errors

Check: `uv run pytest B2 -k errors`

## ask_number.py `[core]`

`ask_int(question, minimum, maximum)` asks until the answer is a whole number
from `minimum` to `maximum`, and returns it. `main()` is already written.

```
Age: abc
Please type a whole number.
Age: 150
Please type a number from 0 to 120.
Age: 25
Tickets: 2
2 ticket(s), age 25.
```

## parse_grade.py `[core]`

`parse_grade(text)` turns a text into a grade: `"15,5"` → `15.5`, `" 8.5 "` →
`8.5`. It raises a `ValueError`:

- `Not a number: 'abc'.` when the text is not a number;
- `A grade is between 0 and 20, got 25.0.` when it is out of range.

`average_of(texts)` returns the average of the valid grades. For each invalid
one, it prints `Skipped: ` followed by the message of the error, and goes on.
No valid grade: `0.0`.

```python
average_of(["12", "abc", "15,5", "25", " 8.5"])
# prints: Skipped: Not a number: 'abc'.
#         Skipped: A grade is between 0 and 20, got 25.0.
# returns 12.0
```

## check_show.py `[core]`

A show is a dict with the fields of `FIELDS`. Before it enters the programme,
it must be checked.

`parse_clock(text)` works like `to_minutes`, but raises
`ValueError("Invalid time: '24:30' (expected HH:MM).")` for anything that is
not a valid time: `"2030"`, `"24:00"`, `"20:60"`, `"ab:cd"`, `""`.

`check_show(show)` returns nothing when the show is correct, and raises a
`ValueError` for the first problem found, in this order:

| Problem                                   | Message                                     |
| ----------------------------------------- | ------------------------------------------- |
| a field of `FIELDS` is missing            | `Missing field: title.`                     |
| a text field is empty or only spaces      | `Empty field: venue.`                       |
| wrong start time                          | the message of `parse_clock`                |
| duration not a whole number from 1 to 360 | `Invalid duration: 400 (1 to 360 minutes).` |
| negative price                            | `Invalid price: -5.0.`                      |

`valid_shows(shows)` returns the list of the correct shows. Each wrong one is
skipped with a message: `Skipped 'Too Late': Invalid time: '24:30' (expected HH:MM).`
(`'?'` when the show has no title).

Hints: `isinstance(duration, int)` tells whether a value is a whole number.
`"20".isdigit()` tells whether a text only holds digits.
