## ecommerce-

Establishing data pipe lines for e-commerce data in AWS to 1) process transactions ad provde purcahse history (or summary) to customers and 2) to analyse the data for business analytics such as average sales, the most popular units, and total number of invoices

## Dataset
* [Data set - UCI machine learning repository](http://archive.ics.uci.edu/ml/index.php) : 8 Columns and 541909 rows

* Column list


 Column | Description
 --- | ---
 InvoiceNO | ‣  Object type <br /> ‣  6 digits and unique value for each transaction <br /> ‣  Cancellation (Prefix 'c') and bad debt(Prefix 'A') won't be used |
 StockCode | ‣  Object type <br /> ‣  Number or combination of alphabet and number
 Description | ‣  Object type <br /> ‣  1454 null vallues included |
 Quantity | ‣  Int64 <br /> ‣  Less than 0 in case of cacellantion and bad debt <br /> ‣  Callation and bad debt will be filterd out in data ingestion with the lambda function([test](https://github.com/Richie-Kwon/ecommercedata/blob/main/1.%20streaming/lambda_streaming/test.py))|
 InvoiceDate | ‣  Object <br /> ‣  Data type will be changed to datetime with the lambda function ([writeToS3](https://github.com/Richie-Kwon/ecommercedata/blob/main/1.%20streaming/lambda_streaming/writeToS3.py)) |
 UnitPrice | ‣  float64|
 CustomerID | ‣  float64 <br /> ‣ 135080 null values included <br /> ‣null values will be replaced with "Unknown" with the lambda function ([test-cleaning]_
 Country | ‣  Object type |
 
 * Shape of dataset
 ![image](https://user-images.githubusercontent.com/56697877/117875493-23c8c500-b29a-11eb-8c49-a4c6d6560ae1.png)

 
 
InvoiceNo       object  6digit ( prefix c means cancellation and prefix ad mens adjusting bad debt

StockCode       object

Description     object

Quantity         int64

InvoiceDate     object

UnitPrice      float64

CustomerID     float64 >> changed to String at the second lambda function

Country         object

Calleation and bad debt(Prefix 'c' means cancellation and Prefix 'A' means adjust bad debt) won't be used
  * InvoiceNO
    * 6 digit integer and unique value for each transaction
    * 
  * StockCode
  * Description
  * Quantity
  * InvoiceDate
  * UnitPrice
  * CustomerID
  * Country

* Data type


# Streaming process

The layout of the streaming process
![image](https://user-images.githubusercontent.com/56697877/116921770-606a4000-ac4c-11eb-98a9-9159b1d17ba6.png)

# Batch process

The layout of the batch process
￼![image](https://user-images.githubusercontent.com/56697877/117211277-b2e46180-adf0-11eb-9dfe-61f357dbbaca.png)

￼￼
