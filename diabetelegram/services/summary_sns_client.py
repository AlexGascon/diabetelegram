import json
import os

import boto3


class SummarySNSClient:
    def __init__(self):
        self.sns = boto3.client('sns')
        self.topic_name = os.environ['SUMMARY_REQUESTED_TOPIC_ARN']

    def summary_requested(self):
        sns_payload = {
            'TopicArn': self.topic_name,
            'Message': json.dumps({})
        }

        response = self.sns.publish(**sns_payload)
        return response['MessageId']
