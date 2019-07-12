import boto3


class InjectionSNSClient:
    INJECTION_CREATED_TOPIC = 'InjectionCreated'

    def __init__(self):
        self.sns = boto3.resource('sns')

    def create_injection(self, injection):
        """Pushes an event to the CreatedInjection SNS topic"""
        
        sns_payload = self._build_create_injection_message(injection)

        message = sns.topic(self.INJECTION_CREATED_TOPIC).publish(sns_payload)

    def _build_create_injection_message(injection):
        pass