import os


class BaseWebClient:
    """Handles interactions with the Diabetes API"""
    API_URL = os.environ['DIABETES_API_URL']
    API_TOKEN = os.environ['DIABETES_API_TOKEN']

    def _build_headers(self):
        return {'apikey': self.API_TOKEN}

    def _format_response_body(self, response_body):
        message = ""
        for key, value in response_body['data'].items():
            message += self._format_item(key, value) + "\n"

        return message

    def _format_item(self, key, value):
        return f"{key.replace('_', ' ').capitalize()}: {value}"
