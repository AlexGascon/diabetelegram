from diabetelegram.parsers.meal_parser import MealParser
from diabetelegram.services.meal_web_client import MealWebClient
from diabetelegram.services.telegram import TelegramWrapper


class NewMealCommand:
    """Connects with the diabetes API to store information about a meal"""
    @staticmethod
    def handle(message):
        _, meal_info = message['text'].split(maxsplit=1)
        meal = MealParser(meal_info).to_meal()

        result = MealWebClient().create_meal(meal)

        telegram = TelegramWrapper()
        telegram.reply(message, result)
