import pytest

from diabetelegram.services.status_manager import StatusManager


@pytest.fixture
def status_manager(dynamo):
    status_manager = StatusManager(user_id=1234)
    status_manager._dynamo = dynamo
    return status_manager

@pytest.fixture
def dynamo(mocker):
    dynamo_client = mocker.Mock()
    dynamo_client.get_status.return_value = {'user_id': '1234', 'status': 'initial'}
    dynamo_client.set_status.return_value = True
    return dynamo_client

def test_status_manager_get_retrieves_the_status(status_manager):
    assert 'initial' == status_manager.get()

def test_status_manager_get_calls_dynamo_correctly(status_manager):
    status_manager.get()

    status_manager._dynamo.get_status.assert_called_with(user_id=1234)

def test_status_manager_set_returns_true_if_the_operation_was_correct(status_manager):
    assert True == status_manager.set('new_status')

def test_status_manager_set_calls_dynamo_correctly(status_manager):
    status_manager.set('final')

    status_manager._dynamo.set_status.assert_called_with('final', user_id=1234)
