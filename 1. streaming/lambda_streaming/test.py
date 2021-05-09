# Triggers connected to this lambdafunion are API gateways for GET and POST methods

import json
import boto3


def lambda_handler(event, context):

    print("MyEvent:")
    print(event)

    method = event['context']['http-method']

    if method == "GET":
        # TODO: write code...
        dynamo_client = boto3.client('dynamodb')

        # Partition key - InvoiceNo
        im_InvoiceNo = event['params']['querystring']['InvoiceNo']
        print(im_InvoiceNo)

        # Sort key - StockCode
        im_StockCode = event['params']['querystring']['StockCode']

        # Primary key
        primary_key = dict()
        # Updating Partition key
        primary_key.update({'InvoiceNo': {"S": im_InvoiceNo}})
        # Updating Sort Key
        primary_key.update({'StockCode': {"S": im_StockCode}})

        response = dynamo_client.get_item(
            TableName='test-invoice', Key=primary_key)
        print(response['Item'])

        #myreturn = "This is the return of the get"

        return {
            'statusCode': 200,
            'body': json.dumps(response['Item'])
        }

    elif method == "POST":

        # mystring = event['params']['querystring']['param1']
        p_record = event['body-json']
        recordstring = json.dumps(p_record)

        # ignore the data in case either Quantity or unitprice is less than zero
        recordstring_dic = json.loads(recordstring)
        if recordstring_dic['Quantity'] > 0 and recordstring_dic['UnitPrice'] > 0:
            recordstring_validated = json.dumps(recordstring_dic)

        client = boto3.client('kinesis')
        response = client.put_record(
            StreamName='APIdata',
            Data=recordstring_validated,
            PartitionKey='string'
        )

        return {
            'statusCode': 200,
            'body': json.dumps(p_record)
        }
    else:
        return {
            'statusCode': 501,
            'body': json.dumps("Server Error")
        }
