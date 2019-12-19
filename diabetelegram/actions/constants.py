from diabetelegram.actions.expense_actions import ExpenseAction, ExpenseCategoryAction
from diabetelegram.actions.insulin_actions import InsulinBasalAction, InsulinBolusAction, InsulinUnitsAction


class Actions:
    Expense = ExpenseAction
    ExpenseCategory = ExpenseCategoryAction
    Basal = InsulinBasalAction
    Bolus = InsulinBolusAction
    Units = InsulinUnitsAction

    ALL = [
        Expense,
        ExpenseCategory,
        Basal,
        Bolus,
        Units
    ]