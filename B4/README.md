# B4 - Inheritance, abstract classes, packages

## Examples

| File                                                                             | Content                                                               |
| -------------------------------------------------------------------------------- | --------------------------------------------------------------------- |
| [01_encapsulation.ipynb](examples/01_encapsulation.ipynb)                        | `_private`, read-only property, setter, returning copies              |
| [02_inheritance.ipynb](examples/02_inheritance.ipynb)                            | subclass, `super()`, overriding, polymorphism, `isinstance`           |
| [03_abstract_classes.ipynb](examples/03_abstract_classes.ipynb)                  | `ABC`, `@abstractmethod`, a storage interface, a family of exceptions |
| [04_multiple_inheritance.ipynb](examples/04_multiple_inheritance.ipynb) `[ext.]` | mixins, MRO, `super()` along the MRO                                  |
| [05_metaclasses.ipynb](examples/05_metaclasses.ipynb) `[open]`                   | classes are objects, `type`, metaclass, `__init_subclass__`           |
| [greetings/](examples/greetings/README.md)                                       | a package of three files: `pyproject.toml`, `src/`, a command         |
| [packaging.md](packaging.md)                                                     | modules, imports, packages, `pyproject.toml`, `uv build`              |
| [review.md](review.md)                                                           | code review workshop                                                  |

## Exercises

| Folder                                                         | Exercises                                   |
| -------------------------------------------------------------- | ------------------------------------------- |
| [01_encapsulation](exercises/01_encapsulation/README.md)       | wallet, lineup                              |
| [02_inheritance](exercises/02_inheritance/README.md)           | shapes, performances, mixins `[ext.]`       |
| [03_abstract_classes](exercises/03_abstract_classes/README.md) | notifier, storage                           |
| [04_modules_package](exercises/04_modules_package/README.md)   | the `ticketing` package                     |
| [05_project](exercises/05_project/README.md)                   | the project becomes the `deauville` package |

`05_project` is due before B5: your design, the model and its tests, on your
repository.

## Checking

```bash
uv run pytest B4 -k inheritance
uv run ruff format B4 && uv run ruff check B4
```
