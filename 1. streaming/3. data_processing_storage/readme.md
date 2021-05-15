## Create S3 bucket<br /> 
&ensp;&ensp; 1. Create S3 bucket in AWS<br />
&ensp;&ensp;![image](https://user-images.githubusercontent.com/56697877/118369671-2da13f80-b59c-11eb-9b4c-4370c2e2cc48.png)<br /><br /><br />
&ensp;&ensp; 2. Create a Lambda function and put down the Lambda code ([writeToS3](https://github.com/Richie-Kwon/ecommercedata/blob/main/1.%20streaming/lambda_streaming/writeToS3.py)) to store new data in the S3 <br /><br />
&ensp;&ensp; 3. Give the Lambda roles in IAM to read kinesis and write data in S3
&ensp;&ensp;![image](https://user-images.githubusercontent.com/56697877/118369815-cd5ecd80-b59c-11eb-8936-822378b9bcae.png)<br /><br />
&ensp;&ensp;4. Check the data stored<br />
&ensp;&ensp;![image](https://user-images.githubusercontent.com/56697877/118370614-44e22c00-b5a0-11eb-912f-63e0425a481d.png)<br /><br />


##  Create DynamoDB <br />
&ensp;&ensp;1. Create Dynamo DB (test-customer table)<br />
&ensp;&ensp;&ensp;- Keys: "Partition key - CustomerID (String)" and "Sort Key - InvoiceNo (String)"<br />
&ensp;&ensp;&ensp;- Columns: Country, Description, InvoiceDate, Quantity, Stockcode, UnitPrice <br /><br />
&ensp;&ensp;2. Create Dynamo DB (test-invoice table)<br />
&ensp;&ensp;&ensp;- Keys: "Partition key - InvoiceNo (String)" and "Sort Key - StockCode (String)"<br />
&ensp;&ensp;&ensp;- Columns: Country, Description, InvoiceDate, Quantity, UnitPrice <br />
&ensp;&ensp;&ensp;![image](https://user-images.githubusercontent.com/56697877/118370021-aa80e900-b59d-11eb-8262-6a9420b0545f.png)<br /><br /><br />
&ensp;&ensp;3. Create a Lambda function and put down the Lambda code ([writeToDynamoDB](https://github.com/Richie-Kwon/ecommercedata/blob/main/1.%20streaming/lambda_streaming/writeToDynamoDB.py)) to store new data in the DynamoDB <br /><br />
&ensp;&ensp;4. Give the Lambda roles in IAM to read kinesis and write data in DynamoDB <br /><br />
&ensp;&ensp;5. Check the data stored<br />
&ensp;&ensp;&ensp;![image](https://user-images.githubusercontent.com/56697877/118370472-bff71280-b59f-11eb-9d4a-bd5c8fb24789.png)<br /><br />

##  Create Redshift <br />
&ensp;&ensp;1. Create Redshift and configre things below<br />
&ensp;&ensp;&ensp;&ensp;- Change inbound rules in security group: <br />
&ensp;&ensp;&ensp;&ensp;‣ Type - All TCP, <br />
&ensp;&ensp;&ensp;&ensp;‣ Protocol - TCP, <br />
&ensp;&ensp;&ensp;&ensp;‣ Port range - 0-65535, <br />
&ensp;&ensp;&ensp;&ensp;‣ Source-IP address for your region to aceess to Redshift([AWS document](docs.aws.amazon.com/firehose/latest/dev/controlling-access.html)) <br />

&ensp;&ensp;&ensp;![image](https://user-images.githubusercontent.com/56697877/118371813-30089700-b5a6-11eb-9dcc-70beae3a3e75.png)<br /><br />

&ensp;&ensp;&ensp;- Make Publicly accessible "enabled" in properties <br />
&ensp;&ensp;&ensp;![image](https://user-images.githubusercontent.com/56697877/118371728-d4d6a480-b5a5-11eb-94f4-fcfc789e12d4.png)<br /><br />

&ensp;&ensp;&ensp;- Create a table in the cluster by seding query in editor <br />

```SQL
   create table firehosetransactions(
	InvoiceNo int, 
	StockCode varchar(200),
	Description varchar(200),
	Quantity int,	
	InvoiceDate varchar(200),
	UnitPrice float,
	CustomerID varchar(200),  	
 	Country varchar(200));
   ```
&ensp;&ensp;&ensp;- Give the Redshif roles in IAM to read/write data in S3 and read data in Kinesis <br /><br />
   
&ensp;&ensp;2. Create S3 bucket (Intermediate storage)<br />
&ensp;&ensp;&ensp;Upload jsonpaths.json (to map or detect json string object) in the S3 bucket


&ensp;&ensp;3. Create KinesisFirehose and connections to the Redshift<br />
&ensp;&ensp;&ensp;   - Create a delivery stream <br />
&ensp;&ensp;&ensp;- Configure things below <br />
&ensp;&ensp;&ensp;‣ Source: Kinesis Data stream <br />
&ensp;&ensp;&ensp;‣ Destination: Redshift (Put down info. about the cluster)<br />
&ensp;&ensp;&ensp;‣ Intermediate S3 destination: Choose the S3 buecket for intermediate storage<br />
&ensp;&ensp;&ensp;‣ COPY command: Copy & paste [copy command](https://github.com/Richie-Kwon/ecommercedata/blob/main/1.%20streaming/3.%20data_processing_storage/copycommand.txt)

