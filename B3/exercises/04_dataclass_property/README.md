# 04 - Dataclasses and properties

Check: `uv run pytest B3 -k dataclass_property`

The fields are already declared. Write `__post_init__`, the properties and
the methods.

## temperature.py `[core]`

`Temperature(celsius)`, a dataclass. Below `ABSOLUTE_ZERO`:
`ValueError("Below absolute zero: -300.")`. Two properties: `fahrenheit`
(`celsius × 9 / 5 + 32`) and `kelvin` (`celsius + 273.15`). Changing
`celsius` changes both.

## playlist.py `[core]`

`Playlist(name)` starts with an empty list of songs; two playlists never share
their list. Property `count`, method `add(song)` which ignores a song already
in the list.

## show.py `[core]`

`Show(title, artist, venue, start, duration, price=0.0)`: artist and venue are
still plain names here; they become objects in `05_festival`.

`__post_init__` removes the spaces around the title, then raises a
`ValueError`:

| Problem                   | Message                                     |
| ------------------------- | ------------------------------------------- |
| empty title               | `A show needs a title.`                     |
| duration outside 1 to 360 | `Invalid duration: 400 (1 to 360 minutes).` |
| negative price            | `Invalid price: -1.0.`                      |

| Member                    | Gives                                                                |
| ------------------------- | -------------------------------------------------------------------- |
| `end` (property)          | `start` + `duration`                                                 |
| `festival_day` (property) | the day of the programme: 00:30 on 12 June → 11 June                 |
| `overlaps(other, gap=0)`  | like `timing.overlaps` in B2, with `datetime`: works across midnight |
| `str(show)`               | `"23:30-00:30 \| Le Kiosque \| Late Laughs (Nora Lebrun)"`           |
| `==`                      | same venue and same start (it is the same slot)                      |
| `<`, `sorted`             | by start, then by venue name                                         |

The `__eq__` written in the class replaces the one `@dataclass` would
generate.
