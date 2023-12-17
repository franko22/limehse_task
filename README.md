# limehse_task
## I choose Boto3 for AWS environment automation enabling minimal manual s3 routine tasks as I-a-C, hence saving valuable time and resources for this use case below.
## Use case
### - listing specific file type (*.txt) from an s3 Bucket

### Before you run this script**(IT'S ASSUMED YOU HAVE AWS CLI CONFIGURED ON YOUR REMOTE MACHINE)**, you also need to have Boto3 installed and Pyhton3, if not installed follow these steps below to install Boto3 module on Mac
### - upgrade pip installation (optional)
### installation cmd
### - pip install Boto3
### Verifying that Boto3 is installed
### - pip show boto3 
### below is response output
_Name: boto3
Version: 1.34.2
Summary: The AWS SDK for Python
Home-page: https://github.com/boto/boto3
Author: Amazon Web Services
Author-email: 
License: Apache License 2.0
Location: /usr/local/lib/python3.9/site-packages
Requires: botocore, jmespath, s3transfer_

### To run from your remote machine
#### After verifying installations of pyhon, awscli, AWS Credentials and Boto3 is complete with AWS config file, git clone repo and navigate to infra directory and enter this the terminal 
#### _python search.py