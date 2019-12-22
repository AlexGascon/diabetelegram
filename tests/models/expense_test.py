import pytest

from diabetelegram.models.expense import Expense


def test_expense_is_created():
    assert Expense.count() == 0
    Expense(expense_id='test_id', amount=42, category='coca cola', notes='Test notes').save()
    assert Expense.count() == 1

def test_expense_is_set_automatically():
    expense = Expense(amount=42, category='coca cola', notes='test notes')
    assert expense.expense_id is not None

def test_category_is_mandatory():
    with pytest.raises(ValueError):
        Expense(amount=42, notes='test notes').save()

def test_amount_is_not_mandatory():
    assert Expense.count() == 0
    Expense(category='coca cola', notes='test notes').save()
    assert Expense.count() == 1

def test_notes_is_not_mandatory():
    assert Expense.count() == 0
    Expense(category='coca cola', amount=42).save()
    assert Expense.count() == 1
