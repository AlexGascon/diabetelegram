import pytest

from diabetelegram.services.state_manager import StateManager


@pytest.fixture
def state_manager(dynamo):
    state_manager = StateManager(user_id=1234)
    return state_manager

@pytest.fixture
def dynamo(mocker):
    dynamo_mock = mocker.patch('diabetelegram.services.state_manager.Dynamo')
    dynamo_instance = dynamo_mock.return_value
    dynamo_instance.get_state.return_value = {'user_id': '1234', 'state': 'initial'}
    dynamo_instance.set_state.return_value = True
    return dynamo_instance

def test_state_manager_get_retrieves_the_state(state_manager):
    assert 'initial' == state_manager.get()

def test_state_manager_get_calls_dynamo_correctly(state_manager):
    state_manager.get()

    state_manager._dynamo.get_state.assert_called_with(user_id=1234)

def test_state_manager_set_returns_true_if_the_operation_was_correct(state_manager):
    assert True == state_manager.set('new_state')

def test_state_manager_set_calls_dynamo_correctly(state_manager):
    state_manager.set('final')

    state_manager._dynamo.set_state.assert_called_with('final', user_id=1234)
