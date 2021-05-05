# Trigger connected to this lambdafunion is kinesis called apidata2
# It may be required to add a layer of aws wranlger in the lambda function to run this code
# This functio is to change data type and format and then store it in S3 called test-rawstorage

from __future__ import print_function
import base64
import json
import boto3
from datetime import datetime
import pandas as pd
import awswrangler as wr
import ast


s3_client = boto3.client('s3')

# Converting datetime object to string
dateTimeObj = datetime.now()

# format the string
timestampStr = dateTimeObj.strftime("%d-%b-%Y-%H%M%S")

# this is the list for the records
kinesisRecords = []


def lambda_handler(event, context):

    for record in event['Records']:
        # Kinesis data is base64 encoded so decode here
        payload = base64.b64decode(record['kinesis']['data']+"==")
        # append each record to a list
        kinesisRecords.append(payload)

    # changing the list into dataframe
    kinesisRecords_bytestr = kinesisRecords[0]
    kinesisRecords_dicstr = kinesisRecords_bytestr.decode(
        encoding="ISO-8859-1")

    mydata = json.loads(kinesisRecords_dicstr)
    df = pd.DataFrame([mydata])

    # changing to timestamp in InvoiceDate
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

    # creating a key
    mykey = 'output-' + timestampStr + '.parquet'

    # save the data in parquet with my key
    wr.s3.to_parquet(
        df=df,
        path='s3://test-rawstorage/rawdata/'+mykey
    )

    return 'Successfully processed {} records.'.format(len(event['Records']))
