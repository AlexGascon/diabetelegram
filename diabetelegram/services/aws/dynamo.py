import boto3


class Dynamo:
    STATE_TABLE_NAME = 'diabetelegram-state'

    def __init__(self):
        self._handler = boto3.client('dynamodb')

    def get_state(self, user_id):
        query = self._compose_state_query(user_id=user_id)
        response = self._handler.get_item(TableName=self.STATE_TABLE_NAME, Key=query)
        return self._parse_state(response)

    def _compose_state_query(self, user_id):
        return {'user_id': {'S': str(user_id)}}

    def _parse_state(self, state_response):
        state = state_response['Item']
        return {'user_id': state['user_id']['S'], 'state': state['value']['S']}

    def set_state(self, state, user_id):
        try:
            item = self._compose_state_item(state=state, user_id=user_id)
            response = self._handler.put_item(TableName=self.STATE_TABLE_NAME, Item=item)
            return True
        except Exception:
            return False

    def _compose_state_item(self, state, user_id):
        return {'user_id': {'S': str(user_id), }, 'state': {'S': state}}
