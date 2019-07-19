import json
import os

import boto3

from diabetelegram.serializers.injection_serializer import InjectionSerializer


class InjectionSNSClient:
    INJECTION_CREATED_TOPIC = os.environ['INJECTION_CREATED_TOPIC_ARN']

    def __init__(self):
        self.sns = boto3.client('sns')

    def create_injection(self, injection):
        """Pushes an event to the CreatedInjection SNS topic"""
        
        sns_payload = {
            'TopicArn': self.INJECTION_CREATED_TOPIC,
            'Message': json.dumps(InjectionSerializer(injection).to_dict())
        }

        response = sns.publish(sns_payload)

        return response['MessageId']
