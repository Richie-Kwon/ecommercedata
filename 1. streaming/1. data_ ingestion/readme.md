# Create Lambda fuction in AWS

1. Create a function in AWS
2. Configure roles: attach policies for POST(to write/read data in Kinesis) and GET(to read data in DynamoDB)
3. Refer to the code in test.py in lambda_streaming folder

# Create API gateway in AWS

1. Build new REST API in APIgateway
2. Create resource and method (POST and GET)
3. Create connections to lamda function
4. Select GET and POST method and then configure things below
   - Integration type: Lambday function
   - Lambda function: test (in my case)
   - Lambda region: your region
   - Integration Request > Mapping templates > Content-Type: application/json
   - Integration Request > Mapping templates > Generate template: Method Request passthrough
5. Select Deploy API in actions in Resouces
6. Check URL(end point) in stages to post data

# Create Kinesis in AWS

Create one data stream in Kinesis

# Run Insert_tempalte.py

1. Put down the URL (endpoint) in the python code (insert_template.py)
2. Run the code to ingest data
