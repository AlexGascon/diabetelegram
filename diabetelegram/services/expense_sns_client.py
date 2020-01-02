import json
import os

import boto3

from diabetelegram.serializers.expense_serializer import ExpenseSerializer


class ExpenseSNSClient:
    def __init__(self):
        self.sns = boto3.client('sns')
        self.topic_name = os.environ['MONEY_SPENT_TOPIC_ARN']

    def money_spent(self, expense):
        sns_payload = {
            'TopicArn': self.topic_name,
            'Message': json.dumps(ExpenseSerializer(expense).to_dict())
        }

        response = self.sns.publish(**sns_payload)
        return response['MessageId']
