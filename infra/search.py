import boto3
# for extra security to connection adding session token was required using aws sts assume-role, Boto3 is passing credentilas as params when creating Session Object.
session = boto3.Session( aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY, aws_session_token=AWS_SESSION_TOKEN)

s3 = session.resource('s3')

my_bucket = s3.Bucket('my-test-bucket')

for obj in my_bucket.objects.all():
    if obj.key.endswith('txt'):
        print(obj.key)
