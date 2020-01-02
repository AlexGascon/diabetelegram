import os

import boto3

class ExpenseSNSClient:
    def __init__(self):
        self.sns = boto3.client('sns')
        self.topic_name = os.environ['MONEY_SPENT_TOPIC_ARN']

    def money_spent(self, expense):
        pass
