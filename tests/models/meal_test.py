import pytest

from diabetelegram.models.meal import Meal


def test_str_generates_a_readable_text(meal):
    expected = (
        "Meal\n"
        "-----\n"
        "Carbohydrates: 5 portions\n"
        "Food: Hamburguesa Goiko Kevin Bacon con Sweet Potatos\n"
        "Insulin: 2 units\n"
        "Meal type: Lunch\n"
        "Blood Glucose level - Previous: 85 - Posterior: 123\n"
        "Notes: No me termino todas las patatas - como la mitad aprox"
    )

    assert str(meal) == expected
