from unittest import mock

import pytest

from diabetelegram.actions.constants import Actions
from diabetelegram.models.meal import Meal
from tests.fixtures.actions import MockActionFactory


@pytest.fixture
def sns_client(mocker):
    sns_mock = mocker.patch('diabetelegram.actions.meal_actions.MealSNSClient')
    sns_instance = sns_mock.return_value
    return sns_instance


class TestMealAction:
    def build_action(self, message, state_manager=None):
        return MockActionFactory.build(Actions.Meal, message, state_manager=state_manager)

    @pytest.mark.parametrize('message', ['Meal'], indirect=True)
    def test_matches_if_message_is_meal(self, message):
        action = self.build_action(message)

        assert action.matches()

    @pytest.mark.parametrize('message', ['mEaL'], indirect=True)
    def test_matches_is_case_insensitive(self, message):
        action = self.build_action(message)

        assert action.matches()

    @pytest.mark.parametrize('message', ['Random message'], indirect=True)
    def test_does_not_match_with_a_different_message(self, message):
        action = self.build_action(message)

        assert not action.matches()

    @pytest.mark.parametrize('message', ['Meal'], indirect=True)
    def test_handle_sets_the_next_state(self, message):
        action = self.build_action(message)

        action.handle()

        action.state_manager.set.assert_called_once_with('meal')

    @pytest.mark.parametrize('message', ['Meal'], indirect=True)
    def test_handle_sends_a_telegram_response(self, message):
        action = self.build_action(message)

        action.handle()

        action.telegram.reply.assert_called_once()

class TestMealFoodAction:
    def build_action(self, message, state_manager=None):
        return MockActionFactory.build(Actions.MealFood, message, state_manager=state_manager)

    @pytest.mark.parametrize('state', ['meal'], indirect=True)
    def test_matches_if_state_is_meal(self, message, state):
        action = self.build_action(message, state_manager=state)

        assert action.matches()

    @pytest.mark.parametrize('state', ['random-state'], indirect=True)
    def test_does_not_match_if_state_is_not_meal(self, state, message):
        action = self.build_action(message, state)

        assert not action.matches()

    @pytest.mark.parametrize('state', ['meal'], indirect=True)
    def test_handle_sets_the_state_to_initial(self, message, state, sns_client):
        action = self.build_action(message, state_manager=state)

        action.handle()

        action.state_manager.set.assert_called_once_with('initial')


    @pytest.mark.parametrize('message, state', [('pizza', 'meal')], indirect=True)
    def test_handle_publishes_the_meal(self, message, state, sns_client):
        action = self.build_action(message, state_manager=state)

        action.handle()

        meal = Meal(food='pizza')
        sns_client.meal_eaten.assert_called_once_with(meal)

    
    @pytest.mark.parametrize('message, state', [('pizza', 'meal')], indirect=True)
    def test_handle_sends_a_telegram_response(self, message, state, sns_client):
        action = self.build_action(message, state_manager=state)

        action.handle()

        action.telegram.reply.assert_called_once()
