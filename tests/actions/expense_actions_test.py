import pytest

from diabetelegram.actions.constants import Actions
from tests.fixtures.actions import MockActionFactory


class TestExpenseAction:
    def build_action(self, message):
        return MockActionFactory.build(Actions.Expense, message)

    @pytest.mark.parametrize('message', ['Expense'], indirect=True)
    def test_matches_if_message_text_is_expense(self, message):
        expense_action = self.build_action(message)

        assert expense_action.matches()

    @pytest.mark.parametrize('message', ['some text'], indirect=True)
    def test_not_matches_on_other_message_texts(self, message):
        expense_action = self.build_action(message)

        assert not expense_action.matches()

    @pytest.mark.parametrize('message', ['Expense'], indirect=True)
    def test_handle_sets_the_state_to_expense(self, message):
        expense_action = self.build_action(message)

        expense_action.handle()

        expense_action.state_manager.set.assert_called_with('expense')

    def test_handle_sends_a_telegram_response(self, message):
        expense_action = self.build_action(message)

        expense_action.handle()

        expense_action.telegram.reply.assert_called_once()


class TestExpenseCategoryAction:
    def build_action(self, message, state_manager):
        return MockActionFactory.build(Actions.ExpenseCategory, message, state_manager=state_manager)

    @pytest.mark.parametrize('state, message', [('expense', 'Eating out')], indirect=True)
    def test_matches_when_the_state_is_expense_and_the_category_is_allowed(self, state, message):
        action = self.build_action(message, state)

        assert action.matches()

    @pytest.mark.parametrize('state, message', [('some state', 'Eating out')], indirect=True)
    def test_does_not_match_when_the_state_is_not_expense(self, state, message):
        action = self.build_action(message, state)

        assert not action.matches()

    @pytest.mark.parametrize('state, message', [('expense', 'not a category')], indirect=True)
    def test_does_not_match_when_the_message_is_not_a_valid_category(self, state, message):
        action = self.build_action(message, state)

        assert not action.matches()
