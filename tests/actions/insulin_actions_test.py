import pytest
from unittest import mock

from diabetelegram.actions.insulin_actions import InsulinAction, InsulinBasalAction, InsulinBolusAction


class TestInsulinAction:
    @pytest.mark.parametrize('message', ['Insulin'], indirect=True)
    def test_matches_if_the_message_text_is_insulin(self, message):
        insulin_action = InsulinAction(message)

        assert insulin_action.matches()

    @pytest.mark.parametrize('message', ['some message'], indirect=True)
    def test_does_not_match_if_the_message_text_is_other(self, message):
        insulin_action = InsulinAction(message)

        assert not insulin_action.matches()


class TestInsulinBasalAction:
    @pytest.mark.parametrize('state, message', [('insulin', 'basal')], indirect=True)
    def test_matches_if_the_message_is_basal_and_state_is_insulin(self, state, message):
        basal_action = InsulinBasalAction(message)

        assert basal_action.matches()

    @pytest.mark.parametrize('state, message', [('some state', 'basal')], indirect=True)
    def test_does_not_match_if_state_is_not_insulin(self, state, message):
        basal_action = InsulinBasalAction(message)

        assert not basal_action.matches()

    @pytest.mark.parametrize('state, message', [('insulin', 'whatever')], indirect=True)
    def test_matches_if_the_message_is_not_basal(self, state, message):
        basal_action = InsulinBasalAction(message)

        assert not basal_action.matches()


class TestInsulinBolusAction:
    @pytest.mark.parametrize('state, message', [('insulin', 'bolus')], indirect=True)
    def test_matches_if_the_message_is_bolus_and_state_is_insulin(self, state, message):
        bolus_action = InsulinBolusAction(message)

        assert bolus_action.matches()

    @pytest.mark.parametrize('state, message', [('some state', 'bolus')], indirect=True)
    def test_does_not_match_if_state_is_not_insulin(self, state, message):
        bolus_action = InsulinBolusAction(message)

        assert not bolus_action.matches()

    @pytest.mark.parametrize('state, message', [('insulin', 'whatever')], indirect=True)
    def test_matches_if_the_message_is_not_bolus(self, state, message):
        bolus_action = InsulinBolusAction(message)

        assert not bolus_action.matches()
