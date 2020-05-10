import json
import os
import pytest
from collections import defaultdict

from diabetelegram.handler import handler


class TestHandlerSmoke:
    """
    Class to verify that the most common types of messages can be handled.
    We don't want to assert any specific behavior, only that there aren't
    exceptions on the process.
    """

    def test_text_message(self):
        event = self._load_event('tests/fixtures/aws/lambda/text_event.json')
        context = {}

        handler(event, context)

    def test_command_message(self):
        event = self._load_event('tests/fixtures/aws/lambda/command_event.json')
        context = {}

        handler(event, context)


    def _load_event(self, event_file):
        return json.loads(open(event_file).read())