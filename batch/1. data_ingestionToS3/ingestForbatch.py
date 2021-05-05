import json
import pandas as pd
import boto3
from datetime import datetime
import awswrangler as wr


def lambda_handler(event, context):
    # setup bucket and file name
    bucket_name = "bucket-batchprocess"
    file_name = "testdata-batch.json"

    # make a connection to s3
    s3 = boto3.client('s3')
    obj = s3.get_object(Bucket=bucket_name, Key=file_name)

    # make a dataFrame with pandas
    df = initial_df = pd.read_json(obj['Body'])
    #print (df.head(3))

    # filter data: both quantity and unitprice are more than 0
    filtered_df = df[(df['Quantity'] > 0) & (df['UnitPrice'] > 0)]

    # mark 'unknown' if customerIF is null
    filtered_df["CustomerID"].fillna("Unknown", inplace=True)

    # change to datetype
    filtered_df['InvoiceDate'] = pd.to_datetime(filtered_df['InvoiceDate'])

    # Converting datetime object to string
    dateTimeObj = datetime.now()

    # format the string
    timestampStr = dateTimeObj.strftime("%d-%b-%Y-%H%M%S")

    # create a file name in parquet
    mykey = 'output-' + timestampStr + '.parquet'

    # save a parquet file in s3 called 'bucket-rawstorage'
    wr.s3.to_parquet(
        df=filtered_df,
        path='s3://bucket-rawstorage/rawdata/'+mykey
    )

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
