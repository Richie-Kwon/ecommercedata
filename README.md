# Creating data-pipelines with Ecommerce Data 

## Introduction
The main goal is to create data pipelines to analyse ecommerce data

* Establishing data pipe-lines in AWS to analyse e-commerce data with business analytics tools 
* Two main processes: Streaming & Batcth process 
* Python3 used in AWS lambda functions 
*  <span fontsize=10em;>cardinals</span>

## Contents
* [Dataset](#Dataset)
* [Tools](#Tools)
* [Streaming process](#Streamingprocess)
* [Batch process](#Batchprocess)
* [Conclusion](#Conclustion)

## Dataset <a name="Dataset"></a>
ecommerce data 

* Data Source: [UCI machine learning repository](http://archive.ics.uci.edu/ml/index.php)
* Overview of dataset: 8 Columns and 541909 rows in CSV
![image](https://user-images.githubusercontent.com/56697877/118081985-4ea73c00-b3b4-11eb-80b4-40c5a9ee87dc.png)

* Column list


 Column | Description
 --- | ---
 InvoiceNO | ‣  Object type <br /> ‣  6 digits and unique value for each transaction <br /> ‣  Cancellation (Prefix 'c') and bad debt(Prefix 'A') won't be used |
 StockCode | ‣  Object type <br /> ‣  Number or combination of alphabet and number
 Description | ‣  Object type <br /> ‣  1454 null vallues included |
 Quantity | ‣  Quantity of items per transaction <br /> ‣  Int64 <br /> ‣  Less than 0 in case of cacellantion and bad debt <br /> ‣  Cacellantion and bad debt will be filterd out in the the lambda function ([test](https://github.com/Richie-Kwon/ecommercedata/blob/main/1.%20streaming/lambda_streaming/test.py))|
 InvoiceDate | ‣ date and time when each transaction was made <br /> ‣  Object type <br /> ‣  Data type will be changed to datetime in the lambda function ([writeToS3](https://github.com/Richie-Kwon/ecommercedata/blob/main/1.%20streaming/lambda_streaming/writeToS3.py)) |
 UnitPrice | ‣ Unit price in sterling <br /> ‣  float64|
 CustomerID | ‣ Uniquely assigned to each customer <br /> ‣  float64 <br /> ‣ 135080 null values included; null values will be replaced with "Unknown" in the lambda function ([test-cleaning](https://github.com/Richie-Kwon/ecommercedata/blob/main/1.%20streaming/lambda_streaming/test-cleaning.py)) |
 Country | ‣  Name of the country where customers reside   <br /> ‣ Object type |
 
## Tools <a name="Tools"></a>
* 

## Streaming process <a name="Streamingprocess"></a>
* Description <br /> 
 ‣ Constantly pulling Raw data in CSV into the pipe lines <br /> 
 ‣ Transformed data can be stored in the storage such as S3, redshift and DynamoDB <br /> 
 ‣ The data in the storage can be connected to Business analytics tools such as Tableau, Athena and Jupyternote book <br /> 
 ‣ A customer can send a query to check transacion data in DynamoDB with API and primary key (InvoiceNO & Stockcode) <br /> 

* The layout of the streaming process
![image](https://user-images.githubusercontent.com/56697877/118083663-34229200-b3b7-11eb-89ac-887a84044a3f.png)

* Sub-process

* AWS Cognito <br />
For security, AWS congnito can be used to access API gateway with a token in this streaming process([Cognito](https://github.com/Richie-Kwon/ecommercedata/tree/main/3.%20cognito))

## Batch process <a name="Batchprocess"></a>
* Description <br /> 
 ‣ Import bulky raw data into the pipe lines <br />
 ‣ Transformed data can be stored in the storage such as S3 and redshift <br />
 ‣ The data in the storage can be connected to Business analytics tools such as EMR & Zeppline and PowerBI <br />

* The layout of the batch process
![image](https://user-images.githubusercontent.com/56697877/118084976-81076800-b3b9-11eb-9ba5-87dc49c87d0a.png)

* Sub-process￼￼

## Conclusion <a name="Conclustion"></a>




