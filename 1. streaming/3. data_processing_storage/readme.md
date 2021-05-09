# Create and Update S3

1. Create S3 bucket in AWS
2. Create a Lambda function and put down the Lambda code in writeToS3.py to store new data in the S3
3. Give the Lambda roles to read kinesis and write data in S3

# Create and Update DynamoDB

1. Create Dynamo DB (two tables)
   1. test-customer table
   - Keys: Partition key - CustomerID (String), Sort Key - InvoiceNo (String)
   - Columns: Country, Description, InvoiceDate, Quantity, Stockcode, UnitPrice
   2. test-invoice table
   - Keys: Partition key - InvoiceNo (String), Sort Key - StockCode (String)
   - Columns: Country, Description, InvoiceDate, Quantity, UnitPrice
2. Create a Lambda function and put down the Lambda code in writeToDynamoDB.py to store new data in the DynamoDB
3. IAM role: Read in kinesis and Write data in DynamoDB

# Create and Update Redshift

1. Create Redshift

   - Create a cluster
   - Check inbound rules in security group : Type - All TCP, Protocol - TCP, Port range - 0-65535, Source-IP address for your region to aceess to Redshift(docs.aws.amazon.com/firehose/latest/dev/controlling-access.html)
   - Make Publicly accessible "enabled" in properties
   - Create a table in the cluster by seding query in editor: refer to creating_table.txt
   - IAM role: Read in S3

2. Create S3 bucket (Intermediate storage)

   - Upload jsonpaths.json (to map or detect json string object)

3. Create KinesisFirehose and create connections to the Redshift
   - Create a delivery stream
   - Source: Kinesis Data stream
   - Destination: Redshift (Put down info. about the cluster)
   - Intermediate S3 destination: Choose the S3 buecket for intermediate storage
   - COPY command: refer to copy command.txt
   - IAM role: Read Kinesis and Write S3
