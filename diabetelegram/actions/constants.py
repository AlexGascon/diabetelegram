from diabetelegram.actions.expense_actions import ExpenseAction
from diabetelegram.actions.insulin_actions import InsulinBasalAction, InsulinBolusAction, InsulinUnitsAction


class Actions:
    Expense = ExpenseAction
    Basal = InsulinBasalAction
    Bolus = InsulinBolusAction
    Units = InsulinUnitsAction

    ALL = [
        Expense,
        Basal,
        Bolus,
        Units
    ]