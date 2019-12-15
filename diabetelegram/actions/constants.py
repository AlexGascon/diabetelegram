from diabetelegram.actions.insulin_actions import InsulinAction, InsulinBasalAction, InsulinBolusAction, InsulinUnitsAction

class Actions:
    Insulin = InsulinAction
    Basal = InsulinBasalAction
    Bolus = InsulinBolusAction
    Units = InsulinUnitsAction

    ALL = [
        Insulin,
        Basal,
        Bolus,
        Units
    ]