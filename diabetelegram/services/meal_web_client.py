import json
import logging
import os

import requests

from diabetelegram.serializers.meal_serializer import MealSerializer


class MealWebClient:
    """Handles interactions with the Diabetes API"""
    API_URL = os.environ['DIABETES_API_URL']
    API_TOKEN = os.environ['DIABETES_API_TOKEN']

    def create_meal(self, meal):
        """Send the request to store data of a new meal"""
        url = self.API_URL
        headers = {'api_key': self.API_TOKEN}
        body = {'meal': MealSerializer(meal).to_dict()}

        response = requests.post(url, headers=headers, json=body)

        return self._handle_response(response)

    def _handle_response(self, response):
        if response.status_code == 201:
            return str(response.json())
        else:
            return str(response.status_code)
