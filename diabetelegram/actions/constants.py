from diabetelegram.actions.expense_actions import ExpenseAction, ExpenseAmountAction, ExpenseCategoryAction, ExpenseDescriptionAction
from diabetelegram.actions.insulin_actions import InsulinBasalAction, InsulinBolusAction, InsulinUnitsAction, InsulinSummaryAction


class Actions:
    Expense = ExpenseAction
    ExpenseAmount = ExpenseAmountAction
    ExpenseCategory = ExpenseCategoryAction
    ExpenseDescription = ExpenseDescriptionAction
    Basal = InsulinBasalAction
    Bolus = InsulinBolusAction
    Units = InsulinUnitsAction
    InsulinSummary = InsulinSummaryAction

    ALL = [
        Expense,
        ExpenseAmount,
        ExpenseCategory,
        ExpenseDescription,
        Basal,
        Bolus,
        Units,
        InsulinSummary
    ]