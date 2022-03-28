"""

Author Margaret Maina-s1906597.

This script:

  • creates an sns topic


"""

# import necessarry resources
import boto3
from botocore.exceptions import ClientError


client = boto3.client('sns',  aws_access_key_id="",
                      aws_secret_access_key="",
                      aws_session_token="")


def create_sns(topic_name):
    try:
        client.create_topic(Name=topic_name)
        print(
            "\n\033[96m"
            + "... SNS topic 's1906597-topic' HAS BEEN CREATED SUCCESSFULLY\n"
            + "\033[0m"
        )

    except ClientError as e:
        print(e)


create_sns('s1906597topic')
