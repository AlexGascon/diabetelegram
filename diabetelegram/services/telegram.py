import os

import telebot


class TelegramWrapper:
    """Handles interactions with the Telegram Bot API"""
    def __init__(self):
        self.bot = telebot.TeleBot(os.environ['TELEGRAM_BOT_TOKEN'])

    def reply(self, message, output_message):
        chat_id = message['chat']['id']
        self.bot.send_message(chat_id=chat_id, text=output_message)
        return None

    def extract_message(self, update):
        return update['message']
