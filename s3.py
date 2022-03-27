"""

Author Margaret Maina-s1906597. 

This script 

  • Checks whether an S3 Bucket named '' exists
  • Checks whether the bucket has private or public access
  • Creates an S3 Bucket if one doesn't exist


"""

#import libraries
import boto3
import botocore

# create s3 resource
s3 = boto3.resource("s3",
                    aws_access_key_id="ASIA6ELGL3SCYT3TOMNI",
                    aws_secret_access_key="o8qvL+IPhQdVogrnqFoKlztBOrYLYcLSiGsUnNmg",
                    aws_session_token="FwoGZXIvYXdzEDEaDG8eIrF6sArdfJ/JBiLHATsA3446WwZt7FeodnIIRSUg8JOK+FB4Q4lC5RLKRoi9idwRjKx4u7dHPffprv2SjM4UOhql9OX2ggqq1a3T0qkFzWHnWlC0pA0DMppG0oGHYcNL+pgbyyNnXozuztTXJY2uVTjx0L5QN9L/BI2DZ6LU4jEWwEPArlKZgPOXOFj0F2AcS0pKkNZQra7z8vDkkbqFc975OBllk6Mi2Leip3AGYP3mMBjgOCmGSvNmnfVMQUAZhPVPa1wyC3WQrt0NOMDO3Y4mSOcotoKCkgYyLb/ZDdlB6f2+X/LxsckqRX68w4eFkPfd62dbdVcTk6DuJ9qGRyO0wcnHDQhQqA==")


# Declare bucket name
bucket_name = "s1906597-bucket"
bucket = s3.Bucket(bucket_name)

# check whether 's1906597-bucket' bucket exists
# checks whether its access is public or private, if it is private it throws a 403 error
# if the bucket is not available, it creates a new bucket


def check_bucket(bucket):
    try:
        s3.meta.client.head_bucket(Bucket=bucket_name)
        print(
            "\n\033[93m"
            + "... S3 BUCKET 's1906597-bucket' ALREADY EXISTS\n"
            + "\033[0m"
        )
        return True

    except botocore.exceptions.ClientError as e:
        error_code = int(e.response["Error"]["Code"])

        if error_code == 403:

            print(
                "\n\033[93m"
                + "... S3 BUCKET 's1906597-bucket' ALREADY EXISTS\n"
                + "\033[0m"
            )
            return True

        elif error_code == 404:

            s3.create_bucket(
                Bucket="s1906597-bucket",
                CreateBucketConfiguration={"LocationConstraint": "us-west-2"},
            )

            print(
                "\n\033[93m"
                + "... S3 BUCKET 's1906597-bucket' HAS BEEN CREATED SUCCESSFULLY\n"
                + "\033[0m"
            )

            return False


check_bucket(bucket)
