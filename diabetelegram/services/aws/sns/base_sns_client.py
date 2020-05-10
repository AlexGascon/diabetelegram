from abc import ABC, abstractmethod

import boto3


class BaseSNSClient(ABC):
    def __init__(self):
        self.sns = boto3.client('sns')
        self.topic_name = self.get_topic_name()

    def publish(self, subject=None):
        sns_payload = {
            'TopicArn': self.topic_name,
            'Message': self.build_payload(subject)
        }

        response = self.sns.publish(**sns_payload)
        return response['MessageId']

    @abstractmethod
    def build_payload(self, subject):
        pass

    @abstractmethod
    def get_topic_name(self):
        pass