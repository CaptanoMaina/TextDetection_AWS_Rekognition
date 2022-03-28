"""

Author Margaret Maina-s1906597.

This script:

  • checks if a table stratying with 'TEXT' exists
  • creates a table called TEXT-s1906597-table if it does not exist


"""

# import required resources
import boto3

# creates resource for dynamoDB
dynamodb = boto3.client("dynamodb",  aws_access_key_id="ASIA6ELGL3SC7XVXFXG2",
                        aws_secret_access_key="2jiFd2278edE24YLB4weYMj0VpFVPK/SvFal3AHL",
                        aws_session_token="FwoGZXIvYXdzEDYaDBg+gu6s3UEb+gQmZSLHAa8ytgjrnKPi7Cu9oG5NHi9+u3Vsecvic+FLWvS6IvgivAdKsnP9MdXo8lqXPhbQKFB+TFdLX3F7DKsm+v2Z4S8lRczL1ZC4NSUkN1s2vWveiehX5aKVYlltxuzE93awkOH9QmIrK/J1NmA2G7hz1InuvGgcVaS63MU3M3At1hJ3b3Z9QuzhASRJjAr7voJIieRPkd7mqpaG5LHdC7upEhMMlv5WaMjTuY/Lk28s/8Bd6l5kynO2jqwEyzrNZxmTH5+kR1BPobsoy4+DkgYyLd81wP6Si2wlGQ6PZD69sKM+FRtakx0hAsyk+dUWDcVcyFS8Pi50ulazkBipwQ==", region_name="us-west-2")

# retrieve a list of tables starting with 'TEXT'
# creates a new table called TEXT-s1906597-table if it does not exist

table_check = dynamodb.list_tables(ExclusiveStartTableName="TEXT", Limit=10)

table_name = table_check["TableNames"]


# KeySchema Specifies the attributes that make up the primary key for a table or an index
# AttributeDefinitions specifies the  data type e.g, Strings, Numbers, Booleans, etc.
# ProvisionedThroughput is where the capacity for reading/writing is set for the dynamoDB table


if len(table_name) == 0 or table_name != ["TEXT-s1906597-table"]:
    table = dynamodb.create_table(
        TableName="TEXT-s1906597-table",
        KeySchema=[{"AttributeName": "Image_Name", "KeyType": "HASH"},
                   {"AttributeName": "id", "KeyType": "RANGE", }],
        AttributeDefinitions=[
            {"AttributeName": "Image_Name", "AttributeType": "S"},
            {"AttributeName": "id", "AttributeType": "S"},
        ],
        ProvisionedThroughput={
            "ReadCapacityUnits": 10, "WriteCapacityUnits": 10},
    )
    print(
        "\n\033[96m"
        + "... dynamoDB table 'TEXT-s1906597-table' HAS BEEN CREATED SUCCESSFULLY\n"
        + "\033[0m"
    )


else:
    print(
        "\n\033[93m"
        + " ••• TABLE WITH NAME: "
        + str(table_name)
        + " ALREADY EXISTS"
        + "\n"
        + "\033[0m"
    )
