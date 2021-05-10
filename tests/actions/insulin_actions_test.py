import pytest
from unittest import mock

from diabetelegram.actions.constants import Actions
from tests.fixtures.actions import MockActionFactory
from diabetelegram.actions.insulin_actions import InsulinBasalAction, InsulinBolusAction, InsulinUnitsAction
from diabetelegram.models.injection import Injection


@pytest.fixture
def sns_client(mocker):
    sns_mock = mocker.patch('diabetelegram.actions.insulin_actions.InjectionSNSClient')
    sns_instance = sns_mock.return_value
    return sns_instance

@pytest.fixture
def sns_summary_client(mocker):
    sns_mock = mocker.patch('diabetelegram.actions.insulin_actions.SummarySNSClient')
    sns_instance = sns_mock.return_value
    return sns_instance


class TestInsulinBasalAction:
    def build_action(self, message, state_manager):
        return MockActionFactory.build(Actions.Basal, message, state_manager)

    @pytest.mark.parametrize('state, message', [('whatever', 'basal')], indirect=True)
    def test_matches_if_the_message_is_basal(self, state, message):
        basal_action = self.build_action(message, state)

        assert basal_action.matches()

    @pytest.mark.parametrize('state, message', [('whatever', 'BASAL')], indirect=True)
    def test_matches_is_case_insensitive(self, state, message):
        basal_action = self.build_action(message, state)

        assert basal_action.matches()

    @pytest.mark.parametrize('state, message', [('insulin', 'whatever')], indirect=True)
    def test_does_not_match_if_the_message_is_not_basal(self, state, message):
        basal_action = self.build_action(message, state)

        assert not basal_action.matches()

    def test_handle_sets_the_state_to_basal(self, state, message):
        basal_action = self.build_action(message, state)

        basal_action.handle()

        state.set.assert_called_with('basal')

    def test_handle_sends_a_telegram_response(self, message, state):
        basal_action = self.build_action(message, state)

        basal_action.handle()

        basal_action.telegram.reply.assert_called_once()


class TestInsulinBolusAction:
    def build_action(self, message, state_manager):
        return MockActionFactory.build(Actions.Bolus, message, state_manager)

    @pytest.mark.parametrize('state, message', [('whatever', 'bolus')], indirect=True)
    def test_matches_if_the_message_is_bolus(self, state, message):
        bolus_action = self.build_action(message, state)

        assert bolus_action.matches()

    @pytest.mark.parametrize('state, message', [('whatever', 'BOLUS')], indirect=True)
    def test_matches_is_case_insensitive(self, state, message):
        bolus_action = self.build_action(message, state)

        assert bolus_action.matches()

    @pytest.mark.parametrize('state, message', [('insulin', 'whatever')], indirect=True)
    def test_does_not_match_if_the_message_is_not_bolus(self, state, message):
        bolus_action = self.build_action(message, state)

        assert not bolus_action.matches()

    def test_handle_sets_the_state_to_bolus(self, state, message):
        bolus_action = self.build_action(message, state)

        bolus_action.handle()

        state.set.assert_called_with('bolus')

    def test_handle_sends_a_telegram_response(self, message, state):
        bolus_action = self.build_action(message, state)

        bolus_action.handle()

        bolus_action.telegram.reply.assert_called_once()


class TestInsulinUnitsAction:
    def build_action(self, message, state_manager):
        return MockActionFactory.build(Actions.Units, message, state_manager)

    @pytest.mark.parametrize('state, message', [('bolus', '18')], indirect=True)
    def test_matches_if_the_message_is_an_integer_and_state_is_bolus(self, state, message):
        units_action = self.build_action(message, state)

        assert units_action.matches()

    @pytest.mark.parametrize('state, message', [('basal', '18')], indirect=True)
    def test_matches_if_the_message_is_an_integer_and_state_is_basal(self, state, message):
        units_action = self.build_action(message, state)

        assert units_action.matches()

    @pytest.mark.parametrize('state, message', [('other_state', '185')], indirect=True)
    def test_not_matches_if_state_is_not_basal_or_bolus(self, state, message):
        units_action = self.build_action(message, state)

        assert not units_action.matches()

    @pytest.mark.parametrize('state, message', [('basal', '18.5')], indirect=True)
    def test_not_matches_if_message_is_not_an_integer(self, state, message):
        units_action = self.build_action(message, state)

        assert not units_action.matches()

    @pytest.mark.parametrize('state, message', [('basal', '-1')], indirect=True)
    def test_matches_if_the_message_is_a_negative_integer(self, state, message):
        units_action = self.build_action(message, state)

        assert units_action.matches()

    @pytest.mark.parametrize('message', ['22'], indirect=True)
    def test_handle_sets_the_state_to_initial(self, state, message, sns_client):
        units_action = self.build_action(message, state)

        units_action.handle()

        state.set.assert_called_with('initial')

    @pytest.mark.parametrize('state, message', [('basal', '18')], indirect=True)
    def test_handle_publishes_the_injection(self, state, message, sns_client):
        units_action = self.build_action(message, state)

        units_action.handle()

        expected_injection = Injection(injection_type='basal', units=18)
        sns_client.insulin_injected.assert_called_once_with(expected_injection)

    @pytest.mark.parametrize('message', ['22'], indirect=True)
    def test_handle_sets_the_state_to_initial(self, state, message, sns_client):
        units_action = self.build_action(message, state)

        units_action.handle()


class TestInsulinSummaryAction:
    def build_action(self, message, state_manager):
        return MockActionFactory.build(Actions.InsulinSummary, message, state_manager)

    @pytest.mark.parametrize('message', ['summary'], indirect=True)
    def test_matches_if_the_message_is_summary(self, state, message):
        summary_action = self.build_action(message, state)

        assert summary_action.matches()

    @pytest.mark.parametrize('message', ['SUMMARY'], indirect=True)
    def test_matches_is_case_insensitive(self, state, message):
        summary_action = self.build_action(message, state)

        assert summary_action.matches()

    @pytest.mark.parametrize('message', ['whatever'], indirect=True)
    def test_does_not_match_if_the_message_is_not_summary(self, state, message):
        summary_action = self.build_action(message, state)

        assert not summary_action.matches()

    def test_handle_requests_the_summary(self, sns_summary_client, message, state):
        summary_action = self.build_action(message, state)

        summary_action.handle()

        sns_summary_client.summary_requested.assert_called_once()

    @pytest.mark.parametrize('message', ['summary'], indirect=True)
    def test_handle_sets_the_state_to_initial(self, state, message, sns_summary_client):
        summary_action = self.build_action(message, state)

        summary_action.handle()

        state.set.assert_called_with('initial')
