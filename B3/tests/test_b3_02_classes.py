import pytest


@pytest.fixture
def rectangle(load_exercise):
    return load_exercise("02_classes/rectangle.py")


@pytest.fixture
def counter(load_exercise):
    return load_exercise("02_classes/counter.py")


@pytest.fixture
def venue(load_exercise):
    return load_exercise("02_classes/venue.py")


# --- rectangle ---------------------------------------------------------------------


def test_rectangle(rectangle):
    stage = rectangle.Rectangle(12, 8)
    assert stage.width == 12
    assert stage.height == 8
    assert stage.area() == 96
    assert stage.perimeter() == 40
    assert not stage.is_square()
    assert rectangle.Rectangle(5, 5).is_square()


def test_rectangle_scale(rectangle):
    stage = rectangle.Rectangle(12, 8)
    result = stage.scale(0.5)
    assert result is None, "scale changes the rectangle, it returns nothing."
    assert (stage.width, stage.height) == (6, 4)


def test_rectangles_are_independent(rectangle):
    first = rectangle.Rectangle(1, 2)
    second = rectangle.Rectangle(3, 4)
    first.scale(10)
    assert (second.width, second.height) == (3, 4)


# --- counter -----------------------------------------------------------------------


def test_counter(counter):
    door = counter.Counter("Door A")
    assert door.name == "Door A"
    assert door.value == 0
    door.increment()
    door.increment(3)
    assert door.value == 4
    door.reset()
    assert door.value == 0


def test_counter_class_attribute(counter):
    before = counter.Counter.created
    door_a = counter.Counter("Door A")
    counter.Counter("Door B")
    assert counter.Counter.created == before + 2
    assert door_a.created == before + 2, "created belongs to the class."
    assert "created" not in vars(door_a), "created belongs to the class."


# --- venue -------------------------------------------------------------------------


def test_new_venue(venue):
    kiosque = venue.Venue("Le Kiosque", 120)
    assert kiosque.name == "Le Kiosque"
    assert kiosque.capacity == 120
    assert kiosque.sold == 0
    assert kiosque.seats_left() == 120
    assert not kiosque.is_full()
    assert kiosque.occupancy() == 0.0


def test_venue_needs_seats(venue):
    with pytest.raises(ValueError, match="at least one seat"):
        venue.Venue("Nowhere", 0)


def test_book_and_cancel(venue):
    kiosque = venue.Venue("Le Kiosque", 120)
    kiosque.book(4)
    kiosque.book(2)
    kiosque.cancel(1)
    assert kiosque.sold == 5
    assert kiosque.seats_left() == 115
    assert kiosque.occupancy() == pytest.approx(4.1666, 0.001)


def test_booking_limits(venue):
    cabane = venue.Venue("La Cabane", 12)
    assert venue.Venue.MAX_PER_BOOKING == 10
    with pytest.raises(ValueError, match="A booking is 1 to 10 seats, got 11."):
        cabane.book(11)
    with pytest.raises(ValueError, match="got 0"):
        cabane.book(0)
    cabane.book(10)
    with pytest.raises(ValueError, match="Not enough seats: 2 left."):
        cabane.book(3)
    cabane.book(2)
    assert cabane.is_full()
    with pytest.raises(ValueError, match="Only 12 seats sold."):
        cabane.cancel(13)
    assert cabane.sold == 12


def test_max_per_booking_is_shared(venue):
    kiosque = venue.Venue("Le Kiosque", 120)
    assert kiosque.MAX_PER_BOOKING == 10
    assert "MAX_PER_BOOKING" not in vars(kiosque)
