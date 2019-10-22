import boto3

from os import getenv
from botocore.exceptions import NoCredentialsError

ACCESS_KEY = getenv('AWS_ACCESS_KEY_ID')
SECRET_KEY = getenv('AWS_SECRET_ACCESS_KEY')


def upload_to_aws(local_file, bucket, s3_file):
    s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY,
                      aws_secret_access_key=SECRET_KEY)
    bucket_location = boto3.client('s3', aws_access_key_id=ACCESS_KEY,
                      aws_secret_access_key=SECRET_KEY).get_bucket_location(Bucket='face-checking')
    object_url = "https://s3-{0}.amazonaws.com/{1}/{2}".format(
                    bucket_location['LocationConstraint'], bucket, s3_file)
    try:
        s3.upload_file(local_file, bucket, s3_file, ExtraArgs={'ACL':'public-read'})
        print("Upload Successful")
        return object_url
    except FileNotFoundError:
        print("The file was not found")
        return False
    except NoCredentialsError:
        print("Credentials not available")
        return False


uploaded = upload_to_aws('./img/groups/group-faces.jpg', 
        'face-checking', 'group-faces4.jpg')
print(uploaded)