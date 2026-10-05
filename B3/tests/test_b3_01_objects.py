from datetime import date, datetime

import pytest


@pytest.fixture
def text_methods(load_exercise):
    return load_exercise("01_objects/text_methods.py")


@pytest.fixture
def dates(load_exercise):
    return load_exercise("01_objects/dates.py")


@pytest.fixture
def festival_time(load_exercise):
    return load_exercise("01_objects/festival_time.py")


# --- text_methods ------------------------------------------------------------------


def test_clean_name(text_methods):
    assert text_methods.clean_name("  nORA   lebrun ") == "Nora Lebrun"
    assert text_methods.clean_name("max") == "Max"


def test_hashtag(text_methods):
    assert text_methods.hashtag("Deauville festival du rire") == (
        "#DeauvilleFestivalDuRire"
    )
    assert text_methods.hashtag("late laughs") == "#LateLaughs"


def test_unique_words(text_methods):
    assert text_methods.unique_words("Ha ha the show THE end") == [
        "end",
        "ha",
        "show",
        "the",
    ]
    assert text_methods.unique_words("") == []


# --- dates -------------------------------------------------------------------------


def test_days_until(dates):
    assert dates.days_until(date(2026, 10, 1), date(2027, 6, 10)) == 252
    assert dates.days_until(date(2027, 6, 11), date(2027, 6, 10)) == -1


def test_weekday_name(dates):
    assert dates.weekday_name(date(2027, 6, 10)) == "Thursday"
    assert dates.weekday_name(date(2027, 6, 13)) == "Sunday"


@pytest.mark.parametrize(
    ("birth", "day", "age"),
    [
        (date(2008, 11, 3), date(2027, 6, 10), 18),
        (date(2009, 6, 10), date(2027, 6, 10), 18),
        (date(2009, 6, 11), date(2027, 6, 10), 17),
    ],
)
def test_age_on(dates, birth, day, age):
    assert dates.age_on(birth, day) == age


# --- festival_time -----------------------------------------------------------------


def test_parse_start(festival_time):
    assert festival_time.parse_start("2027-06-11 20:30") == datetime(
        2027, 6, 11, 20, 30
    )


def test_end_of(festival_time):
    assert festival_time.end_of(datetime(2027, 6, 11, 23, 30), 90) == datetime(
        2027, 6, 12, 1, 0
    )


@pytest.mark.parametrize(
    ("start", "day"),
    [
        (datetime(2027, 6, 11, 20, 30), date(2027, 6, 11)),
        (datetime(2027, 6, 12, 0, 30), date(2027, 6, 11)),
        (datetime(2027, 6, 12, 5, 59), date(2027, 6, 11)),
        (datetime(2027, 6, 12, 6, 0), date(2027, 6, 12)),
    ],
)
def test_festival_day(festival_time, start, day):
    assert festival_time.festival_day(start) == day


def test_minutes_between(festival_time):
    first = datetime(2027, 6, 11, 23, 30)
    assert festival_time.minutes_between(first, datetime(2027, 6, 12, 1, 0)) == 90
    assert festival_time.minutes_between(first, first) == 0


def test_format_slot(festival_time):
    start = datetime(2027, 6, 11, 20, 30)
    assert festival_time.format_slot(start, 75) == "Fri 11 Jun 20:30-21:45"
    late = datetime(2027, 6, 11, 23, 30)
    assert festival_time.format_slot(late, 60) == "Fri 11 Jun 23:30-00:30"
