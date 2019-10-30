import pytest
from unittest import mock

from diabetelegram.actions.insulin_actions import InsulinAction, InsulinBasalAction, InsulinBolusAction


class TestInsulinAction:
    def test_matches_if_the_message_text_is_insulin(self):
        insulin_action = InsulinAction({'text': 'Insulin', 'from': {'id': 'dummy'}})

        assert insulin_action.matches()

    def test_does_not_match_if_the_message_text_is_other(self):
        insulin_action = InsulinAction({'text': 'whatever', 'from': {'id': 'dummy'}})

        assert not insulin_action.matches()


class TestInsulinBasalAction:
    def test_matches_if_the_message_is_basal_and_state_is_insulin(self):
        with mock.patch('diabetelegram.actions.base_action.StateManager') as mocked_state_manager:
            mocked_state_manager.return_value.get.return_value = 'insulin'

            basal_action = InsulinBasalAction({'text': 'basal', 'from': {'id': 'dummy'}})

        assert basal_action.matches()

    def test_does_not_match_if_state_is_not_insulin(self):
        with mock.patch('diabetelegram.actions.base_action.StateManager') as mocked_state_manager:
            mocked_state_manager.return_value.get.return_value = 'whatever'

            basal_action = InsulinBasalAction({'text': 'basal', 'from': {'id': 'dummy'}})

        assert not basal_action.matches()

    def test_matches_if_the_message_is_not_basal(self):
        with mock.patch('diabetelegram.actions.base_action.StateManager') as mocked_state_manager:
            mocked_state_manager.return_value.get.return_value = 'insulin'

            basal_action = InsulinBasalAction({'text': 'whatever', 'from': {'id': 'dummy'}})

        assert not basal_action.matches()


class TestInsulinBolusAction:
    def test_matches_if_the_message_is_bolus_and_state_is_insulin(self):
        with mock.patch('diabetelegram.actions.base_action.StateManager') as mocked_state_manager:
            mocked_state_manager.return_value.get.return_value = 'insulin'

            bolus_action = InsulinBolusAction({'text': 'bolus', 'from': {'id': 'dummy'}})

        assert bolus_action.matches()

    def test_does_not_match_if_state_is_not_insulin(self):
        with mock.patch('diabetelegram.actions.base_action.StateManager') as mocked_state_manager:
            mocked_state_manager.return_value.get.return_value = 'whatever'

            bolus_action = InsulinBolusAction({'text': 'bolus', 'from': {'id': 'dummy'}})

        assert not bolus_action.matches()

    def test_matches_if_the_message_is_not_bolus(self):
        with mock.patch('diabetelegram.actions.base_action.StateManager') as mocked_state_manager:
            mocked_state_manager.return_value.get.return_value = 'insulin'

            bolus_action = InsulinBolusAction({'text': 'whatever', 'from': {'id': 'dummy'}})

        assert not bolus_action.matches()
