import json

import pytest

from checks import assert_in_order, lines, run_python


@pytest.fixture
def festival(load_exercise):
    return load_exercise("05_festival/festival.py")


def make_show(
    title="Test Show",
    artist="Nora Lebrun",
    venue="Le Kiosque",
    day="2027-06-10",
    start="18:00",
    duration=60,
    price=10.0,
) -> dict:
    return {
        "title": title,
        "artist": artist,
        "venue": venue,
        "day": day,
        "start": start,
        "duration": duration,
        "price": price,
    }


# --- Files -------------------------------------------------------------------------


def test_save_and_load(festival, tmp_path):
    path = tmp_path / "programme.json"
    shows = [make_show(venue="Théâtre des Planches")]
    festival.save_programme(shows, path)
    assert "Théâtre des Planches" in path.read_text(encoding="utf-8")
    assert festival.load_programme(path) == shows


def test_load_missing_file(festival, tmp_path):
    assert festival.load_programme(tmp_path / "nothing.json") == []


def test_load_broken_file(festival, tmp_path):
    path = tmp_path / "programme.json"
    path.write_text('[{"title": "Gala",', encoding="utf-8")
    with pytest.raises(ValueError, match="programme.json is not valid JSON."):
        festival.load_programme(path)


# --- Times -------------------------------------------------------------------------


def test_to_minutes(festival):
    assert festival.to_minutes("20:30") == 1230
    for wrong in ["2030", "24:00", "20:60", "ab:cd", ""]:
        with pytest.raises(ValueError, match="Invalid time"):
            festival.to_minutes(wrong)


def test_to_clock_and_end_time(festival):
    assert festival.to_clock(1230) == "20:30"
    assert festival.to_clock(1500) == "01:00"
    assert festival.end_time(make_show(start="23:30", duration=90)) == "01:00"


# --- Rules -------------------------------------------------------------------------


def test_check_show(festival):
    festival.check_show(make_show())
    with pytest.raises(ValueError, match="Missing field: price."):
        show = make_show()
        del show["price"]
        festival.check_show(show)
    with pytest.raises(ValueError, match="Empty field: artist."):
        festival.check_show(make_show(artist=" "))
    with pytest.raises(ValueError, match="Invalid duration"):
        festival.check_show(make_show(duration=400))
    with pytest.raises(ValueError, match="Invalid price"):
        festival.check_show(make_show(price=-1.0))


def test_too_close(festival):
    first = make_show(start="20:00", duration=60)
    assert festival.too_close(first, make_show(start="20:30"), 0)
    assert not festival.too_close(first, make_show(start="21:00"), 0)
    assert festival.too_close(first, make_show(start="21:29"), 30)
    assert not festival.too_close(first, make_show(start="21:30"), 30)
    assert not festival.too_close(first, make_show(day="2027-06-11"), 30)


def test_find_clash_venue(festival):
    shows = [make_show(title="Late Laughs", start="20:00", duration=60)]
    new_show = make_show(artist="Max Pellerin", start="21:15")
    assert festival.find_clash(shows, new_show) == (
        "Le Kiosque is busy with Late Laughs (20:00-21:00)."
    )
    new_show["start"] = "21:30"
    assert festival.find_clash(shows, new_show) is None


def test_find_clash_artist(festival):
    shows = [make_show(title="Tall Tales", venue="Grand Casino", start="20:00")]
    new_show = make_show(venue="Le Kiosque", start="21:10")
    assert festival.find_clash(shows, new_show) == (
        "Nora Lebrun is already on stage in Tall Tales (20:00-21:00)."
    )
    other_artist = make_show(artist="Max Pellerin", start="21:10")
    assert festival.find_clash(shows, other_artist) is None


def test_add_show(festival):
    shows = [make_show(title="First", start="20:00")]
    festival.add_show(shows, make_show(title="Second", start="22:00"))
    assert len(shows) == 2

    with pytest.raises(ValueError, match="busy with Second"):
        festival.add_show(shows, make_show(artist="Max Pellerin", start="22:30"))
    with pytest.raises(ValueError, match="Invalid time"):
        festival.add_show(shows, make_show(start="25:00"))
    assert len(shows) == 2


# --- Programme ---------------------------------------------------------------------


def test_shows_of_day(festival):
    shows = [
        make_show(title="Late", start="23:30"),
        make_show(title="Other day", day="2027-06-11"),
        make_show(title="Early", start="09:00"),
        make_show(title="Evening", start="20:00"),
    ]
    titles = []
    for show in festival.shows_of_day(shows, "2027-06-10"):
        titles.append(show["title"])
    assert titles == ["Early", "Evening", "Late"]
    assert festival.shows_of_day(shows, "2027-06-13") == []


# --- Program -----------------------------------------------------------------------


def run_festival(exercise_copy, *answers):
    folder = exercise_copy("05_festival")
    result = run_python(folder / "festival.py", lines(*answers))
    assert result.returncode == 0, result.stderr
    saved = json.loads((folder / "programme.json").read_text(encoding="utf-8"))
    return result.stdout, saved


def test_program_shows_a_day(exercise_copy):
    output, saved = run_festival(exercise_copy, "day", "2027-06-11", "quit")
    assert_in_order(
        output,
        "10 shows loaded.",
        "Programme for 2027-06-11:",
        "15:00-17:00 | Le Kiosque | Improv Lab (Inès Moreau)",
        "23:30-00:30 | Le Kiosque | Late Laughs (Nora Lebrun)",
    )
    assert len(saved) == 10


def test_program_adds_and_saves(exercise_copy):
    new_show = [
        "Brunch",
        "Max Pellerin",
        "Le Kiosque",
        "2027-06-12",
        "11:00",
        "60",
        "8",
    ]
    output, saved = run_festival(exercise_copy, "add", *new_show, "quit")
    assert "Saved: 11 shows." in output
    assert len(saved) == 11
    assert saved[-1]["duration"] == 60
    assert saved[-1]["price"] == 8.0


def test_program_refuses_a_clash(exercise_copy):
    clash = [
        "Too Soon",
        "Max Pellerin",
        "Grand Casino",
        "2027-06-10",
        "22:45",
        "60",
        "10",
    ]
    output, saved = run_festival(exercise_copy, "add", *clash, "quit")
    assert "Error: Grand Casino is busy with Opening Gala (20:30-22:30)." in output
    assert len(saved) == 10


def test_program_refuses_a_wrong_number(exercise_copy):
    wrong = ["Show", "Max Pellerin", "Le Kiosque", "2027-06-12", "11:00", "an hour"]
    output, saved = run_festival(exercise_copy, "add", *wrong, "hello", "quit")
    assert_in_order(output, "Error:", "Unknown command.")
    assert len(saved) == 10
