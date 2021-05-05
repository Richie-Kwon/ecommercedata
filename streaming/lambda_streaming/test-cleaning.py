# Trigger connected to this lambdafunion is kinesis called APIdata
# This lambda function is to change data type (or do normallisation) and forward the data to kinesis called apidata2

import json
import base64
import boto3
from datetime import datetime


def lambda_handler(event, context):

    record = event['Records']
    print(record)
    t_record = base64.b64decode(record[0]['kinesis']['data'])
    str_record = str(t_record, 'utf-8')
    dict_record = json.loads(str_record)

    # changing data type of CustomerID to string
    dict_record['CustomerID'] = str(dict_record['CustomerID'])

    # convert null values in costomerID to "unknown"
    if not dict_record['CustomerID']:
        dict_record['CustomerID'] = 'unknown'
    recordstring_preprocessing = json.dumps(dict_record)

    # unitprice or quantity can be normalized here (optional)

    client = boto3.client('kinesis')
    response = client.put_record(
        StreamName='apidata2',
        Data=recordstring_preprocessing,
        PartitionKey='string'
    )

    return {
        'statusCode': 200,
        'body': json.dumps('movingintoCleankinesis')
    }
