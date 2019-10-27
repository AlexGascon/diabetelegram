import pytest

from diabetelegram.services.aws.dynamo import Dynamo
from tests.helpers import load_fixture

@pytest.fixture
def dynamo(mocker):
    with mocker.patch('boto3.client'):
        dynamo_client = Dynamo()
    dynamo_response = load_fixture('dynamodb_status_response.json')
    dynamo_client._handler.get_item.return_value = dynamo_response
    return dynamo_client


def test_get_propagates_the_call_to_the_dynamo_client(dynamo):
    dynamo.get_status(user_id='1234')

    dynamo._handler.get_item.assert_called_once_with(TableName='diabetelegram-status', Key={'user_id': {'S': '1234'}})

def test_get_with_table_and_key_returns_the_value(dynamo):
    expected_response = {'user_id': '1234', 'status': 'initial'}
    assert dynamo.get_status(user_id='1234') == expected_response
