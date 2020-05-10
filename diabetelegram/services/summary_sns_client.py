import json
import os

import boto3

from diabetelegram.services.aws.sns.base_sns_client import BaseSNSClient


class SummarySNSClient(BaseSNSClient):
    def summary_requested(self):
        return self.publish()

    def get_topic_name(self):
        return os.environ['SUMMARY_REQUESTED_TOPIC_ARN']

    def build_payload(self, _subject):
        return json.dumps({})
