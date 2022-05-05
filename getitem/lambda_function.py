import json
import boto3
from botocore.config import config

dynamodb=boto3.resource('dynamodb')
table=dynamodb.Table('Users')

def lambda_handler(event, context):
    response = table.get_item(
        key={
            'id':'12345'
            
        }
        )
    print(response)
    return{
        'statusCode':200,
        'body':response
    }
    
