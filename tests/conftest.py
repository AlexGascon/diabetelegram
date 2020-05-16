import pytest
from unittest import mock

import moto

from diabetelegram.models.expense import Expense
from diabetelegram.models.meal import Meal


pytest_plugins = [
    "tests.fixtures.aws",
    "tests.fixtures.functional"
]

@pytest.fixture(scope="function", autouse=True)
def mock_dynamodb(aws_credentials):
    with moto.mock_dynamodb2() as dynamodb:
        Expense.create_table()
        yield

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


@pytest.fixture
def state(request):
    with mock.patch('diabetelegram.actions.factory.StateManager') as mocked_state_manager:
        instance = mocked_state_manager.return_value

        if current_state_is_mocked(request):
            instance.get.return_value = request.param

        yield instance

def current_state_is_mocked(request):
    return hasattr(request, 'param')

@pytest.fixture
def message(request):
    if custom_message_text_is_specified(request):
        message_text = request.param
    else:
        message_text = 'dummy text'

    return {'text': message_text, 'from': {'id': 'dummy_id'}}

def custom_message_text_is_specified(request):
    return hasattr(request, 'param')

@pytest.fixture
def message_with_csv():
    document = {'file_name': 'data.csv', 'file_id': '12abf34', 'mime_type': 'text/csv', 'file_size': '28440', 'file_unique_id': '6825fac'}
    return {'document': document, 'from': {'id': 'dummy_id'}}

@pytest.fixture
def message_with_pdf():
    document = {'file_name': 'example.pdf', 'file_id': '12abf34', 'mime_type': 'application/pdf', 'file_size': '28440', 'file_unique_id': '1234bde'}
    return {'document': document, 'from': {'id': 'dummy_id'}}