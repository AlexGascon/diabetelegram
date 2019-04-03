from diabetelegram.parsers.meal_parser import MealParser
from diabetelegram.services.meal_web_client import MealWebClient
from diabetelegram.services.telegram import TelegramWrapper


class NewMealCommand:
    """Connects with the diabetes API to store information about a meal
    
    It expects the message to have the following form: 
    <command> <meal_info>
    """

    @staticmethod
    def handle(message):
        _, meal_info = message['text'].split(maxsplit=1)
        meal = MealParser(meal_info).to_meal()

        result = MealWebClient().create_meal(meal)

        telegram = TelegramWrapper()
        telegram.reply(message, result)


class EditMealCommand:
    """Connects with the diabetes API to edit information about a meal
    
    It expects the message to have the following form: 
    <command> <meal_id> <meal_info>
    """

    @staticmethod
    def handle(message):
        _, meal_id, meal_info = message['text'].split(maxsplit=2)
        meal = MealParser(meal_info).to_meal()

        result = MealWebClient().edit_meal(meal_id, meal)

        telegram = TelegramWrapper()
        telegram.reply(message, result)


class DeleteMealCommand:
    """Connects with the diabetes API to delete a meal by its ID
    
    It expects the message to have the following form: 
    <command> <meal_id>
    """

    @staticmethod
    def handle(message):
        _, meal_id = message['text'].split(maxsplit=1)

        result = MealWebClient().delete_meal(meal_id)

        telegram = TelegramWrapper()
        telegram.reply(message, result)


class SearchMealCommand:
    """Connects with the diabetes API to search meals containing specific words

    It expects the message to have the following form:
    /searchmeal <search term>
    """

    @staticmethod
    def handle(message):
        _, search_term = message['text'].split(maxsplit=1)

        result = MealWebClient().search_meal(search_term)

        TelegramWrapper().reply(message, result)
