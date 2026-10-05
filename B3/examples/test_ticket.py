"""Tests of ticket.py.

uv run pytest B3/examples
"""

import pytest
from ticket import ticket_price


def test_child_price():
    assert ticket_price(8) == 8.0


def test_young_adult_pays_reduced():
    assert ticket_price(20) == 12.0


def test_student_pays_reduced():
    assert ticket_price(40, student=True) == 12.0


@pytest.mark.parametrize(
    ("age", "price"), [(11, 8.0), (12, 12.0), (25, 12.0), (26, 22.0)]
)
def test_limits(age, price):
    assert ticket_price(age) == price


def test_negative_age_is_refused():
    with pytest.raises(ValueError, match="Invalid age"):
        ticket_price(-1)
