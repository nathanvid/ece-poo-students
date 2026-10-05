# 02 - Inheritance

Check: `uv run pytest B4 -k inheritance`

## shapes.py `[core]`

```
Shape(name)             area() -> 0.0, describe() -> "rectangle: 12.00"
├── Rectangle(width, height)
│   └── Square(side)
└── Circle(radius)
```

Each subclass calls `super().__init__(...)` and replaces `area()`.
`describe()` is written only in `Shape`. A square is a rectangle with two
equal sides: `Square` reuses the `__init__` of `Rectangle`.

`total_area(shapes)` adds the areas of a list of shapes, whatever their kind.

## performances.py `[core]`

```
Performance(title, venue, start, duration)
├── SoloShow(..., artist, min_age=0)
├── Lineup(..., host, acts)
└── Workshop(..., teacher, max_participants)
```

Artists and venues are plain names here.

**`Performance`** checks the title (`A performance needs a title.`) and the
duration (`Invalid duration: 0 (1 to 360 minutes).`), and gives to every kind:
`end`, `festival_day` (properties), `involves(artist)` and `__str__`:

```
Sat 00:30 | Le Kiosque | Late Laughs (Nora Lebrun, 16+)
```

The part in parentheses is `summary()`. `artists()` and `summary()` raise
`NotImplementedError` in `Performance`: each subclass gives its own.

| Class      | `kind`       | `artists()`         | `summary()`                                                |
| ---------- | ------------ | ------------------- | ---------------------------------------------------------- |
| `SoloShow` | `"solo"`     | `["Nora Lebrun"]`   | `"Nora Lebrun"`, or `"Nora Lebrun, 16+"` if `min_age > 0`  |
| `Lineup`   | `"lineup"`   | host, then the acts | `"hosted by Paul Kerbrat, with Nora Lebrun, Max Pellerin"` |
| `Workshop` | `"workshop"` | `["Inès Moreau"]`   | `"with Inès Moreau, 3/12 places taken"`                    |

`Lineup` refuses fewer than two acts: `A lineup needs at least two acts.`

`Workshop` keeps its participants private: property `participants` (a copy),
`places_left()`, `register(name)` which refuses a name already registered
(`Lou is already registered.`) or a full workshop (`Improv Lab is full.`).

`performances_of(performances, artist)` returns the titles of the
performances where the artist is on stage, using `involves`.

## mixins.py `[ext.]`

- `ToDictMixin.to_dict()`: the attributes of the object whose name does not
  start with `_` (`vars(self)` gives all of them as a dict).
- `ReprMixin.__repr__()`: `Ticket(category='full', price=22.0)`, same
  attributes.
- `Ticket` inherits from both.
- `mro_names(Host)`: `["Host", "Announcer", "Performer", "object"]`, from
  `Host.__mro__`.
