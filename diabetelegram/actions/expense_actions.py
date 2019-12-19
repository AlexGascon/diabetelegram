from diabetelegram.actions.base_action import BaseAction
from diabetelegram.models.expense import Expense


class ExpenseAction(BaseAction):
    EXPENSE_MESSAGE = 'expense'
    EXPENSE_STATE = 'expense'
    TELEGRAM_REPLY = "Select the expense category"

    def matches(self):
        return self.message_text == self.EXPENSE_MESSAGE

    def handle(self):
        self.state_manager.set(self.EXPENSE_STATE)

        self.telegram.reply(self.message, self.TELEGRAM_REPLY)


class ExpenseCategoryAction(BaseAction):
    EXPENSE_STATE = 'expense'

    def matches(self):
        return self._state_is_expense() and self._category_is_valid()

    def handle(self):
        pass

    def _state_is_expense(self):
        return self.state_manager.get() == self.EXPENSE_STATE

    def _category_is_valid(self):
        return self.message_text in Expense.CATEGORIES