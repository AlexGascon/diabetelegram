from dataclasses import dataclass

from diabetelegram.models.meal import Meal


@dataclass
class MealSerializer:
    meal: Meal

    def to_dict(self):
        data = {
            "carbohydrates_portions": self.meal.carbohydrates_portions,
            "food": self.meal.food,
            "insulin_units": self.meal.insulin_units,
            "meal_type": self.meal.meal_type,
            "pre_blood_glucose": self.meal.pre_blood_glucose,
            "post_blood_glucose": self.meal.post_blood_glucose
        }

        return {key: value for key, value in data.items() if value is not None}
