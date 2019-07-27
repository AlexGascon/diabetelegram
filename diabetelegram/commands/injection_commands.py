import os

from diabetelegram.parsers.injection_parser import InjectionParser
from diabetelegram.services.injection_web_client import InjectionWebClient
from diabetelegram.services.injection_sns_client import InjectionSNSClient
from diabetelegram.services.telegram import TelegramWrapper


class NewInjectionCommand:
    """Connects with the diabetes API to store information about an injection

    It expects the message to have the following format:
    <command> <injection_info>
    """

    @staticmethod
    def handle(message):
        _, injection_info = message['text'].split(maxsplit=1)
        injection = InjectionParser(injection_info).to_injection()

        if os.environ['EVENT_ORIENTED_ON'] == 'true':
            result = InjectionSNSClient().insulin_injected(injection)
        else:
            result = InjectionWebClient().create_injection(injection)

        telegram = TelegramWrapper()
        telegram.reply(message, result)