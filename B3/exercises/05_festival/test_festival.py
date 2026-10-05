"""Tests of festival.py. Run them with: uv run pytest B3/exercises/05_festival"""

from datetime import datetime

from festival import Artist, Show, Venue


def test_artist_name_is_cleaned():
    assert Artist("  Nora Lebrun ").name == "Nora Lebrun"


def test_show_end():
    show = Show(
        "Late Laughs",
        Artist("Nora Lebrun"),
        Venue("Le Kiosque", 120),
        datetime(2027, 6, 11, 23, 30),
        60,
    )
    assert show.end == datetime(2027, 6, 12, 0, 30)


# --- Your tests ----------------------------------------------------------------
