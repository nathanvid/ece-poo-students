# B3 - Using and writing classes

## Examples

| File                                                                       | Content                                                                            |
| -------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| [01_objects.ipynb](examples/01_objects.ipynb)                              | attributes and methods of `str`, `list`, `date`, `datetime`, `timedelta`; chaining |
| [02_classes.ipynb](examples/02_classes.ipynb)                              | `class`, `__init__`, `self`, methods, class attribute vs instance attribute        |
| [03_special_methods.ipynb](examples/03_special_methods.ipynb)              | `__str__`, `__repr__`, `__eq__`, `__lt__`, `__add__`                               |
| [04_dataclass_property.ipynb](examples/04_dataclass_property.ipynb)        | `@dataclass`, `__post_init__`, `field(default_factory=...)`, `@property`           |
| [ticket.py](examples/ticket.py), [test_ticket.py](examples/test_ticket.py) | a module and its tests                                                             |
| [testing.md](testing.md)                                                   | writing and running tests with pytest                                              |

```bash
uv run pytest B3/examples -v
```

## Exercises

| Folder                                                             | Exercises                                |
| ------------------------------------------------------------------ | ---------------------------------------- |
| [01_objects](exercises/01_objects/README.md)                       | text_methods, dates, festival_time       |
| [02_classes](exercises/02_classes/README.md)                       | rectangle, counter, venue                |
| [03_special_methods](exercises/03_special_methods/README.md)       | duration, artist                         |
| [04_dataclass_property](exercises/04_dataclass_property/README.md) | temperature, playlist, show              |
| [05_festival](exercises/05_festival/README.md)                     | festival in classes, with your own tests |

`05_festival` is due before B4, pushed on your project repository.

## Checking

```bash
uv run pytest B3 -k special_methods
uv run pytest B3/exercises/05_festival    # your own tests only
uv run ruff format B3 && uv run ruff check B3
```
