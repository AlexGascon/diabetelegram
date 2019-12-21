from diabetelegram.models.expense import Expense


def test_expense_is_created():
    assert Expense.count() == 0
    Expense(expense_id='test_id', amount=42, category='coca cola').save()
    assert Expense.count() == 1
