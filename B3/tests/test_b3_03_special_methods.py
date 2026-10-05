import pytest


@pytest.fixture
def duration(load_exercise):
    return load_exercise("03_special_methods/duration.py")


@pytest.fixture
def artist(load_exercise):
    return load_exercise("03_special_methods/artist.py")


# --- duration ----------------------------------------------------------------------


def test_duration_str(duration):
    assert str(duration.Duration(45)) == "45 min"
    assert str(duration.Duration(95)) == "1h35"
    assert str(duration.Duration(120)) == "2h00"
    assert f"{duration.Duration(61)}" == "1h01"


def test_duration_repr(duration):
    assert repr(duration.Duration(95)) == "Duration(95)"
    assert str([duration.Duration(5)]) == "[Duration(5)]"


def test_duration_eq(duration):
    assert duration.Duration(60) == duration.Duration(60)
    assert duration.Duration(60) != duration.Duration(61)
    assert duration.Duration(60) != 60


def test_duration_sort(duration):
    acts = [duration.Duration(20), duration.Duration(95), duration.Duration(45)]
    assert sorted(acts) == [
        duration.Duration(20),
        duration.Duration(45),
        duration.Duration(95),
    ]
    assert max(acts) == duration.Duration(95)


def test_duration_add(duration):
    """[ext.]"""
    total = duration.Duration(20) + duration.Duration(45)
    assert total == duration.Duration(65)


# --- artist ------------------------------------------------------------------------


def test_artist_is_cleaned(artist):
    nora = artist.Artist("  Nora Lebrun ", " Deadpan stories. ")
    assert nora.name == "Nora Lebrun"
    assert nora.bio == "Deadpan stories."
    assert artist.Artist("Max Pellerin").bio == ""


def test_artist_needs_a_name(artist):
    with pytest.raises(ValueError, match="An artist needs a name."):
        artist.Artist("   ")


def test_slug(artist):
    assert artist.Artist("  Nora  LEBRUN ").slug() == "nora-lebrun"


def test_str_and_repr(artist):
    nora = artist.Artist("Nora Lebrun")
    assert str(nora) == "Nora Lebrun"
    assert repr(nora) == "Artist('Nora Lebrun')"


def test_equality(artist):
    assert artist.Artist("Nora Lebrun") == artist.Artist("nora  LEBRUN", "Other bio")
    assert artist.Artist("Nora Lebrun") != artist.Artist("Max Pellerin")
    assert artist.Artist("Nora Lebrun") != "Nora Lebrun"
    names = [artist.Artist("Max Pellerin"), artist.Artist("Nora Lebrun")]
    assert artist.Artist("NORA LEBRUN") in names


def test_sorting(artist):
    artists = [
        artist.Artist("Sacha Diallo"),
        artist.Artist("max pellerin"),
        artist.Artist("Nora Lebrun"),
    ]
    result = []
    for one in sorted(artists):
        result.append(one.name)
    assert result == ["max pellerin", "Nora Lebrun", "Sacha Diallo"]
