# Testing with pytest

A test is a function whose name starts with `test_`, in a file whose name
starts with `test_`. It calls the code and checks the result with `assert`.

```python
from ticket import ticket_price


def test_child_price():
    assert ticket_price(8) == 8.0
```

```bash
uv run pytest B3/examples          # every test_*.py file of the folder
uv run pytest B3/examples -v       # one line per test
uv run pytest B3/examples -k child # only the tests whose name contains "child"
```

A dot per passing test, an `F` per failing one. For a failure, pytest shows
the line of the `assert` and the values on each side.

## Checking that an error is raised

```python
import pytest


def test_negative_age_is_refused():
    with pytest.raises(ValueError, match="Invalid age"):
        ticket_price(-1)
```

The test fails if no `ValueError` is raised, or if its message does not
contain `Invalid age`.

## The same test with several values

```python
@pytest.mark.parametrize(
    ("age", "price"), [(11, 8.0), (12, 12.0), (25, 12.0), (26, 22.0)]
)
def test_limits(age, price):
    assert ticket_price(age) == price
```

Test the limits: the last value before a change and the first one after.

## Objects shared by several tests: fixtures

```python
@pytest.fixture
def kiosque():
    return Venue("Le Kiosque", 120)


def test_new_venue_is_empty(kiosque):
    assert kiosque.seats_left() == 120
```

pytest sees the parameter `kiosque`, calls the fixture of the same name and
gives its result to the test. Each test gets a new object.

`tmp_path` is a fixture given by pytest: an empty temporary folder, to test
saving and loading files without touching the real ones.

## What to test

- one behaviour per test, and a name that says it:
  `test_show_after_midnight_belongs_to_the_evening`;
- the normal case, the limits, and the refused cases (`pytest.raises`);
- a bug found by hand: first a test that fails, then the fix.
