from datetime import datetime

from diabetelegram.actions.base_action import BaseAction
from diabetelegram.commands.aws_commands import PutFileInS3Command
from diabetelegram.services.telegram import TelegramWrapper


class DexcomAction(BaseAction):
    MESSAGE_UPLOADING_FILE = 'Uploading file...'
    MESSAGE_FILE_UPLOADED = 'File uploaded!'

    FILENAME_PREFIX = 'cgm-data'

    S3_BUCKET = 'alexgascon-api-files'
    S3_PATH_PREFIX = 'dexcom'

    def matches(self):
        return self.message_has_file() and self.is_csv_file()

    def handle(self):
        self.telegram.reply(self.message, self.MESSAGE_UPLOADING_FILE)

        file_name = self._filename()
        file_content = self.telegram.get_file(self.message)
        self._upload_file(file_name, file_content)

        self.telegram.reply(self.message, self.MESSAGE_FILE_UPLOADED)
        self.state_manager.set('initial')

    def message_has_file(self):
        return 'document' in self.message

    def is_csv_file(self):
        document = self.message['document']
        return document['mime_type'] == 'text/csv'

    def _filename(self):
        formatted_time = datetime.utcnow().isoformat()
        file_name = f'{self.FILENAME_PREFIX}_{formatted_time}.csv'
        return file_name

    def _upload_file(self, file_name, file_content):
        full_filename = f"{self.S3_PATH_PREFIX}/{file_name}"
        PutFileInS3Command(full_filename, file_content, self.S3_BUCKET).execute()
