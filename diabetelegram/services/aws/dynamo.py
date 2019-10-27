import boto3


class Dynamo:
    STATUS_TABLE_NAME = 'diabetelegram-status'

    def __init__(self):
        self._handler = boto3.client('dynamodb')

    def get_status(self, user_id):
        query = self._compose_status_query(user_id=user_id)
        response = self._handler.get_item(TableName=self.STATUS_TABLE_NAME, Key=query)
        return self._parse_status(response)

    def _compose_status_query(self, user_id):
        return {'user_id': {'S': str(user_id)}}

    def _parse_status(self, status_response):
        status = status_response['Item']
        return {'user_id': status['user_id']['S'], 'status': status['value']['S']}

    def set_status(self, status, user_id):
        try:
            item = self._compose_status_item(status=status, user_id=user_id)
            response = self._handler.put_item(TableName=self.STATUS_TABLE_NAME, Item=item)
            return True
        except Exception:
            return False

    def _compose_status_item(self, status, user_id):
        return {'user_id': {'S': str(user_id), }, 'status': {'S': status}}
