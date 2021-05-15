## Create Lambda fuction in AWS<br /> 
 &ensp;&ensp;- Create a new lambda fuction in AWS which can process data coming from API gateway and send it to Kinesis. <br /> 
 &ensp;&ensp;![image](https://user-images.githubusercontent.com/56697877/118363529-b7e1a780-b58c-11eb-8cc4-eb4890c7139d.png) <br /> <br /> 
 &ensp;&ensp;- Once API gate is created, the API gateway has to be a trigger of this lambda function <br /> 
 &ensp;&ensp;![image](https://user-images.githubusercontent.com/56697877/118363424-312cca80-b58c-11eb-9c58-2932f3c82a41.png)<br /><br /> <br /> 
 &ensp;&ensp;- Attach policies to write/read data in Kinesis and to read data in DynamoDB in IAM<br /> 
 &ensp;&ensp;![image](https://user-images.githubusercontent.com/56697877/118363394-14909280-b58c-11eb-8c45-cf61f56d84d9.png)<br /> <br /> 
 &ensp;&ensp;- Add python code in the lambda function ([test](https://github.com/Richie-Kwon/ecommercedata/blob/main/1.%20streaming/lambda_streaming/test.py))<br /> 
 &ensp;&ensp;![image](https://user-images.githubusercontent.com/56697877/118363829-1ce9cd00-b58e-11eb-8a6a-14a0fe9312ec.png)<br /> 










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
