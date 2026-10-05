# 05 - Festival in classes `[core]` - due before B4

Check: `uv run pytest B3 -k festival`

The B2 version worked with dicts and compared `"day"` strings: a show at 00:45
was never compared with one ending at 00:30 the same night. This version uses
classes and `datetime`.

[programme.json](programme.json) has a new format: venues, artists (with a
bio) and shows, which refer to artist and venue by name. It holds 11 shows,
with `After Hours` at 01:00 on 12 June, part of the Friday programme.

```
Deauville Festival du Rire 2027: 11 shows loaded.
Command (day/add/quit): day
Day (YYYY-MM-DD): 2027-06-11
Programme for Friday 11 June:
15:00-17:00 | Le Kiosque | Improv Lab (Inès Moreau)
...
23:30-00:30 | Le Kiosque | Late Laughs (Nora Lebrun)
01:00-02:00 | Le Kiosque | After Hours (Max Pellerin)
Command (day/add/quit): add
Title: Too Late
Artist: karim benali
Venue: le kiosque
Start (YYYY-MM-DD HH:MM): 2027-06-12 02:15
Duration (min): 30
Price (EUR): 5
Error: Le Kiosque is busy with After Hours (Sat 01:00-02:00).
```

`print_day`, `ask_show` and `main` are written.

## The classes

**`Artist`** and **`Venue`** are dataclasses. Names are stored without the
spaces around them; an empty name, or a capacity below 1, raises a
`ValueError`. Property `slug` (`slugify(name)`); two artists, or two venues,
are equal when their slugs are. Artists sort by slug.
`str(venue)` is `"Le Kiosque (120 seats)"`.

**`Show`**: the dataclass of `04_dataclass_property/show.py`, with an `Artist`
and a `Venue` instead of names. `to_dict()` gives the data saved in the file:

```python
{
    "title": "Late Laughs",
    "artist": "Nora Lebrun",
    "venue": "Le Kiosque",
    "start": "2027-06-12T00:30",
    "duration": 60,
    "price": 10.0,
}
```

**`Programme`** holds the lists `venues`, `artists` and `shows`.

| Method                                   | Does                                                                    |
| ---------------------------------------- | ----------------------------------------------------------------------- |
| `add_venue(venue)`, `add_artist(artist)` | adds; an existing one raises `ValueError("Le Kiosque already exists.")` |
| `find_venue(name)`, `find_artist(name)`  | whatever the spaces and case; `ValueError("Unknown venue: Nowhere.")`   |
| `find_clash(new_show)`                   | message of the first conflict, or `None` (below)                        |
| `add_show(show)`                         | unknown venue or artist, then clash: `ValueError`; otherwise adds       |
| `shows_of_day(day)`                      | shows whose `festival_day` is `day`, sorted                             |
| `to_dict()`, `save(path)`                | the whole programme in JSON                                             |

`load_programme(path)` reads the file and calls `programme_from_dict`, which
rebuilds the objects and adds every show with `add_show`: a file with a clash
is refused.

## The rules

Same as in B2 (`VENUE_CHANGEOVER`, `ARTIST_REST`), now across midnight with
`Show.overlaps`. For each show already in the programme, venue first, then
artist:

```
Le Kiosque is busy with Late Laughs (Fri 23:30-00:30).
Nora Lebrun is already on stage in Nothing Serious (Thu 21:00-22:15).
```

## Your tests

[test_festival.py](test_festival.py) has two tests. Add at least six, one
behaviour each: see [testing.md](../../testing.md). The course tests check
that yours pass and that there are at least 8.

```bash
uv run pytest B3/exercises/05_festival -v
```

## In your project repository

Replace `festival.py` and `programme.json` by this version, add
`test_festival.py`, commit, push. The README of the repository says how to run
the program and the tests.
