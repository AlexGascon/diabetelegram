from diabetelegram.actions.base_action import BaseAction
from diabetelegram.models.meal import Meal
from diabetelegram.services.meal_sns_client import MealSNSClient


class MealAction(BaseAction):
    MEAL_MESSAGE = 'meal'
    MEAL_STATE = 'meal'
    TELEGRAM_REPLY = 'What food did you eat?'

    def matches(self):
        return self.message_text.lower() == self.MEAL_MESSAGE

    def handle(self):
        self.state_manager.set(self.MEAL_STATE)

        self.telegram.reply(self.message, self.TELEGRAM_REPLY)

class MealFoodAction(BaseAction):
    MEAL_STATE = 'meal'
    INITIAL_STATE = 'initial'

    def matches(self):
        state = self.state_manager.get()
        return state == self.MEAL_STATE

    def handle(self):
        self.state_manager.set('initial')

        meal = Meal(food=self.message_text)
        message_id = MealSNSClient().meal_eaten(meal)

        reply = f'Meal published.\nMessage ID: {message_id}'
        self.telegram.reply(self.message, reply)
