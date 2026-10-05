import json

import pytest

from checks import run_python

# --- line_stats --------------------------------------------------------------------


@pytest.fixture
def line_stats(load_exercise):
    return load_exercise("03_files/line_stats.py")


def test_file_stats(line_stats, tmp_path):
    path = tmp_path / "text.txt"
    path.write_text("Ha ha.\nThe longest line of all.\n\nÉté.\n", encoding="utf-8")
    assert line_stats.file_stats(path) == {
        "lines": 4,
        "words": 8,
        "longest": "The longest line of all.",
    }


def test_file_stats_missing_file(line_stats, tmp_path):
    with pytest.raises(FileNotFoundError):
        line_stats.file_stats(tmp_path / "missing.txt")


def test_number_lines(line_stats, tmp_path):
    source = tmp_path / "source.txt"
    source.write_text("Théâtre\n\nKiosque\n", encoding="utf-8")
    target = tmp_path / "numbered.txt"
    line_stats.number_lines(source, target)
    assert target.read_text(encoding="utf-8") == "1. Théâtre\n2. \n3. Kiosque\n"


def test_line_stats_main(exercise_copy):
    folder = exercise_copy("03_files")
    result = run_python(folder / "line_stats.py")
    assert result.returncode == 0, result.stderr
    assert "Lines: 6" in result.stdout
    assert "Words: 41" in result.stdout
    assert (
        "Longest line: Four venues, four days, and a sea breeze between two shows."
        in result.stdout
    )


# --- shows_csv ---------------------------------------------------------------------


@pytest.fixture
def shows_csv(load_exercise):
    return load_exercise("03_files/shows_csv.py")


CSV_TEXT = (
    "title,artist,venue,day,start,duration,price\n"
    "Nothing Serious,Nora Lebrun,Théâtre des Planches,2027-06-10,21:00,75,22.0\n"
    "Open Mic Night,Max Pellerin,Le Kiosque,2027-06-10,22:30,90,0\n"
)

SHOWS = [
    {
        "title": "Nothing Serious",
        "artist": "Nora Lebrun",
        "venue": "Théâtre des Planches",
        "day": "2027-06-10",
        "start": "21:00",
        "duration": 75,
        "price": 22.0,
    },
    {
        "title": "Open Mic Night",
        "artist": "Max Pellerin",
        "venue": "Le Kiosque",
        "day": "2027-06-10",
        "start": "22:30",
        "duration": 90,
        "price": 0.0,
    },
]


def test_load_csv_converts_numbers(shows_csv, tmp_path):
    path = tmp_path / "programme.csv"
    path.write_text(CSV_TEXT, encoding="utf-8")
    shows = shows_csv.load_csv(path)
    assert shows == SHOWS
    assert isinstance(shows[0]["duration"], int)
    assert isinstance(shows[1]["price"], float)


def test_json_round_trip(shows_csv, tmp_path):
    path = tmp_path / "programme.json"
    shows_csv.save_json(SHOWS, path)
    text = path.read_text(encoding="utf-8")
    assert "Théâtre des Planches" in text, "Use ensure_ascii=False."
    assert "\n  " in text, "Use indent=2."
    assert shows_csv.load_json(path) == SHOWS


def test_shows_csv_main(exercise_copy):
    folder = exercise_copy("03_files")
    result = run_python(folder / "shows_csv.py")
    assert result.returncode == 0, result.stderr
    assert "10 shows written to programme.json" in result.stdout
    shows = json.loads((folder / "programme.json").read_text(encoding="utf-8"))
    assert len(shows) == 10
    assert shows[0]["title"] == "Opening Gala"
    assert shows[-1]["duration"] == 130


def test_save_csv(shows_csv, tmp_path):
    """[ext.]"""
    path = tmp_path / "copy.csv"
    shows_csv.save_csv(SHOWS, path)
    assert path.read_text(encoding="utf-8").splitlines()[0] == (
        "title,artist,venue,day,start,duration,price"
    )
    assert shows_csv.load_csv(path) == SHOWS
