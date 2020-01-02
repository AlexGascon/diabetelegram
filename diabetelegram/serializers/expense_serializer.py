from dataclasses import dataclass

from diabetelegram.models.expense import Expense

@dataclass
class ExpenseSerializer:
    expense: Expense

    def to_dict(self):
        data = {
            'expense_id': self.expense.expense_id,
            'amount': self.expense.amount,
            'category': self.expense.category,
            'notes': self.expense.notes
        }

        return {key: value for key, value in data.items() if value is not None}
