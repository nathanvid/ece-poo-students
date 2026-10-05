import pytest

from checks import assert_in_order, lines


@pytest.mark.parametrize(
    ("width", "height", "area", "perimeter"),
    [
        ("5", "2.5", "12.50", "15.00"),
        ("3", "4", "12.00", "14.00"),
        ("0.1", "0.2", "0.02", "0.60"),
    ],
)
def test_rectangle(run_script, width, height, area, perimeter):
    output = run_script("01_variables_io/rectangle.py", lines(width, height))
    assert_in_order(output, f"Area: {area}", f"Perimeter: {perimeter}")


@pytest.mark.parametrize(
    ("seconds", "expected"),
    [
        ("3725", "1 h 2 min 5 s"),
        ("59", "0 h 0 min 59 s"),
        ("3600", "1 h 0 min 0 s"),
        ("90061", "25 h 1 min 1 s"),
    ],
)
def test_seconds(run_script, seconds, expected):
    assert expected in run_script("01_variables_io/seconds.py", lines(seconds))


@pytest.mark.parametrize(
    ("full", "reduced", "count", "subtotal", "fees", "total"),
    [
        ("2", "1", "3", "56.00", "4.50", "60.50"),
        ("0", "0", "0", "0.00", "0.00", "0.00"),
        ("0", "4", "4", "48.00", "6.00", "54.00"),
        ("1", "0", "1", "22.00", "1.50", "23.50"),
    ],
)
def test_receipt(run_script, full, reduced, count, subtotal, fees, total):
    output = run_script("01_variables_io/receipt.py", lines(full, reduced))
    assert_in_order(
        output,
        f"Tickets: {count}",
        f"Subtotal: {subtotal} EUR",
        f"Booking fees: {fees} EUR",
        f"Total: {total} EUR",
    )
