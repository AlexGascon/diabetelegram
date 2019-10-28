from diabetelegram.services.aws.dynamo import Dynamo


class StatusManager:
    def __init__(self, user_id):
        self.user_id = user_id
        self._dynamo = Dynamo()

    def get(self):
        status_information = self._dynamo.get_status(user_id=self.user_id)
        return status_information['status']

    def set(self, new_status):
        result = self._dynamo.set_status(new_status, user_id=self.user_id)
        return result
