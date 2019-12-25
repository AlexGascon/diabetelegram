from diabetelegram.actions.insulin_actions import InsulinBasalAction, InsulinBolusAction, InsulinUnitsAction

class Actions:
    Basal = InsulinBasalAction
    Bolus = InsulinBolusAction
    Units = InsulinUnitsAction

    ALL = [
        Basal,
        Bolus,
        Units
    ]