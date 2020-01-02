from diabetelegram.models.expense import Expense
from diabetelegram.serializers.expense_serializer import ExpenseSerializer


def test_to_dict():
    amount = 12
    category = 'eating out'
    notes = 'Data of the expense'

    expense = Expense(amount=amount, notes=notes, category=category)
    serialized = ExpenseSerializer(expense).to_dict()

    assert serialized['amount'] == amount
    assert serialized['category'] == category
    assert serialized['notes'] == notes
    assert serialized['expense_id'] == expense.expense_id

def test_to_dict_with_incomplete_expense():
    amount = 12
    category = 'eating out'

    expense = Expense(amount=amount, category=category)
    serialized = ExpenseSerializer(expense).to_dict()

    assert serialized['amount'] == amount
    assert serialized['category'] == category
    assert 'notes' not in serialized
    assert serialized['expense_id'] == expense.expense_id
