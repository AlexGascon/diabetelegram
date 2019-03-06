import inspect
from dataclasses import dataclass


@dataclass
class Meal:
    """Represents a meal and its diabetic-related information"""
    carbohydrates_portions: float = None
    food:                   str = None
    insulin_units:          float = None
    meal_type:              str = None
    notes:                  str = None
    pre_blood_glucose:      int = None
    post_blood_glucose:     int = None

    def __str__(self):
        meal_text = f"""
        Meal
        -----
        Carbohydrates: {self.carbohydrates_portions} portions
        Food: {self.food}
        Insulin: {self.insulin_units} units
        Meal type: {self.meal_type.capitalize()}
        Blood Glucose level - Previous: {self.pre_blood_glucose} - Posterior: {self.post_blood_glucose}
        Notes: {self.notes}
        """

        return inspect.cleandoc(meal_text)

