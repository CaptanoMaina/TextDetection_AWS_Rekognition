"""

Author Margaret Maina-s1906597.

This script:

  • finds the directory containing the image files
  • uploads files to s3 bucket every 10 seconds


"""

# import libraries
import boto3
import os
import time
from botocore.exceptions import ClientError
import glob

# Set directory path for files to be uploaded
# scan for files with the '.jpg' extension
dir_path = "./images/*"
main_dir = glob.glob(dir_path)

bucket_name = ("s1906597-bucket")

# upload all '.jpg' files to the s3 bucket 's1906597-bucket'
# this fuction loops through the main directory and uploads an image every 10 seconds


def upload_images(dir_path, bucket):
    for image in main_dir:
        # print(image)
        session = boto3.Session()
        s3 = boto3.client("s3",
                          aws_access_key_id="ASIA6ELGL3SCYT3TOMNI",
                          aws_secret_access_key="o8qvL+IPhQdVogrnqFoKlztBOrYLYcLSiGsUnNmg",
                          aws_session_token="FwoGZXIvYXdzEDEaDG8eIrF6sArdfJ/JBiLHATsA3446WwZt7FeodnIIRSUg8JOK+FB4Q4lC5RLKRoi9idwRjKx4u7dHPffprv2SjM4UOhql9OX2ggqq1a3T0qkFzWHnWlC0pA0DMppG0oGHYcNL+pgbyyNnXozuztTXJY2uVTjx0L5QN9L/BI2DZ6LU4jEWwEPArlKZgPOXOFj0F2AcS0pKkNZQra7z8vDkkbqFc975OBllk6Mi2Leip3AGYP3mMBjgOCmGSvNmnfVMQUAZhPVPa1wyC3WQrt0NOMDO3Y4mSOcotoKCkgYyLb/ZDdlB6f2+X/LxsckqRX68w4eFkPfd62dbdVcTk6DuJ9qGRyO0wcnHDQhQqA==")
        s3.upload_file(image, bucket, os.path.basename(image))
        print(
            "\n\033[93m"
            + "   "
            + image
            + "   "
            + "UPLOADED TO S3 BUCKET (s1906597-bucket) SUCCESSFULLY\n"
            + "\033[0m"

        )
        time.sleep(10)

    print("\n\033[96m" +
          " ••• FILES UPLOADED SUCCESSFULLY\n" + "\033[0m")


upload_images(main_dir, bucket_name)
