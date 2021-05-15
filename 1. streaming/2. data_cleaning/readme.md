## Data Cleaning and changing type 
Create new lambda fuctions in AWS which can play key roles of cleaning in AWS 
- Null values changed to unknown in CustomerID: [test-cleaning](https://github.com/Richie-Kwon/ecommercedata/blob/main/1.%20streaming/lambda_streaming/test-cleaning.py) 
- Changing type to Parquet and timestamp: (InvoiceDate): [writeToS3](https://github.com/Richie-Kwon/ecommercedata/blob/main/1.%20streaming/lambda_streaming/writeToS3.py) 
- Data nomalisation can be done if necessary for preidictive analysis or machine learning




