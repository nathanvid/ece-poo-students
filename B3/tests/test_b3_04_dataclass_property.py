from dataclasses import is_dataclass
from datetime import date, datetime

import pytest


@pytest.fixture
def temperature(load_exercise):
    return load_exercise("04_dataclass_property/temperature.py")


@pytest.fixture
def playlist(load_exercise):
    return load_exercise("04_dataclass_property/playlist.py")


@pytest.fixture
def show(load_exercise):
    return load_exercise("04_dataclass_property/show.py")


# --- temperature -------------------------------------------------------------------


def test_temperature(temperature):
    assert is_dataclass(temperature.Temperature)
    evening = temperature.Temperature(18.5)
    assert evening.fahrenheit == pytest.approx(65.3)
    assert evening.kelvin == pytest.approx(291.65)
    evening.celsius = 100
    assert evening.fahrenheit == pytest.approx(212)


def test_temperature_below_absolute_zero(temperature):
    temperature.Temperature(-273.15)
    with pytest.raises(ValueError, match="Below absolute zero"):
        temperature.Temperature(-300)


# --- playlist ----------------------------------------------------------------------


def test_playlist(playlist):
    assert is_dataclass(playlist.Playlist)
    warm_up = playlist.Playlist("Warm-up")
    assert warm_up.songs == []
    assert warm_up.count == 0
    warm_up.add("Opening theme")
    warm_up.add("Drum roll")
    warm_up.add("Opening theme")
    assert warm_up.songs == ["Opening theme", "Drum roll"]
    assert warm_up.count == 2


def test_playlists_do_not_share_their_songs(playlist):
    first = playlist.Playlist("First")
    second = playlist.Playlist("Second")
    first.add("Drum roll")
    assert second.songs == []


# --- show --------------------------------------------------------------------------


def make(
    show,
    title="Late Laughs",
    venue="Le Kiosque",
    start=(2027, 6, 11, 23, 30),
    duration=60,
    price=12.0,
):
    return show.Show(title, "Nora Lebrun", venue, datetime(*start), duration, price)


def test_show_is_a_dataclass(show):
    assert is_dataclass(show.Show)
    late = make(show)
    assert late.title == "Late Laughs"
    assert late.price == 12.0
    free = show.Show("Open Mic", "Max", "Le Kiosque", datetime(2027, 6, 10, 22), 90)
    assert free.price == 0.0


def test_show_checks(show):
    assert make(show, title="  Late  ").title == "Late"
    with pytest.raises(ValueError, match="A show needs a title."):
        make(show, title=" ")
    with pytest.raises(ValueError, match="Invalid duration: 0"):
        make(show, duration=0)
    with pytest.raises(ValueError, match="Invalid duration: 361"):
        make(show, duration=361)
    with pytest.raises(ValueError, match="Invalid price: -1"):
        make(show, price=-1.0)


def test_end_and_festival_day(show):
    late = make(show, start=(2027, 6, 12, 0, 30))
    assert late.end == datetime(2027, 6, 12, 1, 30)
    assert late.festival_day == date(2027, 6, 11)
    late.duration = 90
    assert late.end == datetime(2027, 6, 12, 2, 0), "end must be a @property."
    evening = make(show, start=(2027, 6, 12, 20, 0))
    assert evening.festival_day == date(2027, 6, 12)


def test_overlaps(show):
    first = make(show, start=(2027, 6, 11, 20, 0))
    assert first.overlaps(make(show, start=(2027, 6, 11, 20, 30)))
    assert not first.overlaps(make(show, start=(2027, 6, 11, 21, 0)))
    assert first.overlaps(make(show, start=(2027, 6, 11, 21, 29)), gap=30)
    assert not first.overlaps(make(show, start=(2027, 6, 11, 21, 30)), gap=30)
    late = make(show, start=(2027, 6, 11, 23, 30))
    assert late.overlaps(make(show, start=(2027, 6, 12, 0, 15)))


def test_str(show):
    assert str(make(show)) == "23:30-00:30 | Le Kiosque | Late Laughs (Nora Lebrun)"


def test_equality_is_venue_and_start(show):
    assert make(show) == make(show, title="Other", duration=30)
    assert make(show) != make(show, venue="Grand Casino")
    assert make(show) != make(show, start=(2027, 6, 11, 23, 0))


def test_sorting(show):
    b = make(show, title="B", venue="Le Kiosque", start=(2027, 6, 11, 20, 0))
    a = make(show, title="A", venue="Grand Casino", start=(2027, 6, 11, 20, 0))
    early = make(show, title="Early", start=(2027, 6, 11, 18, 0))
    titles = []
    for one in sorted([b, a, early]):
        titles.append(one.title)
    assert titles == ["Early", "A", "B"]
