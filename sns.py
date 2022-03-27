"""

Author Margaret Maina-s1906597.

This script:

  • creates an sns topic


"""

# import necessarry resources
import boto3
from botocore.exceptions import ClientError


client = boto3.client('sns',  aws_access_key_id="ASIA6ELGL3SCYT3TOMNI",
                      aws_secret_access_key="o8qvL+IPhQdVogrnqFoKlztBOrYLYcLSiGsUnNmg",
                      aws_session_token="FwoGZXIvYXdzEDEaDG8eIrF6sArdfJ/JBiLHATsA3446WwZt7FeodnIIRSUg8JOK+FB4Q4lC5RLKRoi9idwRjKx4u7dHPffprv2SjM4UOhql9OX2ggqq1a3T0qkFzWHnWlC0pA0DMppG0oGHYcNL+pgbyyNnXozuztTXJY2uVTjx0L5QN9L/BI2DZ6LU4jEWwEPArlKZgPOXOFj0F2AcS0pKkNZQra7z8vDkkbqFc975OBllk6Mi2Leip3AGYP3mMBjgOCmGSvNmnfVMQUAZhPVPa1wyC3WQrt0NOMDO3Y4mSOcotoKCkgYyLb/ZDdlB6f2+X/LxsckqRX68w4eFkPfd62dbdVcTk6DuJ9qGRyO0wcnHDQhQqA==", region_name="us-west-2")


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
