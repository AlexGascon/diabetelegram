from diabetelegram.actions.constants import Actions
from diabetelegram.actions.factory import ActionFactory

class MessageRouter:
    """Sends a message to the action that corresponds for its processing"""

    @classmethod
    def dispatch(cls, message):
        for action_class in Actions.ALL:
            action = ActionFactory.build(action_class, message)

            if action.matches():
                action.handle()
                break
