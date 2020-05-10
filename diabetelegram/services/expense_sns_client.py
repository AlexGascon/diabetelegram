import json
import os

import boto3

from diabetelegram.serializers.expense_serializer import ExpenseSerializer
from diabetelegram.services.aws.sns.base_sns_client import BaseSNSClient


class ExpenseSNSClient(BaseSNSClient):
    def money_spent(self, expense):
        return self.publish(expense)

    def build_payload(self, expense):
        return json.dumps(ExpenseSerializer(expense).to_dict())

    def get_topic_name(self):
        return os.environ['MONEY_SPENT_TOPIC_ARN']