import requests

from diabetelegram.services.base_web_client import BaseWebClient
from diabetelegram.serializers.meal_serializer import MealSerializer


class MealWebClient(BaseWebClient):
    """Handles interactions with the Meal resource of the diabetes API"""

    def create_meal(self, meal):
        """Send the request to store data of a new meal"""
        body = {'meal': MealSerializer(meal).to_dict()}

        response = requests.post(self._base_url(), headers=self._build_headers(), json=body)

        return self._handle_response(response)

    def edit_meal(self, meal_id, new_meal_data):
        """Edits the meal with the specified id"""
        url = f"{self._base_url()}/{meal_id}"
        body = {'meal': MealSerializer(new_meal_data).to_dict()}

        response = requests.patch(url, headers=self._build_headers(), json=body)

        return self._handle_response(response)

    def delete_meal(self, meal_id):
        """Send the request to delete the meal associated with the specified id"""
        url = f"{self._base_url()}/{meal_id}"

        response = requests.delete(url, headers=self._build_headers())

        return self._handle_response(response)

    def search_meal(self, search_term):
        params = {'q': search_term}

        response = requests.get(self._base_url(), params=params, headers=self._build_headers())

        return self._handle_response(response)

    def _base_url(self):
        return f"{self.API_URL}/meals"

    def _handle_response(self, response):
        if response.status_code in range(200, 300):
            response_msg = f"CODE: {response.status_code}\n"

            if response.text:
                response_data = response.json()['data']

                if type(response_data) == list:
                    response_msg += self._format_meals(response_data)
                else:
                    response_msg += self._format_meal(response_data)
            return response_msg

        else:
            return str(response.status_code)

    def _format_meals(self, meals_data):
        meals_info = [self._format_meal(meal_data) for meal_data in meals_data]
        meals_separator = "\n-----------------\n"

        return meals_separator.join(meals_info)

    def _format_meal(self, meal_data):
        info_separator = "\n"
        info_title = "Meal:"

        meal_info = [self._format_item(key, value) for key, value in meal_data.items()]
        meal_info.insert(0, info_title)

        return info_separator.join(meal_info)
