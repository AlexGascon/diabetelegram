from diabetelegram.actions.constants import Actions
from diabetelegram.services.state_manager import StateManager
from diabetelegram.services.telegram import TelegramWrapper


class ActionFactory:
    """
    Encapsulates the logic of building an action

    Some examples of this logic are extracting the user from the message or
    instantiating and setting the fields that the action will be using
    """

    @classmethod
    def build(cls, action_class, message):
        factory = cls.get_factory(action_class)
        state_manager = StateManager(user_id=message['from']['id'])
        telegram = TelegramWrapper()

        return factory(message, state_manager, telegram)

    @classmethod
    def get_factory(cls, action_class):
        if action_class in cls.COMPLEX_FACTORIES:
            return cls.COMPLEX_FACTORIES.get(action_class)
        else:
            return lambda *args: action_class(*args)

    COMPLEX_FACTORIES = {}
