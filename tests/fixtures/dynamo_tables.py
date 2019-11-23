STATE = {
    'TableName': 'diabetelegram-state',
    'AttributeDefinitions': [{
        'AttributeName': 'user_id',
        'AttributeType': 'S'
    }],
    'KeySchema': [{
        'AttributeName': 'user_id',
        'KeyType': 'HASH'
    }]
}
