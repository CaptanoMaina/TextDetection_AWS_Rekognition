"""

Author Margaret Maina-s1906597. 

This script 

  • checks if there are Records in the responses; the responses are not empty
  • Extract the bucket name and the image name
  • Request AWS Rekognition text detection to anlyse images in the s3 bucket
  • extract text data
  • check for the word danger or hazard in the detected text
  • send an sms if any of these words are found



"""

# import required libraries
from email import message
import boto3
from botocore.exceptions import ClientError
import json

# create required resources
rekognition_client = boto3.client('rekognition')
sns_client = boto3.client('sns')
s3 = boto3.resource('s3')
table = boto3.resource('dynamodb').Table('TEXT-s1906597-table')

# detects texts


def detect_text(bucket, image):
    response = rekognition_client.detect_text(
        Image={'S3Object': {'Bucket': bucket, 'Name': image}})
    return response

# extracts relevant data from the response


def retrieve_data(response, image):
    for text in response['TextDetections']:
        id = text['Id']
        detected_text = text['DetectedText']
        confidence = text['Confidence']

        print(
            "\n\033[93m"
            + " Detected text is  "
            + detected_text
            + " with a confidence of "
            + str(confidence)
            + "in the detected item\n"
            + "\033[0m"

        )
        # exporting data to the TEXT-s1906597-table
        table.put_item(Item={
            'Image_Name': image,
            'id': str(id)+detected_text,
            'Text_Detected': detected_text,
            'Confidence': str(confidence)

        })

        # looping through the detected text fot danger and hazard
        # sending an sms if either words are found

        if detected_text == 'Danger' or detected_text == 'HAZARD':
            sns_client.publish(
                PhoneNumber='ZZ-ZZZZZZZZZZ',
                Message='The word' + detected_text + 'was detected in' + image,
                Subject='Important'
            )

# If there are Records in the responses; the responses are not empty
# Extract the bucket name and the image name
# Request AWS Rekognition text detection to anlyse images in the s3 bucket
# extract text data


def lambda_handler(event, context):
    print(event)
    message = event["Records"][0]["Sns"]["Message"]
    message = json.loads(message)
    bucket = message["Records"][0]["s3"]["bucket"]["name"]
    key = message["Records"][0]["s3"]["object"]["key"].replace("+", " ")

    try:
        response = detect_text(bucket, key)
        retrieve_data(response, key)
    except ClientError as e:
        print(e)
