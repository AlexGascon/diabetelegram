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
        body = {'meal': MealSerializer(meal).to_dict()}

        response = requests.post(url, headers=self._build_headers(), json=body)

        return self._handle_response(response)

    def edit_meal(self, meal_id, new_meal_data):
        """Edits the meal with the specified id"""
        url = f"{self.API_URL}/{meal_id}"
        body = {'meal': MealSerializer(new_meal_data).to_dict()}

        response = requests.patch(url, headers=self._build_headers(), json=body)

        return self._handle_response(response)

    def delete_meal(self, meal_id):
        """Send the request to delete the meal associated with the specified id"""
        url = f"{self.API_URL}/{meal_id}"

        response = requests.delete(url, headers=self._build_headers())

        return self._handle_response(response)


    def _build_headers(self):
        return {'apikey': self.API_TOKEN}

    def _handle_response(self, response):
        if response.status_code in range(200, 300):
            response_msg = f"CODE: {response.status_code}\n"
            if response.text:
                response_msg += f"\nMeal:\n{self._format_response_body(response.json())}"

            return response_msg
        else:
            return str(response.status_code)

    def _format_response_body(self, response_body):
        message = ""
        for key, value in response_body['data'].items():
            message += f"{key.replace('_', ' ').capitalize()}: {value}\n"

        return message
