from unittest.mock import Mock
from unittest.mock import create_autospec

import pytest

from diabetelegram.actions.factory import ActionFactory
from diabetelegram.services.state_manager import StateManager
from diabetelegram.services.telegram import TelegramWrapper

class MockActionFactory(ActionFactory):
    """
    Subclass of ActionFactory to be used in our tests

    Avoids creating real instances of the required objects and uses autospecs
    in its place
    """

    @classmethod
    def build(cls, action_class, message, state_manager=None, telegram=None):
        factory = cls.get_factory(action_class)

        if not state_manager:
            state_manager = create_autospec(StateManager)

        if not telegram:
            telegram = create_autospec(TelegramWrapper)

        return factory(message, state_manager, telegram)
