import pytest

from diabetelegram.serializers.meal_serializer import MealSerializer


def test_serializes_meal(meal):
    serialized_meal = MealSerializer(meal).to_dict()

    assert serialized_meal["carbohydrates_portions"] == 5
    assert serialized_meal["food"] == "Hamburguesa Goiko Kevin Bacon con Sweet Potatos"
    assert serialized_meal["insulin_units"] == 2
    assert serialized_meal["meal_type"] == "lunch"
    assert serialized_meal["notes"] == "No me termino todas las patatas - como la mitad aprox"
    assert serialized_meal["pre_blood_glucose"] == 85
    assert serialized_meal["post_blood_glucose"] == 123

def test_serializes_incomplete_meal(incomplete_meal):
    serialized_meal = MealSerializer(incomplete_meal).to_dict()

    assert serialized_meal["food"] == "café y tostadas con jamón"
    assert serialized_meal["insulin_units"] == 1
    assert serialized_meal["meal_type"] == "breakfast"
    assert serialized_meal["notes"] == "Desayuno en el bar de la esquina"
    assert serialized_meal["pre_blood_glucose"] == 92
