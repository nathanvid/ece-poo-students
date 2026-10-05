import pytest

from checks import assert_in_order, lines


@pytest.mark.parametrize(
    ("number", "parity", "sign"),
    [
        ("7", "odd", "positive"),
        ("8", "even", "positive"),
        ("0", "even", "zero"),
        ("-3", "odd", "negative"),
        ("-4", "even", "negative"),
    ],
)
def test_even_odd(run_script, number, parity, sign):
    output = run_script("02_conditions/even_odd.py", lines(number))
    assert_in_order(output, f"{number} is {parity}.", f"{number} is {sign}.")


@pytest.mark.parametrize(
    ("year", "is_leap"),
    [("2024", True), ("2023", False), ("1900", False), ("2000", True), ("2100", False)],
)
def test_leap_year(run_script, year, is_leap):
    output = run_script("02_conditions/leap_year.py", lines(year))
    if is_leap:
        assert f"{year} is a leap year." in output
    else:
        assert f"{year} is not a leap year." in output


@pytest.mark.parametrize(
    ("age", "student", "price"),
    [
        ("5", "n", "8.00"),
        ("11", "y", "8.00"),
        ("12", "n", "12.00"),
        ("25", "n", "12.00"),
        ("26", "n", "22.00"),
        ("40", "y", "12.00"),
        ("40", "  Y ", "12.00"),
        ("64", "n", "22.00"),
        ("65", "n", "15.00"),
        ("70", "y", "12.00"),
        ("0", "n", "8.00"),
        ("120", "n", "15.00"),
    ],
)
def test_ticket_price(run_script, age, student, price):
    output = run_script("02_conditions/ticket_price.py", lines(age, student))
    assert f"Ticket price: {price} EUR" in output


@pytest.mark.parametrize("age", ["-1", "121", "150"])
def test_ticket_price_invalid_age(run_script, age):
    output = run_script("02_conditions/ticket_price.py", lines(age))
    assert "Invalid age." in output
    assert "Student?" not in output
    assert "Ticket price" not in output
