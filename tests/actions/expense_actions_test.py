from unittest import mock

import pytest

from diabetelegram.actions.constants import Actions
from diabetelegram.models.expense import Expense
from tests.fixtures.actions import MockActionFactory


class TestExpenseAction:
    def build_action(self, message):
        return MockActionFactory.build(Actions.Expense, message)

    @pytest.mark.parametrize('message', ['Expense'], indirect=True)
    def test_matches_if_message_text_is_expense(self, message):
        expense_action = self.build_action(message)

        assert expense_action.matches()

    @pytest.mark.parametrize('message', ['EXPENSE'], indirect=True)
    def test_matches_is_case_insensitive(self, message):
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

    @pytest.mark.parametrize('state, message', [('expense', 'EATING OUT')], indirect=True)
    def test_matches_is_case_insensitive(self, state, message):
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

    @pytest.mark.parametrize('state, message', [('expense', 'Eating out')], indirect=True)
    def test_handle_creates_the_expense(self, message, state):
        action = self.build_action(message, state)
        count = Expense.count()

        action.handle()

        assert Expense.count() == count + 1

    @pytest.mark.parametrize('state, message', [('expense', 'Eating out')], indirect=True)
    def test_handle_sets_the_state_to_expense_amount(self, state, message):
        action = self.build_action(message, state)

        action.handle()

        mock_args, mock_kwargs = action.state_manager.set.call_args
        assert mock_args[0].startswith('expense-amount-')

    @pytest.mark.parametrize('state, message', [('expense', 'Eating out')], indirect=True)
    def test_handle_sends_a_telegram_response(self, state, message):
        action = self.build_action(message, state)

        action.handle()

        action.telegram.reply.assert_called_once()


class TestExpenseAmountAction:
    def build_action(self, message, state_manager):
        return MockActionFactory.build(Actions.ExpenseAmount, message, state_manager=state_manager)

    @pytest.mark.parametrize('state, message', [('expense-amount-abcdef', '12.40')], indirect=True)
    def test_matches_if_text_is_an_amount_and_state_is_expense_amount(self, message, state):
        Expense(id='abcdef', category='random category').save()
        action = self.build_action(message, state)

        assert action.matches()

    @pytest.mark.parametrize('state, message', [('expense-amount-abcdef', 'five')], indirect=True)
    def test_does_not_match_if_text_is_not_an_amount(self, state, message):
        Expense(id='abcdef', category='random category').save()
        action = self.build_action(message, state)

        assert not action.matches()

    @pytest.mark.parametrize('state, message', [('some state', '12.40')], indirect=True)
    def test_does_not_match_if_state_is_not_expense_amount(self, message, state):
        Expense(id='abcdef', category='random category').save()
        action = self.build_action(message, state)

        assert not action.matches()

    @pytest.mark.parametrize('state, message', [('expense-amount-abcdef', '12.40')], indirect=True)
    def test_handle_updates_the_expense(self, state, message):
        expense = Expense(id='abcdef', category='random category')
        expense.save()
        action = self.build_action(message, state)

        assert not expense.amount

        action.handle()

        expense.refresh()
        assert expense.amount == 12.40

    @pytest.mark.parametrize('state, message', [('expense-amount-abcdef', '12.40')], indirect=True)
    def test_handle_sets_the_next_state(self, state, message):
        Expense(id='abcdef', category='random category').save()
        action = self.build_action(message, state)

        action.handle()

        action.state_manager.set.assert_called_once_with('expense-notes-abcdef')

    @pytest.mark.parametrize('state, message', [('expense-amount-abcdef', '12.40')], indirect=True)
    def test_handle_sends_a_telegram_response(self, state, message):
        Expense(id='abcdef', category='random category').save()
        action = self.build_action(message, state)

        action.handle()

        action.telegram.reply.assert_called_once()


class TestExpenseDescriptionAction:
    def build_action(self, message, state_manager):
        return MockActionFactory.build(Actions.ExpenseDescription, message, state_manager=state_manager)

    @pytest.mark.parametrize('state', [('expense-notes-abcdef')], indirect=True)
    def test_matches_if_state_is_expense_description(self, message, state):
        Expense(id='abcdef', category='random category').save()
        action = self.build_action(message, state)

        assert action.matches()

    @pytest.mark.parametrize('state', [('random state')], indirect=True)
    def test_does_not_match_if_text_is_not_expense_description(self, message, state):
        Expense(id='abcdef', category='random category').save()
        action = self.build_action(message, state)

        assert not action.matches()

    @pytest.mark.parametrize('state, message', [('expense-notes-abcdef', 'Description of the expense')], indirect=True)
    def test_handle_updates_the_expense(self, state, message, sns_client):
        expense = Expense(id='abcdef', category='random category')
        expense.save()
        action = self.build_action(message, state)

        assert not expense.notes

        action.handle()

        expense.refresh()
        assert expense.notes == 'Description of the expense'.lower()

    @pytest.mark.parametrize('state, message', [('expense-notes-abcdef', 'Description of the expense')], indirect=True)
    def test_handle_sets_the_next_state(self, state, message, sns_client):
        Expense(id='abcdef', category='random category').save()
        action = self.build_action(message, state)

        action.handle()

        action.state_manager.set.assert_called_once_with('initial')

    @pytest.mark.parametrize('state, message', [('expense-notes-abcdef', 'Description of the expense')], indirect=True)
    def test_handle_sends_a_telegram_response(self, state, message, sns_client):
        Expense(id='abcdef', category='random category').save()
        action = self.build_action(message, state)

        action.handle()

        action.telegram.reply.assert_called_once()

    @pytest.mark.parametrize('state, message', [('expense-notes-abcdef', 'Description of the expense')], indirect=True)
    def test_handle_publishes_the_expense(self, state, message, sns_client):
        expected_expense = Expense(id='abcdef', category='Some category', amount=42.24, notes='description of the expense')
        expected_expense.save()
        action = self.build_action(message, state)
        action._expense = expected_expense

        action.handle()

        sns_client.money_spent.assert_called_once_with(expected_expense)


@pytest.fixture
def sns_client(mocker):
    sns_mock = mocker.patch('diabetelegram.actions.expense_actions.ExpenseSNSClient')
    sns_instance = sns_mock.return_value
    return sns_instance
