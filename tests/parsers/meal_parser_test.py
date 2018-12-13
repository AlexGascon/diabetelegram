import pytest

from diabetelegram.parsers.meal_parser import MealParser
from tests.fixtures.messages import meal_message, incomplete_meal_message

# Fixtures

@pytest.fixture
def parser():
    return MealParser("pre: 85, post: 123, tipo: lunch, insulina: 2, raciones: 5, comida: Hamburguesa Goiko Kevin Bacon con Sweet Potatos - Solo un poco sin terminarlas todas")

@pytest.fixture
def incomplete_parser():
    return MealParser("pre: 92, tipo: breakfast, insulina: 1, comida: café y tostadas con jamón")


# Test cases

def test_to_meal(parser):
    meal = parser.to_meal()

    assert meal.carbohydrates_portions == 5
    assert meal.food == "Hamburguesa Goiko Kevin Bacon con Sweet Potatos - Solo un poco sin terminarlas todas"
    assert meal.insulin_units == 2
    assert meal.meal_type == "lunch"
    assert meal.pre_blood_glucose == 85
    assert meal.post_blood_glucose == 123

def test_to_meal_with_incomplete_message(incomplete_parser):
    incomplete_meal = incomplete_parser.to_meal()

    assert incomplete_meal.food == "café y tostadas con jamón"
    assert incomplete_meal.insulin_units == 1
    assert incomplete_meal.meal_type == "breakfast"
    assert incomplete_meal.pre_blood_glucose == 92
    assert incomplete_meal.post_blood_glucose == None
    assert incomplete_meal.carbohydrates_portions == None
