# 03 - Special methods

Check: `uv run pytest B3 -k special_methods`

## duration.py `[core]`

`Duration(minutes)`:

| Written                                | Gives                                   |
| -------------------------------------- | --------------------------------------- |
| `str(Duration(45))`                    | `"45 min"`                              |
| `str(Duration(95))`                    | `"1h35"`                                |
| `repr(Duration(95))`                   | `"Duration(95)"`                        |
| `Duration(60) == Duration(60)`         | `True`; `Duration(60) == 60` is `False` |
| `sorted(...)`, `max(...)`              | by number of minutes                    |
| `Duration(20) + Duration(45)` `[ext.]` | `Duration(65)`                          |

## artist.py `[core]`

`Artist(name, bio="")` stores the name and the bio without the spaces around
them. An empty name raises `ValueError("An artist needs a name.")`.

| Written                                           | Gives                           |
| ------------------------------------------------- | ------------------------------- |
| `Artist("  Nora  LEBRUN ").slug()`                | `"nora-lebrun"`                 |
| `str(nora)`                                       | `"Nora Lebrun"`                 |
| `repr(nora)`                                      | `"Artist('Nora Lebrun')"`       |
| `Artist("Nora Lebrun") == Artist("nora  LEBRUN")` | `True`: same slug               |
| `Artist("Nora Lebrun") in artists`                | uses `==`                       |
| `sorted(artists)`                                 | alphabetical order of the slugs |

Compare the slugs in `__eq__` and `__lt__`: the slug already ignores upper
case and extra spaces.
