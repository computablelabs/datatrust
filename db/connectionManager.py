"""
Class to manage DynamoDB connection
"""

import boto3
from botocore.exceptions import ClientError

class ConnectionManager:

    def __init__(self, db_url, local, table_name):
        self.db = boto3.resource('dynamodb', endpoint_url=db_url)
        self.table_name = table_name

        if local:
            # If running locally, create the table if needed. 
            # Staging/Prod should not create tables automatically
            self.setup_local_db(table_name)

    def setup_local_db(self, table_name):
        """
        Create the local instance table if it doesn't exist
        """
        try:
            print('Setting up local db')
            table = self.db.create_table(
                    TableName=table_name,
                    KeySchema=[
                        {
                            'AttributeName': 'listing',
                            'KeyType': 'HASH'
                        }
                    ],
                    AttributeDefinitions=[
                        {
                            'AttributeName': 'listing',
                            'AttributeType': 'S'
                        }
                    ],
                    ProvisionedThroughput={
                        'ReadCapacityUnits': 10,
                        'WriteCapacityUnits': 10
                    }
                )
        except ClientError as riu:
            if riu.response['Error']['Code'] == 'ResourceInUseException':
                print('Table already created, moving on...')

    def add_listing(self, payload):
        """
        Add a listing to the table
        """
        try:
            table = self.db.Table(self.table_name)
            response = table.put_item(
                Item=payload
            )
            if response['ResponseMetadata']['HTTPStatusCode'] == 200:
                return 'Success'
            else:
                return 'Error writing to database'
        except ClientError as exc:
            if exc.response['Error']['Code'] == 'ValidationException':
                return 'ValidationException'
                # TODO: Add 'data' array to db schema
