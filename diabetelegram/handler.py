import json
import logging
import os
import traceback

from diabetelegram.commands.command_router import CommandRouter
from diabetelegram.services.telegram import TelegramWrapper


logger = logging.getLogger()
logger.setLevel(logging.INFO)

def handler(event, context):
    try:
        logger.info(json.dumps(event))

        telegram = TelegramWrapper()
        message = telegram.extract_message(_event_body(event))

        if message['text'].startswith('/'):
            CommandRouter.dispatch(message)

    except Exception as e:
        logger.error(f"ERROR MESSAGE: {e}")
        logger.error(traceback.print_exception(e))

    finally:
        # Making sure to notify Telegram Webhook that we received the update
        # Otherwise it will retry until we give them a successful response
        return {"statusCode": 200}


def _event_body(event):
    return json.loads(event['body'])
