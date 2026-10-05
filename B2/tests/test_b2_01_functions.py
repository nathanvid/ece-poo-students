import pytest


@pytest.fixture
def text_tools(load_exercise):
    return load_exercise("01_functions/text_tools.py")


@pytest.fixture
def number_tools(load_exercise):
    return load_exercise("01_functions/number_tools.py")


@pytest.fixture
def timing(load_exercise):
    return load_exercise("01_functions/timing.py")


# --- text_tools --------------------------------------------------------------------


@pytest.mark.parametrize(
    ("name", "expected"),
    [("nora lebrun", "N.L."), ("  léa   fontaine ", "L.F."), ("Cher", "C.")],
)
def test_initials(text_tools, name, expected):
    assert text_tools.initials(name) == expected


def test_count_vowels(text_tools):
    assert text_tools.count_vowels("Deauville") == 5
    assert text_tools.count_vowels("RHYTHM") == 1
    assert text_tools.count_vowels("") == 0


def test_repeat(text_tools):
    assert text_tools.repeat("ha") == "ha ha"
    assert text_tools.repeat("ha", 4) == "ha ha ha ha"
    assert text_tools.repeat("ha", 3, "-") == "ha-ha-ha"
    assert text_tools.repeat("ha", separator="", times=2) == "haha"
    assert text_tools.repeat("ha", 1) == "ha"


def test_is_palindrome(text_tools):
    assert text_tools.is_palindrome("Laval")
    assert text_tools.is_palindrome("Esope reste ici et se repose")
    assert not text_tools.is_palindrome("Deauville")


# --- number_tools ------------------------------------------------------------------


def test_average(number_tools):
    assert number_tools.average([12.0, 15.5, 9.0]) == pytest.approx(12.1666, 0.001)
    assert number_tools.average([]) == 0.0


def test_largest(number_tools):
    assert number_tools.largest([3, 17, 8]) == 17
    assert number_tools.largest([-5, -2, -9]) == -2


def test_count_between(number_tools):
    assert number_tools.count_between([12.0, 15.5, 8.0, 17.0, 10.0], 10, 16) == 3
    assert number_tools.count_between([], 0, 20) == 0


# --- timing ------------------------------------------------------------------------


@pytest.mark.parametrize(
    ("clock", "minutes"), [("20:30", 1230), ("00:00", 0), ("09:05", 545)]
)
def test_to_minutes(timing, clock, minutes):
    assert timing.to_minutes(clock) == minutes


@pytest.mark.parametrize(
    ("minutes", "clock"),
    [(1230, "20:30"), (5, "00:05"), (1440, "00:00"), (1500, "01:00")],
)
def test_to_clock(timing, minutes, clock):
    assert timing.to_clock(minutes) == clock


def test_end_time(timing):
    assert timing.end_time("20:30", 75) == "21:45"
    assert timing.end_time("23:30", 90) == "01:00"


def test_overlaps(timing):
    assert timing.overlaps("20:00", 60, "20:30", 60)
    assert timing.overlaps("20:30", 60, "20:00", 60)
    assert timing.overlaps("20:00", 120, "20:30", 30)
    assert not timing.overlaps("20:00", 60, "21:00", 30)
    assert not timing.overlaps("21:00", 30, "20:00", 60)


def test_overlaps_with_gap(timing):
    assert timing.overlaps("20:00", 60, "21:00", 30, gap=30)
    assert timing.overlaps("20:00", 60, "21:29", 30, gap=30)
    assert not timing.overlaps("20:00", 60, "21:30", 30, gap=30)


def test_lineup_duration(timing):
    """[ext.]"""
    assert timing.lineup_duration([20, 15, 25]) == 66
    assert timing.lineup_duration([20, 15], host_break=5) == 40
    assert timing.lineup_duration([30]) == 30
    assert timing.lineup_duration([]) == 0
