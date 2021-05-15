## Connect Redshift with PowerBI<br /> 
&ensp;&ensp;1. Add rule in the inbound rule<br />
&ensp;&ensp;&ensp;‣ TCP, Port number (used for your cluster)<br />
&ensp;&ensp;&ensp;‣ IP (e.g. 0.0.0.0/0)<br />
&ensp;&ensp;&ensp;![image](https://user-images.githubusercontent.com/56697877/118372836-67c60d80-b5ab-11eb-9121-21e777f96e75.png)

&ensp;&ensp;2. Create a connection with the endpoint of the cluster, Database name, Port, unsername, and password in the Getdata menu
&ensp;&ensp;&ensp;!![image](https://user-images.githubusercontent.com/56697877/118372925-e91da000-b5ab-11eb-90a3-f1999c448d89.png)
&ensp;&ensp;3. Select import or directQuery(if you want to run query in the cluster)<br /><br />
&ensp;&ensp;4. Exploit the table to find out insights about ecommerce transactions<br />
&ensp;&ensp;![image](https://user-images.githubusercontent.com/56697877/118373049-87aa0100-b5ac-11eb-9265-eb58d2d61963.png)


## Connect Redshift with Tableau<br /> 
&ensp;&ensp;Create a connection with the endpoint of the cluster, Database naem, Port, unsername, and password in the source
&ensp;&ensp;![image](https://user-images.githubusercontent.com/56697877/118373320-2420d300-b5ae-11eb-92d5-977aeb519ae2.png)


## Connect S3 with Jupyternotebook
Run [boto3.py](https://github.com/Richie-Kwon/ecommercedata/blob/main/1.%20streaming/4.%20BI%20analytics/boto3.py) with AWS Key and AWS secret
![image](https://user-images.githubusercontent.com/56697877/118373436-b32deb00-b5ae-11eb-88bf-0cd06d9d49b4.png)


## Create datacatalog in glue and run queries in Athena
1. Create a crawler
![image](https://user-images.githubusercontent.com/56697877/118373558-7adadc80-b5af-11eb-845c-e7d501dab455.png)
   ‣ Crawler name: create your crawler name <br />
   ‣ Crawler source type: S3 and its path <br />
   ‣ IAM: Read in S3 <br />
   ‣ Frequency: set up frequecy <br />
   ‣ Database: create your database name <br /><br />
2. Run the crawler<br />
3. Edit schema of the table created if necessary<br />
![image](https://user-images.githubusercontent.com/56697877/118373645-eb81f900-b5af-11eb-80a1-0c41f89b6e3d.png)

4. Open the database and the table in Athena<br />
5. Put down the path of S3 bucket where the query results are stored in settings<br />
6. Run Queries to analyse data<br />
![image](https://user-images.githubusercontent.com/56697877/118373842-cd68c880-b5b0-11eb-8fdd-06bb64ef2e65.png)<br />

## Create a reqeust to get transaction data in DynamoDB
1. Check the URL of GET method in Stages in API gateway <br />
![image](https://user-images.githubusercontent.com/56697877/118373941-423c0280-b5b1-11eb-9122-b35c6e116ae0.png)

2. Open Postman (https://www.postman.com/)<br />
3. Check the URL of GET method in Stages in API gateway<br />
4. Go to create a request menu <br />
5. Enter URL and add Key (InvoiceNo & Stockcode) and values <br />
6. Get a response from DynameDB with new URL
![image](https://user-images.githubusercontent.com/56697877/118374170-90053a80-b5b2-11eb-994d-e24cc4e1e922.png)

7. The same result can be found when running the code below ([transaction.py](https://github.com/Richie-Kwon/ecommercedata/blob/main/1.%20streaming/4.%20BI%20analytics/transaction.py))
```
import requests

URL = 'Your end point of API gateway'

# examples with invoice No (536365) and stockCode (85123A)
params = {'InvoiceNo': '536365', 'StockCode': '85123A'}

response = requests.get(URL, params=params)

# Print the result of the query
print(response.json()['body'])
```
