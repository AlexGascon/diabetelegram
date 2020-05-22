from abc import ABC, abstractmethod


class BaseAction(ABC):
    VALID_USER_ID = 713744
    def __init__(self, message, state_manager, telegram):
        self._validate_user(message)

        self.message = message
        self.state_manager = state_manager
        self.telegram = telegram

    @abstractmethod
    def matches(self):
        pass

    @abstractmethod
    def handle(self):
        pass

    @property
    def message_text(self):
        if 'text' not in self.message:
            return ''

        return self.message['text']

    def _validate_user(self, message):
        user_id = int(message['from']['id'])
        if not user_id == self.VALID_USER_ID:
            raise ValueError('User not authorized to trigger actions')
