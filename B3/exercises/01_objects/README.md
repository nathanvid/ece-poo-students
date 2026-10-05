# 01 - Using objects

Check: `uv run pytest B3 -k objects`

## text_methods.py `[core]`

One line each is possible, by chaining methods.

| Function             | Example                                                                                         |
| -------------------- | ----------------------------------------------------------------------------------------------- |
| `clean_name(text)`   | `"  nORA   lebrun "` → `"Nora Lebrun"`                                                          |
| `hashtag(text)`      | `"Deauville festival du rire"` → `"#DeauvilleFestivalDuRire"`                                   |
| `unique_words(text)` | `"Ha ha the show THE end"` → `["end", "ha", "show", "the"]` (lower case, no repetition, sorted) |

## dates.py `[core]`

| Function                   | Example                                                                            |
| -------------------------- | ---------------------------------------------------------------------------------- |
| `days_until(today, event)` | `(date(2026, 10, 1), date(2027, 6, 10))` → `252`; negative when the event is over  |
| `weekday_name(day)`        | `date(2027, 6, 10)` → `"Thursday"`                                                 |
| `age_on(birth, day)`       | born `date(2009, 6, 11)`, on `date(2027, 6, 10)` → `17` (birthday not reached yet) |

## festival_time.py `[core]`

A festival day runs from 06:00 to 06:00 the next morning: a show starting at
00:30 on 12 June is part of the programme of 11 June.

| Function                         | Example                                                               |
| -------------------------------- | --------------------------------------------------------------------- |
| `parse_start(text)`              | `"2027-06-11 20:30"` → `datetime(2027, 6, 11, 20, 30)`                |
| `end_of(start, duration)`        | `(datetime(2027, 6, 11, 23, 30), 90)` → `datetime(2027, 6, 12, 1, 0)` |
| `festival_day(start)`            | `datetime(2027, 6, 12, 0, 30)` → `date(2027, 6, 11)`                  |
| `minutes_between(first, second)` | 23:30 and 01:00 the next day → `90`                                   |
| `format_slot(start, duration)`   | `"Fri 11 Jun 20:30-21:45"`                                            |

Hint: `DAY_CHANGE` is already in the file. `timedelta` has
`total_seconds()`. The codes of `format_slot` are in the example notebook.
