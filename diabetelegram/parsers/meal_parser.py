from dataclasses import dataclass

from diabetelegram.models.meal import Meal

@dataclass
class MealParser:
    message: str

    def to_meal(self):
        meal_fields = {
            "carbohydrates_portions": self.parse_carbohydrates_portions(),
            "food": self.parse_food(),
            "insulin_units": self.parse_insulin_units(),
            "meal_type": self.parse_meal_type(),
            "pre_blood_glucose": self.parse_pre_blood_glucose(),
            "post_blood_glucose": self.parse_post_blood_glucose()
        }
        
        return Meal(**meal_fields)

    def parse_carbohydrates_portions(self):
        carbohydrates_portions_value = self._extract_value("raciones")

        if carbohydrates_portions_value:
            return float(carbohydrates_portions_value)

    def parse_food(self):
        return self._extract_value("comida")

    def parse_insulin_units(self):
        insulin_units_value = self._extract_value("insulina")

        if insulin_units_value:
            return float(insulin_units_value)

    def parse_meal_type(self):
        return self._extract_value("tipo")

    def parse_pre_blood_glucose(self):
        pre_blood_glucose_value = self._extract_value("pre")
        
        if pre_blood_glucose_value:
            return int(pre_blood_glucose_value)

    def parse_post_blood_glucose(self):
        post_blood_glucose_value = self._extract_value("post")

        if post_blood_glucose_value:
            return int(post_blood_glucose_value)

    def _extract_value(self, field_key):
        field_info = list(filter(lambda m: m.strip().startswith(field_key), self._message_parts()))

        if not field_info:
            return None

        field_value = field_info[0].split(":")[1].strip()

        return field_value

    def _message_parts(self):
        return self.message.split(",")