from diabetelegram.services.telegram import TelegramWrapper


class PingCommand:
    """Responds to a message with 'pong'. Useful to check if the bot is working"""
    @staticmethod
    def handle(message):
        telegram = TelegramWrapper()
        telegram.reply(message, 'pong')
