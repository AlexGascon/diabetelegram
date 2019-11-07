import json
import os

import boto3

from diabetelegram.serializers.injection_serializer import InjectionSerializer


class InjectionSNSClient:
    def __init__(self):
        self.sns = boto3.client('sns')
        self.topic_name = os.environ['INSULIN_INJECTED_TOPIC_ARN']

    def insulin_injected(self, injection):
        """Notify that the user has injected insulin to himself"""
        
        sns_payload = {
            'TopicArn': self.topic_name,
            'Message': json.dumps(InjectionSerializer(injection).to_dict())
        }

        response = self.sns.publish(**sns_payload)

        return response['MessageId']
