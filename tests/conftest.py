import pytest

from diabetelegram.models.meal import Meal


# Data
@pytest.fixture
def meal_data():
    return "pre: 85, post: 123, tipo: lunch, insulina: 2, raciones: 5, comida: Hamburguesa Goiko Kevin Bacon con Sweet Potatos, notas: No me termino todas las patatas - como la mitad aprox"

@pytest.fixture
def incomplete_meal_data():
    return "pre: 92, tipo: breakfast, insulina: 1, comida: café y tostadas con jamón, notas: Desayuno en el bar de la esquina"

# Meals
@pytest.fixture
def meal():
    return Meal(
        carbohydrates_portions=5,
        food="Hamburguesa Goiko Kevin Bacon con Sweet Potatos",
        insulin_units=2,
        meal_type="lunch",
        notes="No me termino todas las patatas - como la mitad aprox",
        pre_blood_glucose=85,
        post_blood_glucose=123
    )

@pytest.fixture
def incomplete_meal():
    return Meal(
        food="café y tostadas con jamón",
        insulin_units=1,
        meal_type="breakfast",
        notes="Desayuno en el bar de la esquina",
        pre_blood_glucose=92
    )

