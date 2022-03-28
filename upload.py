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
                          aws_access_key_id="",
                          aws_secret_access_key="",
                          aws_session_token="")

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
