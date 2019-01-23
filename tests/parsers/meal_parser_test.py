import pytest

from diabetelegram.parsers.meal_parser import MealParser


def test_to_meal(meal_data):
    meal = MealParser(meal_data).to_meal()

    assert meal.carbohydrates_portions == 5
    assert meal.food == "Hamburguesa Goiko Kevin Bacon con Sweet Potatos"
    assert meal.insulin_units == 2
    assert meal.meal_type == "lunch"
    assert meal.notes == "No me termino todas las patatas - como la mitad aprox"
    assert meal.pre_blood_glucose == 85
    assert meal.post_blood_glucose == 123

def test_to_meal_with_incomplete_message(incomplete_meal_data):
    incomplete_meal = MealParser(incomplete_meal_data).to_meal()

    assert incomplete_meal.food == "café y tostadas con jamón"
    assert incomplete_meal.insulin_units == 1
    assert incomplete_meal.meal_type == "breakfast"
    assert incomplete_meal.notes == "Desayuno en el bar de la esquina"
    assert incomplete_meal.pre_blood_glucose == 92
    assert incomplete_meal.post_blood_glucose == None
    assert incomplete_meal.carbohydrates_portions == None
