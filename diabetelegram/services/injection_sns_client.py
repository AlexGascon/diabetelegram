import json
import os

import boto3

from diabetelegram.serializers.injection_serializer import InjectionSerializer
from diabetelegram.services.aws.sns.base_sns_client import BaseSNSClient


class InjectionSNSClient(BaseSNSClient):
    def build_payload(self, injection):
        return json.dumps(InjectionSerializer(injection).to_dict()) 

    def get_topic_name(self):
        return os.environ['INSULIN_INJECTED_TOPIC_ARN']

    def insulin_injected(self, injection):
        return self.publish(injection)
