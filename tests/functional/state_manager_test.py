import pytest

from diabetelegram.services.state_manager import StateManager
from tests.fixtures.dynamo_tables import STATE

@pytest.fixture
def state_manager(mock_dynamodb):
    state_manager = StateManager(user_id=42)
    state_manager._dynamo._handler.create_table(**STATE)
    return state_manager


def test_state_manager_gets_the_state_we_just_set(state_manager):
    state_manager.set('mock_state')
    assert state_manager.get() == 'mock_state'

    state_manager.set('another_mock_state')
    assert state_manager.get() == 'another_mock_state'
