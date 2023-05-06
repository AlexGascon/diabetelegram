from diabetelegram.actions.dexcom_actions import DexcomAction
from diabetelegram.actions.expense_actions import ExpenseAction, ExpenseAmountAction, ExpenseCategoryAction, ExpenseDescriptionAction
from diabetelegram.actions.insulin_actions import InsulinBasalAction, InsulinBolusAction, InsulinUnitsAction, InsulinSummaryAction
from diabetelegram.actions.meal_actions import MealAction, MealFoodAction
from diabetelegram.actions.url2pdf_actions import Url2PdfAction


class Actions:
    Expense = ExpenseAction
    ExpenseAmount = ExpenseAmountAction
    ExpenseCategory = ExpenseCategoryAction
    ExpenseDescription = ExpenseDescriptionAction
    Basal = InsulinBasalAction
    Bolus = InsulinBolusAction
    Units = InsulinUnitsAction
    InsulinSummary = InsulinSummaryAction
    Dexcom = DexcomAction
    Meal = MealAction
    MealFood = MealFoodAction
    Url2Pdf = Url2PdfAction

    ALL = [
        Expense,
        ExpenseAmount,
        ExpenseCategory,
        ExpenseDescription,
        Basal,
        Bolus,
        Units,
        InsulinSummary,
        Dexcom,
        Meal,
        MealFood,
        Url2Pdf
    ]