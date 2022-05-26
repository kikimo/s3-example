import pdb
import boto3
from botocore.client import Config

s3 = boto3.resource('s3',
                    endpoint_url='http://192.168.15.12:9000',
                    aws_access_key_id='minioadmin',
                    aws_secret_access_key='minioadmin',
                    config=Config(signature_version='s3v4'),
                    )

bkt = s3.Bucket('tbkt')
# pdb.set_trace()
for obj in bkt.objects.all():
    print(obj)


# pdb.set_trace()
# print(bkt)
# print(s3.Bucket('tbkt').list_files())
