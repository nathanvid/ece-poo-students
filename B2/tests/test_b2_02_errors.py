import pytest

from checks import assert_in_order, lines

# --- ask_number --------------------------------------------------------------------


def test_ask_number(run_script):
    output = run_script("02_errors/ask_number.py", lines("abc", "150", "25", "0", "2"))
    assert_in_order(
        output,
        "Please type a whole number.",
        "Please type a number from 0 to 120.",
        "Please type a number from 1 to 10.",
        "2 ticket(s), age 25.",
    )


def test_ask_number_limits_are_allowed(run_script):
    output = run_script("02_errors/ask_number.py", lines("120", "10"))
    assert "10 ticket(s), age 120." in output
    assert "Please" not in output


# --- parse_grade -------------------------------------------------------------------


@pytest.fixture
def parse_grade(load_exercise):
    return load_exercise("02_errors/parse_grade.py")


@pytest.mark.parametrize(
    ("text", "grade"), [("12", 12.0), ("15,5", 15.5), (" 8.5 ", 8.5), ("0", 0.0)]
)
def test_parse_grade(parse_grade, text, grade):
    assert parse_grade.parse_grade(text) == grade


def test_parse_grade_not_a_number(parse_grade):
    with pytest.raises(ValueError, match="Not a number: 'abc'."):
        parse_grade.parse_grade("abc")


@pytest.mark.parametrize("text", ["25", "-1", "20.5"])
def test_parse_grade_out_of_range(parse_grade, text):
    with pytest.raises(ValueError, match="A grade is between 0 and 20"):
        parse_grade.parse_grade(text)


def test_average_of(parse_grade, capsys):
    average = parse_grade.average_of(["12", "abc", "15,5", "25", " 8.5"])
    assert average == 12.0
    output = capsys.readouterr().out
    assert_in_order(
        output,
        "Skipped: Not a number: 'abc'.",
        "Skipped: A grade is between 0 and 20, got 25.0.",
    )


def test_average_of_nothing_valid(parse_grade):
    assert parse_grade.average_of(["abc"]) == 0.0
    assert parse_grade.average_of([]) == 0.0


# --- check_show --------------------------------------------------------------------


@pytest.fixture
def check_show(load_exercise):
    return load_exercise("02_errors/check_show.py")


def good_show() -> dict:
    return {
        "title": "Opening Gala",
        "artist": "Paul Kerbrat",
        "venue": "Grand Casino",
        "day": "2027-06-10",
        "start": "20:30",
        "duration": 120,
        "price": 35.0,
    }


@pytest.mark.parametrize(
    ("text", "minutes"), [("20:30", 1230), ("00:00", 0), ("23:59", 1439), ("9:05", 545)]
)
def test_parse_clock(check_show, text, minutes):
    assert check_show.parse_clock(text) == minutes


@pytest.mark.parametrize("text", ["2030", "24:00", "20:60", "ab:cd", "", "20:30:00"])
def test_parse_clock_refuses(check_show, text):
    with pytest.raises(
        ValueError, match=f"Invalid time: '{text}' \\(expected HH:MM\\)."
    ):
        check_show.parse_clock(text)


def test_good_show_passes(check_show):
    check_show.check_show(good_show())


@pytest.mark.parametrize(
    ("field", "value", "message"),
    [
        ("title", "   ", "Empty field: title."),
        ("venue", "", "Empty field: venue."),
        ("start", "8pm", "Invalid time: '8pm'"),
        ("duration", 0, "Invalid duration: 0 \\(1 to 360 minutes\\)."),
        ("duration", 361, "Invalid duration: 361"),
        ("duration", "90", "Invalid duration: 90"),
        ("price", -5.0, "Invalid price: -5.0."),
    ],
)
def test_check_show_refuses(check_show, field, value, message):
    show = good_show()
    show[field] = value
    with pytest.raises(ValueError, match=message):
        check_show.check_show(show)


@pytest.mark.parametrize("field", ["title", "day", "duration", "price"])
def test_check_show_missing_field(check_show, field):
    show = good_show()
    del show[field]
    with pytest.raises(ValueError, match=f"Missing field: {field}."):
        check_show.check_show(show)


def test_valid_shows(check_show, capsys):
    broken = good_show()
    broken["title"] = "Too Late"
    broken["start"] = "24:30"
    untitled = good_show()
    del untitled["title"]
    other = good_show()
    other["title"] = "Late Laughs"

    result = check_show.valid_shows([good_show(), broken, untitled, other])

    assert result == [good_show(), other]
    assert_in_order(
        capsys.readouterr().out,
        "Skipped 'Too Late': Invalid time: '24:30' (expected HH:MM).",
        "Skipped '?': Missing field: title.",
    )
