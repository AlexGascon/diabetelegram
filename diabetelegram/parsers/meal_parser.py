from diabetelegram.parsers.base_parser import BaseParser
from diabetelegram.models.meal import Meal


class MealParser(BaseParser):
    def to_meal(self):
        meal_fields = {
            "carbohydrates_portions": self.parse_carbohydrates_portions(),
            "food": self.parse_food(),
            "insulin_units": self.parse_insulin_units(),
            "meal_type": self.parse_meal_type(),
            "notes": self.parse_notes(),
            "pre_blood_glucose": self.parse_pre_blood_glucose(),
            "post_blood_glucose": self.parse_post_blood_glucose()
        }
        
        return Meal(**meal_fields)

    def parse_carbohydrates_portions(self):
        carbohydrates_portions_value = self._extract_value("raciones")

        return float(carbohydrates_portions_value) if carbohydrates_portions_value else None

    def parse_food(self):
        return self._extract_value("comida")

    def parse_insulin_units(self):
        insulin_units_value = self._extract_value("insulina")

        return float(insulin_units_value) if insulin_units_value else None

    def parse_meal_type(self):
        return self._extract_value("tipo")

    def parse_notes(self):
        return self._extract_value("notas")

    def parse_pre_blood_glucose(self):
        pre_blood_glucose_value = self._extract_value("pre")
        
        return int(pre_blood_glucose_value) if pre_blood_glucose_value else None

    def parse_post_blood_glucose(self):
        post_blood_glucose_value = self._extract_value("post")

        return int(post_blood_glucose_value) if post_blood_glucose_value else None
