# Creating data-pipelines with Ecommerce Data 

## Introduction
The main goal is to create data pipelines to analyse ecommerce data

* Establish data pipelines in AWS to analyse e-commerce data with business analytics tools 
* The data pipielines cover streaming & batcth process 
* Python3 used in AWS lambda functions to process data 

## Contents
* [Dataset](#Dataset)
* [Tools](#Tools)
* [Streaming process](#Streamingprocess)
* [Batch process](#Batchprocess)
* [Conclusion](#Conclustion)

## Dataset <a name="Dataset"></a>
ecommerce data 

* Data Source: [UCI machine learning repository](http://archive.ics.uci.edu/ml/index.php)
* Overview of dataset - 8 Columns and 541909 rows in CSV
![image](https://user-images.githubusercontent.com/56697877/118081985-4ea73c00-b3b4-11eb-80b4-40c5a9ee87dc.png)

* Column list


 Column | Description
 --- | ---
 InvoiceNO | ‣ Uniquely assigned to each transaction <br /> ‣  Object type <br /> ‣  6 digits and unique value for each transaction <br /> ‣  Cancellation (Prefix 'c') and bad debt(Prefix 'A') won't be used: negative number |
 StockCode | ‣  Uniquely assigned to each item <br /> ‣ Object type <br /> ‣  Number or combination of alphabet and number
 Description | ‣ Features of each item <br /> ‣  Object type <br /> ‣  1454 null vallues included |
 Quantity | ‣  Quantity of items per transaction <br /> ‣  Int64 <br /> ‣  Less than 0 in case of cacellantion and bad debt <br /> ‣  Cacellantion and bad debt will be filterd out in the the lambda function ([test](https://github.com/Richie-Kwon/ecommercedata/blob/main/1.%20streaming/lambda_streaming/test.py))|
 InvoiceDate | ‣ Date and time when each transaction was made <br /> ‣  Object type <br /> ‣  Data type will be changed to datetime in the lambda function ([writeToS3](https://github.com/Richie-Kwon/ecommercedata/blob/main/1.%20streaming/lambda_streaming/writeToS3.py)) |
 UnitPrice | ‣ Unit price in sterling <br /> ‣  float64|
 CustomerID | ‣ Uniquely assigned to each customer <br /> ‣  float64 <br /> ‣ 135080 null values will be replaced with "Unknown" in the lambda function ([test-cleaning](https://github.com/Richie-Kwon/ecommercedata/blob/main/1.%20streaming/lambda_streaming/test-cleaning.py)) |
 Country | ‣  Name of the country where customers reside   <br /> ‣ Object type |
 
## Tools <a name="Tools"></a>

* Connect <br /> 
 ‣ API gateway: POST (to ingest data) & GET (to send query to DynamoDB) method <br /> 
 
* Buffer <br /> 
 ‣ AWS Kinesis(Data streams) <br /> 
 
* Processing <br /> 
 ‣ AWS Kinesis firehose(Delivery stream)  <br /> 
 ‣ AWS lambda functions <br /> 
 ‣ Python3 in lambda functions <br /> 
 ‣ AWS glue: Create datacatalog in the streaming process and carry out ETL between S3 and Redshift in the batch process

* Storage <br /> 
 ‣ S3: Store parquet data <br /> 
 ‣ Redshift: Store data and connect to Tableau or Power BI <br /> 
 ‣ DynamoDB: Store data with two tables (Customer & Invoice tables)  <br /> 
 
* BI analytics <br /> 
 ‣ Tableau: Connect to redshift <br /> 
 ‣ AWS Athena : Connect to S3 <br /> 
 ‣ Jupyter notebook : Connect to S3 <br /> 
 ‣ Zepplin notebook: Connect to EMR in batch process <br /> 


## Streaming process <a name="Streamingprocess"></a>
* Description <br /> 
 ‣ Constantly pulling Raw data in CSV into the pipe lines <br /> 
 ‣ Transformed data can be stored in the storage such as S3, redshift and DynamoDB <br /> 
 ‣ The data in the storage can be connected to Business analytics tools such as Tableau, Athena and Jupyternote book <br /> 
 ‣ A customer can send a query to check transacion data in DynamoDB with API and primary key (InvoiceNO & Stockcode) <br /> 

* The layout of the streaming process
![image](https://user-images.githubusercontent.com/56697877/118083663-34229200-b3b7-11eb-89ac-887a84044a3f.png)

* Sub-process <br />
 &ensp;1. [Data ingestion](https://github.com/Richie-Kwon/ecommercedata/tree/main/1.%20streaming/1.%20data_%20ingestion): Ingest data in CSV into AWS Kinesis through API gateway <br />
 &ensp;2. [Data cleaning](https://github.com/Richie-Kwon/ecommercedata/tree/main/1.%20streaming/2.%20data_cleaning): Clean data or change data type <br /> 
 &ensp;3. [Data processing & Storage](https://github.com/Richie-Kwon/ecommercedata/tree/main/1.%20streaming/3.%20data_processing_storage): Bring and send data from Kinesis to storage(S3 or Redshift) and process data <br /> 
 &ensp;4. [BI analytics](https://github.com/Richie-Kwon/ecommercedata/tree/main/1.%20streaming/4.%20BI%20analytics): Create connections to BI tools like Tableau and Athena and Send Queries to DynamoDB <br /> 

* AWS Cognito <br />
For security, AWS congnito can be used to access API gateway with a token in this streaming process([Cognito](https://github.com/Richie-Kwon/ecommercedata/tree/main/3.%20cognito))

## Batch process <a name="Batchprocess"></a>
* Description <br /> 
 ‣ Import bulky raw data into the pipe lines <br />
 ‣ Transformed data can be stored in the storage such as S3 and redshift <br />
 ‣ The data in the storage can be connected to Business analytics tools such as EMR & Zeppline and PowerBI <br />

* The layout of the batch process
![image](https://user-images.githubusercontent.com/56697877/118084976-81076800-b3b9-11eb-9ba5-87dc49c87d0a.png)




## Conclusion <a name="Conclustion"></a>

There are a few things to be improved in this pipelines
- Email notification (AWS SNS)can be applied to this pipelies to monitor updates in the stores
- Cognito set up can be complicated when the number of users goes up 




