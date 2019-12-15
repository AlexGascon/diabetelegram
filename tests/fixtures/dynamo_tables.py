EXPENSES = {
    'TableName': 'algasbot-expenses',
    'AttributeDefinitions': [{
        'AttributeName': 'expense_id',
        'AttributeType': 'N'
    }],
    'KeySchema': [{
        'AttributeName': 'expense_id',
        'KeyType': 'HASH'
    }]
}

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

TABLES = [
    EXPENSES,
    STATE
]
