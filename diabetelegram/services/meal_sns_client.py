import json
import os

import boto3

from diabetelegram.serializers.meal_serializer import MealSerializer
from diabetelegram.services.aws.sns.base_sns_client import BaseSNSClient


class MealSNSClient(BaseSNSClient):
    def meal_eaten(self, meal):
        """Notify that the user has eat"""
        return self.publish(meal)

    def get_topic_name(self):
        return os.environ['MEAL_EATEN_TOPIC_ARN']

    def build_payload(self, meal):
        return json.dumps(MealSerializer(meal).to_dict())
