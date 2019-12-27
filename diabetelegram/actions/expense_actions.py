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
    TELEGRAM_REPLY = 'Indicate the amount of the expense'

    def matches(self):
        return self._state_is_expense() and self._category_is_valid()

    def handle(self):
        expense = Expense(category=self._expense_category())
        expense.save()

        new_state = self._compose_new_state(expense)
        self.state_manager.set(new_state)

        self.telegram.reply(self.message, self.TELEGRAM_REPLY)

    def _state_is_expense(self):
        return self.state_manager.get() == self.EXPENSE_STATE

    def _category_is_valid(self):
        return self._expense_category() in Expense.CATEGORIES

    def _compose_new_state(self, expense):
        return f"expense-amount-{expense.expense_id}"

    def _expense_category(self):
        return self.message_text


class ExpenseAmountAction(BaseAction):
    STATE_PREFIX = 'expense-amount-'
    TELEGRAM_REPLY = 'Add a note for this expense'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._expense = None

    def matches(self):
        return self._state_is_expense_amount() and self._message_is_an_amount()

    def handle(self):
        amount = float(self.message_text)
        self.expense.amount = amount
        self.expense.save()

        new_state = self._compose_new_state()
        self.state_manager.set(new_state)

        self.telegram.reply(self.message, self.TELEGRAM_REPLY)

    @property
    def expense(self):
        if not self._expense:
            self._expense = Expense.get(self._expense_id())

        return self._expense

    def _expense_id(self):
        current_state = self.state_manager.get()
        return current_state[len(self.STATE_PREFIX):]

    def _state_is_expense_amount(self):
        return self.state_manager.get().startswith(self.STATE_PREFIX)

    def _message_is_an_amount(self):
        try:
            float(self.message_text)
            return True
        except ValueError:
            return False

    def _compose_new_state(self):
        return f"expense-notes-{self.expense.expense_id}"