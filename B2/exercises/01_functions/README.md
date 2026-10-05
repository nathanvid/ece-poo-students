# 01 - Functions

Check: `uv run pytest B2 -k functions`

## text_tools.py `[core]`

| Function                               | Example                                                             |
| -------------------------------------- | ------------------------------------------------------------------- |
| `initials(full_name)`                  | `"nora lebrun"` → `"N.L."`, `"  léa   fontaine "` → `"L.F."`        |
| `count_vowels(text)`                   | `"Deauville"` → `5` (a, e, i, o, u, y, upper or lower case)         |
| `repeat(word, times=2, separator=" ")` | `repeat("ha")` → `"ha ha"`, `repeat("ha", 3, "-")` → `"ha-ha-ha"`   |
| `is_palindrome(text)`                  | `"Esope reste ici et se repose"` → `True` (spaces and case ignored) |

## number_tools.py `[core]`

| Function                           | Example                                                        |
| ---------------------------------- | -------------------------------------------------------------- |
| `average(values)`                  | `[12.0, 15.5, 9.0]` → `12.1666...`, `[]` → `0.0`               |
| `largest(values)`                  | `[3, 17, 8]` → `17`, without `max()`. The list is never empty. |
| `count_between(values, low, high)` | `([12, 15.5, 8, 17, 10], 10, 16)` → `3` (both limits included) |

## timing.py `[core]`

A time of the festival is written `"HH:MM"`. To compute with it, turn it into
minutes since midnight.

| Function                                                    | Example                                                            |
| ----------------------------------------------------------- | ------------------------------------------------------------------ |
| `to_minutes(clock)`                                         | `"20:30"` → `1230`                                                 |
| `to_clock(minutes)`                                         | `1230` → `"20:30"`, `5` → `"00:05"`, `1500` → `"01:00"` (next day) |
| `end_time(start, duration)`                                 | `("23:30", 90)` → `"01:00"`                                        |
| `overlaps(start_a, duration_a, start_b, duration_b, gap=0)` | see below                                                          |
| `lineup_duration(act_durations, host_break=3)` `[ext.]`     | `[20, 15, 25]` → `66` (the acts + 2 breaks of 3 min)               |

`overlaps` tells whether two shows of the same day are closer than `gap`
minutes. A show from 20:00 to 21:00 and one starting at 21:00 do not overlap;
with `gap=30`, they do: the venue needs 30 minutes between two shows.

Use `to_minutes` and `to_clock` inside the other functions instead of
splitting the text again.
