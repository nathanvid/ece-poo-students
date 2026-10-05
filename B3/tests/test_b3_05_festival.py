import json
import re
import subprocess
import sys
from dataclasses import is_dataclass
from datetime import date, datetime

import pytest

from checks import assert_in_order, lines, run_python


@pytest.fixture
def festival(load_exercise):
    return load_exercise("05_festival/festival.py")


@pytest.fixture
def programme(festival):
    """A programme with two venues and two artists, no show."""
    programme = festival.Programme("Test")
    programme.add_venue(festival.Venue("Le Kiosque", 120))
    programme.add_venue(festival.Venue("Grand Casino", 650))
    programme.add_artist(festival.Artist("Nora Lebrun", "Stories."))
    programme.add_artist(festival.Artist("Max Pellerin"))
    return programme


def make_show(
    festival,
    programme,
    title,
    start,
    venue="Le Kiosque",
    artist="Nora Lebrun",
    duration=60,
):
    return festival.Show(
        title,
        programme.find_artist(artist),
        programme.find_venue(venue),
        datetime.fromisoformat(start),
        duration,
        10.0,
    )


# --- Artist and Venue --------------------------------------------------------------


def test_artist(festival):
    assert is_dataclass(festival.Artist)
    nora = festival.Artist("  Nora  Lebrun ", " Stories. ")
    assert nora.name == "Nora  Lebrun"
    assert nora.bio == "Stories."
    assert nora.slug == "nora-lebrun"
    assert str(nora) == "Nora  Lebrun"
    assert nora == festival.Artist("NORA LEBRUN")
    assert festival.Artist("Max") < festival.Artist("nora")
    with pytest.raises(ValueError):
        festival.Artist(" ")


def test_venue(festival):
    assert is_dataclass(festival.Venue)
    kiosque = festival.Venue(" Le Kiosque ", 120)
    assert kiosque.name == "Le Kiosque"
    assert kiosque.slug == "le-kiosque"
    assert str(kiosque) == "Le Kiosque (120 seats)"
    assert kiosque == festival.Venue("le kiosque", 80)
    with pytest.raises(ValueError):
        festival.Venue("Nowhere", 0)
    with pytest.raises(ValueError):
        festival.Venue("  ", 10)


# --- Show --------------------------------------------------------------------------


def test_show(festival, programme):
    assert is_dataclass(festival.Show)
    late = make_show(festival, programme, " Late Laughs ", "2027-06-12 00:30")
    assert late.title == "Late Laughs"
    assert late.end == datetime(2027, 6, 12, 1, 30)
    assert late.festival_day == date(2027, 6, 11)
    assert str(late) == "00:30-01:30 | Le Kiosque | Late Laughs (Nora Lebrun)"
    assert late.to_dict() == {
        "title": "Late Laughs",
        "artist": "Nora Lebrun",
        "venue": "Le Kiosque",
        "start": "2027-06-12T00:30",
        "duration": 60,
        "price": 10.0,
    }


def test_show_checks(festival, programme):
    with pytest.raises(ValueError):
        make_show(festival, programme, " ", "2027-06-11 20:00")
    with pytest.raises(ValueError):
        make_show(festival, programme, "A", "2027-06-11 20:00", duration=0)


def test_show_equality_and_order(festival, programme):
    a = make_show(festival, programme, "A", "2027-06-11 20:00", venue="Le Kiosque")
    b = make_show(festival, programme, "B", "2027-06-11 20:00", venue="Grand Casino")
    early = make_show(festival, programme, "Early", "2027-06-11 18:00")
    assert a == make_show(festival, programme, "Other", "2027-06-11 20:00")
    assert a != b
    assert sorted([a, b, early]) == [early, b, a]


def test_overlaps(festival, programme):
    first = make_show(festival, programme, "A", "2027-06-11 23:30")
    assert first.overlaps(make_show(festival, programme, "B", "2027-06-12 00:15"))
    assert first.overlaps(
        make_show(festival, programme, "B", "2027-06-12 00:45"), gap=30
    )
    assert not first.overlaps(
        make_show(festival, programme, "B", "2027-06-12 01:00"), gap=30
    )


# --- Programme ---------------------------------------------------------------------


def test_find(festival, programme):
    assert programme.find_venue("  grand CASINO").name == "Grand Casino"
    assert programme.find_artist("max pellerin").name == "Max Pellerin"
    with pytest.raises(ValueError, match="Unknown venue: Nowhere."):
        programme.find_venue("Nowhere")
    with pytest.raises(ValueError, match="Unknown artist: Nobody."):
        programme.find_artist("Nobody")


def test_no_duplicates(festival, programme):
    with pytest.raises(ValueError, match="already exists"):
        programme.add_venue(festival.Venue("le kiosque", 50))
    with pytest.raises(ValueError, match="already exists"):
        programme.add_artist(festival.Artist("NORA LEBRUN"))


def test_venue_clash_after_midnight(festival, programme):
    programme.add_show(
        make_show(festival, programme, "Late Laughs", "2027-06-11 23:30")
    )
    too_soon = make_show(
        festival, programme, "After", "2027-06-12 00:45", artist="Max Pellerin"
    )
    with pytest.raises(ValueError) as error:
        programme.add_show(too_soon)
    assert str(error.value) == "Le Kiosque is busy with Late Laughs (Fri 23:30-00:30)."
    programme.add_show(
        make_show(
            festival, programme, "After", "2027-06-12 01:00", artist="Max Pellerin"
        )
    )
    assert len(programme.shows) == 2


def test_artist_clash(festival, programme):
    programme.add_show(make_show(festival, programme, "Tall Tales", "2027-06-11 20:30"))
    elsewhere = make_show(
        festival, programme, "Second", "2027-06-11 21:45", venue="Grand Casino"
    )
    with pytest.raises(ValueError) as error:
        programme.add_show(elsewhere)
    assert str(error.value) == (
        "Nora Lebrun is already on stage in Tall Tales (Fri 20:30-21:30)."
    )


def test_unknown_venue_or_artist(festival, programme):
    stranger = festival.Artist("Somebody")
    kiosque = programme.find_venue("Le Kiosque")
    start = datetime(2027, 6, 11, 20, 0)
    with pytest.raises(ValueError, match="Unknown artist: Somebody."):
        programme.add_show(festival.Show("A", stranger, kiosque, start, 60))
    nora = programme.find_artist("Nora Lebrun")
    tent = festival.Venue("The Tent", 50)
    with pytest.raises(ValueError, match="Unknown venue: The Tent."):
        programme.add_show(festival.Show("A", nora, tent, start, 60))


def test_shows_of_day(festival, programme):
    late = make_show(festival, programme, "Late", "2027-06-12 01:00")
    early = make_show(festival, programme, "Early", "2027-06-11 18:00")
    other = make_show(festival, programme, "Other", "2027-06-12 18:00")
    for show in [late, other, early]:
        programme.add_show(show)
    assert programme.shows_of_day(date(2027, 6, 11)) == [early, late]
    assert programme.shows_of_day(date(2027, 6, 13)) == []


def test_save_and_load(festival, programme, tmp_path):
    programme.add_show(make_show(festival, programme, "A", "2027-06-11 20:00"))
    path = tmp_path / "programme.json"
    programme.save(path)
    data = json.loads(path.read_text(encoding="utf-8"))
    assert data["name"] == "Test"
    assert data["shows"][0]["start"] == "2027-06-11T20:00"

    loaded = festival.load_programme(path)
    assert loaded.name == "Test"
    assert loaded.shows == programme.shows
    assert sorted(loaded.artists) == sorted(programme.artists)
    assert loaded.find_artist("Nora Lebrun").bio == "Stories."


def test_loading_checks_the_rules(festival, programme, tmp_path):
    programme.add_show(make_show(festival, programme, "A", "2027-06-11 20:00"))
    path = tmp_path / "programme.json"
    programme.save(path)
    data = json.loads(path.read_text(encoding="utf-8"))
    clash = dict(data["shows"][0])
    clash["start"] = "2027-06-11T20:30"
    data["shows"].append(clash)
    path.write_text(json.dumps(data), encoding="utf-8")
    with pytest.raises(ValueError, match="busy"):
        festival.load_programme(path)


def test_given_data_file(festival, exercise_copy):
    folder = exercise_copy("05_festival")
    programme = festival.load_programme(folder / "programme.json")
    assert len(programme.shows) == 11
    titles = []
    for show in programme.shows_of_day(date(2027, 6, 11)):
        titles.append(show.title)
    assert titles[-1] == "After Hours"


# --- Program -----------------------------------------------------------------------


def run_festival(exercise_copy, *answers):
    folder = exercise_copy("05_festival")
    result = run_python(folder / "festival.py", lines(*answers))
    assert result.returncode == 0, result.stderr
    saved = json.loads((folder / "programme.json").read_text(encoding="utf-8"))
    return result.stdout, saved


def test_program_shows_a_day(exercise_copy):
    output, _ = run_festival(exercise_copy, "day", "2027-06-11", "quit")
    assert_in_order(
        output,
        "Deauville Festival du Rire 2027: 11 shows loaded.",
        "Programme for Friday 11 June:",
        "15:00-17:00 | Le Kiosque | Improv Lab (Inès Moreau)",
        "01:00-02:00 | Le Kiosque | After Hours (Max Pellerin)",
    )


def test_program_adds_and_saves(exercise_copy):
    new_show = ["Brunch", "nora lebrun", "le kiosque", "2027-06-13 11:00", "60", "8"]
    output, saved = run_festival(exercise_copy, "add", *new_show, "quit")
    assert "Saved: 12 shows." in output
    assert len(saved["shows"]) == 12


def test_program_refuses_errors(exercise_copy):
    clash = ["Too Late", "Karim Benali", "Le Kiosque", "2027-06-12 02:15", "30", "5"]
    unknown = ["Show", "Nobody", "Le Kiosque", "2027-06-13 11:00", "60", "8"]
    output, saved = run_festival(
        exercise_copy, "add", *clash, "add", *unknown, "day", "Friday", "quit"
    )
    assert_in_order(
        output,
        "Error: Le Kiosque is busy with After Hours (Sat 01:00-02:00).",
        "Error: Unknown artist: Nobody.",
        "Error:",
    )
    assert len(saved["shows"]) == 11


# --- Your own tests ----------------------------------------------------------------


def test_your_own_tests_pass(exercise_copy):
    folder = exercise_copy("05_festival")
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "pytest",
            "test_festival.py",
            "-q",
            "-p",
            "no:cacheprovider",
        ],
        cwd=folder,
        capture_output=True,
        text=True,
        encoding="utf-8",
        timeout=60,
    )
    assert result.returncode == 0, f"test_festival.py fails:\n{result.stdout}"
    passed = re.search(r"(\d+) passed", result.stdout)
    count = int(passed.group(1)) if passed else 0
    assert count >= 8, f"test_festival.py has {count} tests; write at least 8."
