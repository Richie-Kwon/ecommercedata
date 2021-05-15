## Data Cleaning and changing format 
Create a new lambda fuction in AWS which can play a role of cleaning or formatiing data in AWS 
- Null values changed to unknown in CustomerID: [test-cleaning](https://github.com/Richie-Kwon/ecommercedata/blob/main/1.%20streaming/lambda_streaming/test-cleaning.py) 
- Changing type to Parquet and timestamp: (InvoiceDate): [writeToS3](https://github.com/Richie-Kwon/ecommercedata/blob/main/1.%20streaming/lambda_streaming/writeToS3.py) 
- Data nomalisation can be done if necessary for preidictive analysis or machine learning




