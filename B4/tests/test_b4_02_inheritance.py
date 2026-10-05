import inspect
from datetime import date, datetime

import pytest


@pytest.fixture
def shapes(load_exercise):
    return load_exercise("02_inheritance/shapes.py")


@pytest.fixture
def perf(load_exercise):
    return load_exercise("02_inheritance/performances.py")


@pytest.fixture
def mixins(load_exercise):
    return load_exercise("02_inheritance/mixins.py")


# --- shapes ------------------------------------------------------------------------


def test_shapes(shapes):
    assert shapes.Rectangle(4, 3).area() == 12
    assert shapes.Square(2).area() == 4
    assert shapes.Circle(1).area() == pytest.approx(3.14159)
    assert shapes.Shape("point").area() == 0.0


def test_describe_is_inherited(shapes):
    assert shapes.Rectangle(4, 3).describe() == "rectangle: 12.00"
    assert shapes.Square(2).describe() == "square: 4.00"
    assert shapes.Circle(1).describe() == "circle: 3.14"
    for subclass in [shapes.Rectangle, shapes.Square, shapes.Circle]:
        assert "describe" not in vars(subclass), "describe is written once, in Shape."


def test_hierarchy(shapes):
    assert issubclass(shapes.Square, shapes.Rectangle)
    assert issubclass(shapes.Rectangle, shapes.Shape)
    assert issubclass(shapes.Circle, shapes.Shape)
    square = shapes.Square(3)
    assert (square.width, square.height) == (3, 3)


def test_total_area(shapes):
    total = shapes.total_area([shapes.Rectangle(4, 3), shapes.Square(2)])
    assert total == 16
    assert shapes.total_area([]) == 0


# --- performances ------------------------------------------------------------------


def at(text):
    return datetime.fromisoformat(text)


@pytest.fixture
def programme(perf):
    return [
        perf.SoloShow(
            "Late Laughs", "Le Kiosque", at("2027-06-12 00:30"), 60, "Nora Lebrun", 16
        ),
        perf.Lineup(
            "Opening Gala",
            "Grand Casino",
            at("2027-06-10 20:30"),
            120,
            "Paul Kerbrat",
            ["Nora Lebrun", "Max Pellerin"],
        ),
        perf.Workshop(
            "Improv Lab", "Le Kiosque", at("2027-06-11 15:00"), 120, "Inès Moreau", 2
        ),
    ]


def test_hierarchy_of_performances(perf):
    for subclass in [perf.SoloShow, perf.Lineup, perf.Workshop]:
        assert issubclass(subclass, perf.Performance)
        assert "end" not in vars(subclass), "end is written once, in Performance."
        assert "__str__" not in vars(subclass)
    assert (perf.SoloShow.kind, perf.Lineup.kind, perf.Workshop.kind) == (
        "solo",
        "lineup",
        "workshop",
    )


def test_common_part(programme):
    late = programme[0]
    assert late.end == at("2027-06-12 01:30")
    assert late.festival_day == date(2027, 6, 11)


def test_common_checks(perf):
    with pytest.raises(ValueError, match="A performance needs a title."):
        perf.SoloShow(" ", "Le Kiosque", at("2027-06-11 20:00"), 60, "Nora")
    with pytest.raises(ValueError, match="Invalid duration"):
        perf.Workshop("Class", "Le Kiosque", at("2027-06-11 10:00"), 0, "Inès", 5)


def test_uses_super(perf):
    for subclass in [perf.SoloShow, perf.Lineup, perf.Workshop]:
        assert "super().__init__" in inspect.getsource(subclass.__init__)


def test_artists_and_summary(programme):
    late, gala, improv = programme
    assert late.artists() == ["Nora Lebrun"]
    assert gala.artists() == ["Paul Kerbrat", "Nora Lebrun", "Max Pellerin"]
    assert improv.artists() == ["Inès Moreau"]
    assert late.summary() == "Nora Lebrun, 16+"
    assert gala.summary() == "hosted by Paul Kerbrat, with Nora Lebrun, Max Pellerin"
    assert improv.summary() == "with Inès Moreau, 0/2 places taken"


def test_str_uses_summary(programme):
    assert (
        str(programme[0]) == "Sat 00:30 | Le Kiosque | Late Laughs (Nora Lebrun, 16+)"
    )
    assert str(programme[1]).startswith(
        "Thu 20:30 | Grand Casino | Opening Gala (hosted"
    )


def test_base_class_has_no_artists(perf):
    base = perf.Performance("?", "Le Kiosque", at("2027-06-11 20:00"), 60)
    with pytest.raises(NotImplementedError):
        base.artists()


def test_lineup_needs_two_acts(perf):
    with pytest.raises(ValueError, match="at least two acts"):
        perf.Lineup(
            "Gala", "Grand Casino", at("2027-06-10 20:30"), 90, "Paul", ["Nora"]
        )


def test_workshop_registration(programme):
    improv = programme[2]
    improv.register("Lou")
    with pytest.raises(ValueError, match="Lou is already registered."):
        improv.register("Lou")
    improv.register("Yanis")
    assert improv.places_left() == 0
    with pytest.raises(ValueError, match="Improv Lab is full."):
        improv.register("Camille")
    improv.participants.append("Sneaky")
    assert improv.participants == ["Lou", "Yanis"]
    assert improv.summary() == "with Inès Moreau, 2/2 places taken"


def test_performances_of(perf, programme):
    assert perf.performances_of(programme, "Nora Lebrun") == [
        "Late Laughs",
        "Opening Gala",
    ]
    assert perf.performances_of(programme, "Inès Moreau") == ["Improv Lab"]
    assert perf.performances_of(programme, "Nobody") == []


# --- mixins [ext.] -----------------------------------------------------------------


def test_mixins(mixins):
    ticket = mixins.Ticket("full", 22.0, "X7Q2")
    assert ticket.to_dict() == {"category": "full", "price": 22.0}
    assert repr(ticket) == "Ticket(category='full', price=22.0)"
    assert issubclass(mixins.Ticket, mixins.ToDictMixin)
    assert issubclass(mixins.Ticket, mixins.ReprMixin)


def test_mro(mixins):
    assert mixins.Host().describe() == "announcer"
    assert mixins.mro_names(mixins.Host) == ["Host", "Announcer", "Performer", "object"]
