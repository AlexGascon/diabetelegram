import json
import os

import boto3

from diabetelegram.serializers.injection_serializer import InjectionSerializer


class InjectionSNSClient:
    INSULIN_INJECTED_TOPIC = os.environ['INSULIN_INJECTED_TOPIC_ARN']

    def __init__(self):
        self.sns = boto3.client('sns')

    def insulin_injected(self, injection):
        """Notify that the user has injected insulin to himself"""
        
        sns_payload = {
            'TopicArn': self.INSULIN_INJECTED_TOPIC,
            'Message': json.dumps(InjectionSerializer(injection).to_dict())
        }

        response = self.sns.publish(sns_payload)

        return response['MessageId']
