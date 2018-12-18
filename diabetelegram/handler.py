import json
import logging
import os

from diabetelegram.commands.command_router import CommandRouter
from diabetelegram.services.telegram import TelegramWrapper


logger = logging.getLogger()
logger.setLevel(logging.INFO)

def handler(event, context):
    logger.info(json.dumps(event))

    payload = _event_body(event)

    telegram = TelegramWrapper()
    message = telegram.extract_message(payload)

    if message['text'].startswith('/'):
        CommandRouter.dispatch(message)

    return {"statusCode": 200, "body": "Received"}


def _event_body(event):
    return json.loads(event['body'])
