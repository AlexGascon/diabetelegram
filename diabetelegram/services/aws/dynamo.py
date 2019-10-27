import boto3


class Dynamo:
    STATUS_TABLE_NAME = 'diabetelegram-status'

    def __init__(self):
        self._handler = boto3.client('dynamodb')

    def get_status(self, user_id):
        query = self._compose_status_query(user_id='1234')
        response = self._handler.get_item(TableName=self.STATUS_TABLE_NAME, Key=query)
        return self._parse_status(response)

    def _compose_status_query(self, user_id):
        return {'user_id': {'S': str(user_id)}}

    def _parse_status(self, status_response):
        status = status_response['Item']
        return {'user_id': status['user_id']['S'], 'status': status['value']['S']}