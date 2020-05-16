import boto3


class PutFileInS3Command:
    def __init__(self, filename, content, bucket):
        self.filename = filename
        self.content = content
        self.bucket = bucket
        self.s3 = boto3.client('s3')

    def execute(self):
        self.s3.put_object(Key=self.filename, Body=self.content, Bucket=self.bucket)