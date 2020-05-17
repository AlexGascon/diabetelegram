from abc import ABC, abstractmethod


class BaseAction(ABC):
    def __init__(self, message, state_manager, telegram):
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
