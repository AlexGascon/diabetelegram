import pytest
from unittest import mock

from diabetelegram.actions.insulin_actions import InsulinAction, InsulinBasalAction, InsulinBolusAction, InsulinUnitsAction
from diabetelegram.models.injection import Injection


@pytest.fixture
def telegram(mocker):
    telegram_mock = mocker.patch('diabetelegram.actions.insulin_actions.TelegramWrapper')
    telegram_instance = telegram_mock.return_value
    return telegram_instance

@pytest.fixture
def sns_client(mocker):
    sns_mock = mocker.patch('diabetelegram.actions.insulin_actions.InjectionSNSClient')
    sns_instance = sns_mock.return_value
    return sns_instance

class TestInsulinAction:
    @pytest.mark.parametrize('message', ['Insulin'], indirect=True)
    def test_matches_if_the_message_text_is_insulin(self, message, state):
        insulin_action = InsulinAction(message)

        assert insulin_action.matches()

    @pytest.mark.parametrize('message', ['some message'], indirect=True)
    def test_does_not_match_if_the_message_text_is_other(self, message, state):
        insulin_action = InsulinAction(message)

        assert not insulin_action.matches()

    def test_handle_sets_the_state_to_insulin(self, state, message, telegram):
        InsulinAction(message).handle()

        state.set.assert_called_with('insulin')

    def test_handle_sends_a_telegram_response(self, telegram, message, state):
        InsulinAction(message).handle()

        telegram.reply.assert_called_once()


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

    def test_handle_sets_the_state_to_basal(self, state, message, telegram):
        InsulinBasalAction(message).handle()

        state.set.assert_called_with('basal')

    def test_handle_sends_a_telegram_response(self, telegram, message, state):
        InsulinBasalAction(message).handle()

        telegram.reply.assert_called_once()


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

    def test_handle_sets_the_state_to_bolus(self, state, message, telegram):
        InsulinBolusAction(message).handle()

        state.set.assert_called_with('bolus')

    def test_handle_sends_a_telegram_response(self, telegram, message, state):
        InsulinBolusAction(message).handle()

        telegram.reply.assert_called_once()


class TestInsulinUnitsAction:
    @pytest.mark.parametrize('state, message', [('bolus', '18')], indirect=True)
    def test_matches_if_the_message_is_an_integer_and_state_is_bolus(self, state, message):
        units_action = InsulinUnitsAction(message)

        assert units_action.matches()

    @pytest.mark.parametrize('state, message', [('basal', '18')], indirect=True)
    def test_matches_if_the_message_is_an_integer_and_state_is_basal(self, state, message):
        units_action = InsulinUnitsAction(message)

        assert units_action.matches()

    @pytest.mark.parametrize('state, message', [('other_state', '185')], indirect=True)
    def test_not_matches_if_state_is_not_basal_or_bolus(self, state, message):
        units_action = InsulinUnitsAction(message)

        assert not units_action.matches()

    @pytest.mark.parametrize('state, message', [('basal', '18.5')], indirect=True)
    def test_not_matches_if_message_is_not_an_integer(self, state, message):
        units_action = InsulinUnitsAction(message)

        assert not units_action.matches()

    @pytest.mark.parametrize('message', ['22'], indirect=True)
    def test_handle_sets_the_state_to_initial(self, state, message, telegram, sns_client):
        InsulinUnitsAction(message).handle()

        state.set.assert_called_with('initial')

    @pytest.mark.parametrize('state, message', [('basal', '18')], indirect=True)
    def test_handle_publishes_the_injection(self, state, message, telegram, sns_client):
        InsulinUnitsAction(message).handle()

        expected_injection = Injection(injection_type='basal', units=18)
        sns_client.insulin_injected.assert_called_once_with(expected_injection)

    @pytest.mark.parametrize('message', ['22'], indirect=True)
    def test_handle_sets_the_state_to_initial(self, state, message, telegram, sns_client):
        InsulinUnitsAction(message).handle()

        telegram.reply.assert_called_once()
