import pytest

from diabetelegram.services.aws.dynamo import Dynamo
from diabetelegram.services.state_manager import StateManager


@pytest.fixture
def functional_dynamo(mock_dynamodb):
    dynamo = Dynamo()
    dynamo._handler = mock_dynamodb
    return dynamo

@pytest.fixture
def functional_state_manager(functional_dynamo):
    state_manager = StateManager(user_id=42)
    state_manager._dynamo = functional_dynamo
    return state_manager


