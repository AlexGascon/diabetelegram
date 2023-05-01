import os

import requests
import telebot


class TelegramWrapper:
    """Handles interactions with the Telegram Bot API"""
    def __init__(self):
        self.bot_token = os.environ['TELEGRAM_BOT_TOKEN']
        self.bot = telebot.TeleBot(self.bot_token)

    def reply(self, message, output_message):
        chat_id = message['chat']['id']
        self.bot.send_message(chat_id=chat_id, text=output_message)
        return None

    def send_document(self, message, document):
        chat_id = message['chat']['id']
        self.bot.send_document(chat_id=chat_id, document=document, timeout=120)
        return None

    def extract_message(self, update):
        return update['message']

    def get_file(self, message):
        file_id = message['document']['file_id']
        file = self.bot.get_file(file_id)

        file_url = f"https://api.telegram.org/file/bot{self.bot_token}/{file.file_path}"
        file_content = requests.get(file_url).content

        return file_content