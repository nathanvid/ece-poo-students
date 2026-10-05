import pytest
from rich.console import Console
from rich.table import Table

from checks import assert_in_order, run_python

# --- stats -------------------------------------------------------------------------


@pytest.fixture
def stats(load_exercise):
    return load_exercise("04_decorators_libraries/stats.py")


def test_describe(stats):
    assert stats.describe([120, 75, 90, 60, 130]) == (
        "count 5, mean 95.0, median 90.0, min 60.0, max 130.0"
    )
    assert stats.describe([12.5]) == (
        "count 1, mean 12.5, median 12.5, min 12.5, max 12.5"
    )


def test_describe_empty(stats):
    with pytest.raises(ValueError, match="No values to describe."):
        stats.describe([])


# --- programme_table ---------------------------------------------------------------


@pytest.fixture
def programme_table(load_exercise):
    return load_exercise("04_decorators_libraries/programme_table.py")


def make_show(title: str, day: str, start: str, price: float) -> dict:
    return {
        "title": title,
        "artist": "Nora Lebrun",
        "venue": "Le Kiosque",
        "day": day,
        "start": start,
        "duration": 60,
        "price": price,
    }


SHOWS = [
    make_show("Late", "2027-06-11", "23:30", 12.0),
    make_show("Opening", "2027-06-10", "20:30", 35.0),
    make_show("Morning", "2027-06-11", "09:00", 0.0),
]


def test_start_key(programme_table):
    assert programme_table.start_key(SHOWS[0]) == "2027-06-11 23:30"


def test_sort_shows(programme_table):
    titles = []
    for show in programme_table.sort_shows(SHOWS):
        titles.append(show["title"])
    assert titles == ["Opening", "Morning", "Late"]
    assert SHOWS[0]["title"] == "Late", "sort_shows must not change its argument."


def test_format_price(programme_table):
    assert programme_table.format_price(0.0) == "free"
    assert programme_table.format_price(22.0) == "22.00 EUR"
    assert programme_table.format_price(12.5) == "12.50 EUR"


def test_build_table(programme_table):
    table = programme_table.build_table(SHOWS)
    assert isinstance(table, Table)
    assert table.title == "Deauville Festival du Rire"
    headers = []
    for column in table.columns:
        headers.append(column.header)
    assert headers == ["Day", "Time", "Venue", "Title", "Artist", "Price"]
    assert table.row_count == 3

    console = Console(record=True, width=150)
    console.print(table)
    text = console.export_text()
    assert_in_order(text, "Opening", "35.00 EUR", "Morning", "free", "Late")


def test_programme_table_main(exercise_copy):
    folder = exercise_copy("04_decorators_libraries")
    result = run_python(folder / "programme_table.py")
    assert result.returncode == 0, result.stderr
    assert_in_order(result.stdout, "Opening Gala", "Improv Lab", "Closing Gala")


# --- decorators [ext.] -------------------------------------------------------------


@pytest.fixture
def decorators(load_exercise):
    return load_exercise("04_decorators_libraries/decorators.py")


def test_logged(decorators, capsys):
    @decorators.logged
    def add(a, b):
        return a + b

    assert add(2, 3) == 5
    assert capsys.readouterr().out == "add called with (2, 3)\nadd returned 5\n"


def test_logged_example(decorators, capsys):
    assert decorators.ticket_total(22.0, 3) == 66.0
    assert "ticket_total called with (22.0, 3)" in capsys.readouterr().out


def test_shouted(decorators):
    @decorators.shouted
    def title(name):
        return f"hello {name}"

    assert title("nora") == "HELLO NORA!"
    assert decorators.greet("Nora") == "WELCOME NORA!"
