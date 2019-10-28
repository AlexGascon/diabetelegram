from diabetelegram.services.aws.dynamo import Dynamo


class StateManager:
    def __init__(self, user_id):
        self.user_id = user_id
        self._dynamo = Dynamo()

    def get(self):
        state_information = self._dynamo.get_state(user_id=self.user_id)
        return state_information['state']

    def set(self, new_state):
        result = self._dynamo.set_state(new_state, user_id=self.user_id)
        return result
