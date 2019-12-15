from diabetelegram.actions.base_action import BaseAction


class ExpenseAction(BaseAction):
    EXPENSE_MESSAGE = 'expense'
    EXPENSE_STATE = 'expense'
    TELEGRAM_REPLY = "Select the expense category"

    def matches(self):
        return self.message_text == self.EXPENSE_MESSAGE

    def handle(self):
        self.state_manager.set(self.EXPENSE_STATE)

        self.telegram.reply(self.message, self.TELEGRAM_REPLY)
