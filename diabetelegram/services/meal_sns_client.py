import json
import os

import boto3

from diabetelegram.serializers.meal_serializer import MealSerializer


class MealSNSClient:

    def __init__(self):
        self.sns = boto3.client('sns')
        self.MEAL_EATEN_TOPIC = os.environ['MEAL_EATEN_TOPIC_ARN']

    def meal_eaten(self, meal):
        """Notify that the user has eat"""

        sns_payload = {
            'TopicArn': self.MEAL_EATEN_TOPIC,
            'Message': json.dumps(MealSerializer(meal).to_dict())
        }

        response = self.sns.publish(**sns_payload)

        return response['MessageId']

