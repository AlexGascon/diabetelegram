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
        return cls.FACTORIES[action_class]

    @staticmethod
    def expense_factory(*args):
        return Actions.Expense(*args)

    @staticmethod
    def basal_factory(*args):
        return Actions.Basal(*args)

    @staticmethod
    def bolus_factory(*args):
        return Actions.Bolus(*args)

    @staticmethod
    def units_factory(*args):
        return Actions.Units(*args)

    FACTORIES = {
        Actions.Expense: expense_factory.__func__,
        Actions.Basal: basal_factory.__func__,
        Actions.Bolus: bolus_factory.__func__,
        Actions.Units: units_factory.__func__
    }
