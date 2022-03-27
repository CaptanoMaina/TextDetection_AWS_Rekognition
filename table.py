"""

Author Margaret Maina-s1906597.

This script:

  • checks if a table stratying with 'TEXT' exists
  • creates a table called TEXT-s1906597-table if it does not exist


"""

# import required resources
import boto3

# creates resource for dynamoDB
dynamodb = boto3.client("dynamodb",  aws_access_key_id="ASIA6ELGL3SCYT3TOMNI",
                        aws_secret_access_key="o8qvL+IPhQdVogrnqFoKlztBOrYLYcLSiGsUnNmg",
                        aws_session_token="FwoGZXIvYXdzEDEaDG8eIrF6sArdfJ/JBiLHATsA3446WwZt7FeodnIIRSUg8JOK+FB4Q4lC5RLKRoi9idwRjKx4u7dHPffprv2SjM4UOhql9OX2ggqq1a3T0qkFzWHnWlC0pA0DMppG0oGHYcNL+pgbyyNnXozuztTXJY2uVTjx0L5QN9L/BI2DZ6LU4jEWwEPArlKZgPOXOFj0F2AcS0pKkNZQra7z8vDkkbqFc975OBllk6Mi2Leip3AGYP3mMBjgOCmGSvNmnfVMQUAZhPVPa1wyC3WQrt0NOMDO3Y4mSOcotoKCkgYyLb/ZDdlB6f2+X/LxsckqRX68w4eFkPfd62dbdVcTk6DuJ9qGRyO0wcnHDQhQqA==", region_name="us-west-2")

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
