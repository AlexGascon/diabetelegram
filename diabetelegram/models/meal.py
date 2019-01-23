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
