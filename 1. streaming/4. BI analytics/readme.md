# Connect Redshift with PowerBI

1. Add rule in the inbound rule: TCP, Port number (used for your cluster), IP (e.g. 0.0.0.0/0)
2. Create a connection with the endpoint of the cluster, Database naem, Port, unsername, and password in the Getdata menu
3. Select import or directQuery(if you want to run query in the cluster)

# Connect Redshift with Tableau

Create a connection with the endpoint of the cluster, Database naem, Port, unsername, and password in the source

# Connect S3 with Jupyternotebook

Run boto3.py with AWS Key and AWS secret

# Create datacatalog in glue and run queries in Athena

1. Create a crawler
   - crawler name: create your crawler name
   - crawler source type: S3 and its path
   - IAM: Read in S3
   - Frequency: set up frequecy
   - Database: create your database name
2. Run the crawler
3. Edit schema of the table created if necessary
4. Open the database and the table in Athena
5. Put down the path of S3 bucket where the query results are stored in settings
6. Run Queries to analyse data

# Create a reqeust to get transaction data in DynamoDB

1. Check the URL of GET method in Stages in API gateway
2. Open Postman (https://www.postman.com/)
3. Go to create a request menu
4. Enter URL and add Key (InvoiceNo & Stockcode) and values
5. Get a response from DynameDB with new URL
6. The same result can be found when running transaction.py
