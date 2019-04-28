import requests

from diabetelegram.serializers.injection_serializer import InjectionSerializer
from diabetelegram.services.base_web_client import BaseWebClient


class InjectionWebClient(BaseWebClient):
    def create_injection(self, injection):
        """Send the request to store data of a new injection"""
        body = {'injection': InjectionSerializer(injection).to_dict()}

        response = requests.post(self._base_url(), headers=self._build_headers(), json=body)

        return self._handle_response(response)

    def _base_url(self):
        return f"{self.API_URL}/injections"

    def _handle_response(self, response):
        if response.status_code in range(200, 300):
            response_msg = f"CODE: {response.status_code}\n"
            if response.text:
                response_msg += f"\nInjection:\n{self._format_response_body(response.json())}"

            return response_msg
        else:
            return str(response.status_code)