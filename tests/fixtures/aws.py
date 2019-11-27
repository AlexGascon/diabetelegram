import os

import boto3
import pytest
from moto import mock_dynamodb2

from tests.fixtures.dynamo_tables import TABLES


@pytest.fixture(scope='function')
def aws_credentials():
    """Mocked AWS Credentials for moto."""
    os.environ['AWS_ACCESS_KEY_ID'] = 'testing'
    os.environ['AWS_SECRET_ACCESS_KEY'] = 'testing'
    os.environ['AWS_SECURITY_TOKEN'] = 'testing'
    os.environ['AWS_SESSION_TOKEN'] = 'testing'

@pytest.fixture(scope='function')
def mock_dynamodb(aws_credentials):
    """Mocked DynamoDB client"""
    with mock_dynamodb2():
        dynamodb = boto3.client('dynamodb')
        create_tables(dynamodb)
        yield dynamodb

def create_tables(dynamodb):
    for table in TABLES:
        dynamodb.create_table(**table)