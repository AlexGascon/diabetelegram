import boto3
import moto
import pytest

from diabetelegram.commands.aws_commands import PutFileInS3Command


class TestPutFileInS3Command:
    @pytest.fixture(autouse=True)
    def setup(self, s3):
        self.filename = 'filename.txt'
        self.content = 'This is the content inside of the file'
        self.bucket = 'my-bucket-name'
        self.s3 = s3
        self.s3.create_bucket(Bucket=self.bucket, CreateBucketConfiguration={'LocationConstraint': 'eu-west-1'})

    def test_it_uploads_the_file_to_s3(self):
        assert self._s3_bucket_is_empty()

        command = PutFileInS3Command(self.filename, self.content, self.bucket)
        command.execute()

        assert self._file_exists_in_s3()

    def _s3_bucket_is_empty(self):
        response = self.s3.list_objects(Bucket=self.bucket)
        return 'Content' not in response

    def _file_exists_in_s3(self):
        response = self.s3.list_objects(Bucket=self.bucket, Prefix=self.filename)
        return len(response['Contents']) == 1
