STATE = {
    'TableName': 'diabetelegram-state',
    'AttributeDefinitions': [{
        'AttributeName': 'user_id',
        'AttributeType': 'S'
    }],
    'KeySchema': [{
        'AttributeName': 'user_id',
        'KeyType': 'HASH'
    }],
    'ProvisionedThroughput': {
        'ReadCapacityUnits': 1,
        'WriteCapacityUnits': 1
    }
}

TABLES = [
    STATE
]
