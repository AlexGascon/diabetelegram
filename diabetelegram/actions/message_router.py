from diabetelegram.actions.insulin_actions import InsulinAction, InsulinBasalAction, InsulinBolusAction, InsulinUnitsAction

class MessageRouter:
    """Sends a message to the action that corresponds for its processing"""

    ACTIONS = [
        InsulinAction,
        InsulinBasalAction,
        InsulinBolusAction,
        InsulinUnitsAction
    ]

    @classmethod
    def dispatch(cls, message):
        for action_class in cls.ACTIONS:
            action = action_class(message)

            if action.matches():
                action.handle()
                break
