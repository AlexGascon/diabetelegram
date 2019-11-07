from abc import ABC, abstractmethod
from diabetelegram.services.state_manager import StateManager


class BaseAction(ABC):
    def __init__(self, message):
        self.message = message
        self.state_manager = StateManager(user_id=message['from']['id'])

    @abstractmethod
    def matches(self):
        pass

    @abstractmethod
    def handle(self):
        pass

    @property
    def message_text(self):
        return self.message['text'].lower()
