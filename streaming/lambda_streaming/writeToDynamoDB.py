# Trigger connected to this lambdafunion is kinesis called apidata2
# This functio is to create raws in two tables in DynamoDB

import json
import base64
import boto3


def lambda_handler(event, context):

    client = boto3.client('dynamodb')

    for record in event['Records']:
        print(record)
        # Kinesis data is base64 encoded so decode here
        t_record = base64.b64decode(record['kinesis']['data'])

        # decode the bytes into a string
        str_record = str(t_record, 'utf-8')

        # transform the json string into a dictionary
        dict_record = json.loads(str_record)

        # create Customer Row (Partition key: CustomerID/ Sort key: InvoiceNo)
        ############################
        customer_key = dict()
        customer_key.update(
            {'CustomerID': {"S": str(dict_record['CustomerID'])}})  # Partition key
        customer_key.update(
            {'InvoiceNo': {"S": str(dict_record['InvoiceNo'])}})  # Sort key

        attributes_customer = dict()
        attributes_customer.update(
            {'StockCode': {'Value': {"S": str(dict_record['StockCode'])}, "Action": "PUT"}})
        attributes_customer.update(
            {'Description': {'Value': {"S": str(dict_record['Description'])}, "Action": "PUT"}})
        attributes_customer.update(
            {'Quantity': {'Value': {"N": str(dict_record['Quantity'])}, "Action": "PUT"}})
        attributes_customer.update(
            {'InvoiceDate': {'Value': {"S": str(dict_record['InvoiceDate'])}, "Action": "PUT"}})
        attributes_customer.update(
            {'UnitPrice': {'Value': {"N": str(dict_record['UnitPrice'])}, "Action": "PUT"}})
        attributes_customer.update(
            {'Country': {'Value': {"S": str(dict_record['Country'])}, "Action": "PUT"}})

        response = client.update_item(
            TableName='test-customer', Key=customer_key, AttributeUpdates=attributes_customer)

        # Create Invoice Row
        #############################

        invoice_key = dict()
        invoice_key.update(
            {'InvoiceNo': {"S": str(dict_record['InvoiceNo'])}})  # Primary key
        invoice_key.update(
            {'StockCode': {"S": str(dict_record['StockCode'])}})  # Sort key

        attributes_invoice = dict()
        attributes_invoice.update(
            {'Description': {'Value': {"S": str(dict_record['Description'])}, "Action": "PUT"}})
        attributes_invoice.update(
            {'Quantity': {'Value': {"N": str(dict_record['Quantity'])}, "Action": "PUT"}})
        attributes_invoice.update(
            {'InvoiceDate': {'Value': {"S": str(dict_record['InvoiceDate'])}, "Action": "PUT"}})
        attributes_invoice.update(
            {'UnitPrice': {'Value': {"N": str(dict_record['UnitPrice'])}, "Action": "PUT"}})
        attributes_invoice.update(
            {'Country': {'Value': {"S": str(dict_record['Country'])}, "Action": "PUT"}})

        response = client.update_item(
            TableName='test-invoice', Key=invoice_key, AttributeUpdates=attributes_invoice)

    return 'Successfully processed {} records.'.format(len(event['Records']))
