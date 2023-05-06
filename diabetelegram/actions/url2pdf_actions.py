import logging
import os
import re
from urllib.parse import urlparse, urlunparse

from diabetelegram.actions.base_action import BaseAction

logger = logging.getLogger()
logger.setLevel(logging.INFO)


class Url2PdfAction(BaseAction):
    # Matches messages starting with 'http://' or 'https://'
    URL_REGEX = r"^(https?://).*"

    def matches(self):
        return bool(re.match(self.URL_REGEX, self.message_text.lower()))

    def handle(self):
        url2pdf_endpoint = os.environ['URL2PDF_ENDPOINT']
        requested_url = self.message_text
        parsed = urlparse(requested_url)

        url = urlunparse(
            parsed._replace(
                scheme='https',
                netloc=url2pdf_endpoint,
                path='',
                params='',
                query='url=' + parsed.netloc + parsed.path
            )
        )

        # We can use a URL with send_document, and Telegram will get the file and
        # send it automatically
        self.telegram.send_document(self.message, url)
