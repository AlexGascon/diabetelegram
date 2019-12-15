from unittest import mock

import pytest

from diabetelegram.services.aws.dynamo import Dynamo
from tests.helpers import load_fixture

@pytest.fixture
def dynamo():
    with mock.patch('boto3.client'):
        dynamo_client = Dynamo()
    dynamo_client._handler.get_item.return_value = load_fixture('dynamodb_get_item_response.json')
    dynamo_client._handler.set_item.return_value = load_fixture('dynamodb_put_item_response.json')
    return dynamo_client


def test_get_propagates_the_call_to_the_dynamo_client(dynamo):
    dynamo.get_state(user_id='1234')

    dynamo._handler.get_item.assert_called_once_with(TableName='diabetelegram-state', Key={'user_id': {'S': '1234'}})

def test_get_with_table_and_key_returns_the_value(dynamo):
    expected_response = {'user_id': '1234', 'state': 'initial'}
    assert dynamo.get_state(user_id='1234') == expected_response

def test_put_state_when_the_operation_was_successful_return_true(dynamo):
    assert dynamo.set_state('final', user_id='4321') == True

def test_put_state_propagates_the_call_to_the_dynamo_client(dynamo):
    dynamo.set_state('final', user_id=4321)

    dynamo._handler.put_item.assert_called_once_with(
        TableName='diabetelegram-state',
        Item={'user_id': {'S': '4321'}, 'state': {'S': 'final'}}
    )

def test_put_state_returns_False_if_there_was_an_exception(dynamo):
    dynamo._handler.put_item.side_effect = ValueError

    assert dynamo.set_state('final', user_id=1234) == False
