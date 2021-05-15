## Create Lambda fuction in AWS<br /> 
 &ensp;&ensp;1. Create a new lambda fuction in AWS which can process data coming from API gateway and send it to Kinesis. <br /> 
 &ensp;&ensp;![image](https://user-images.githubusercontent.com/56697877/118363529-b7e1a780-b58c-11eb-8cc4-eb4890c7139d.png) <br /> <br /> 
 &ensp;&ensp;2. Once API gate is created, the API gateway has to be a trigger of this lambda function <br /> 
 &ensp;&ensp;![image](https://user-images.githubusercontent.com/56697877/118363424-312cca80-b58c-11eb-9c58-2932f3c82a41.png)<br /><br /> <br /> 
 &ensp;&ensp;3. Attach policies to write/read data in Kinesis and to read data in DynamoDB in IAM<br /> 
 &ensp;&ensp;![image](https://user-images.githubusercontent.com/56697877/118363394-14909280-b58c-11eb-8c45-cf61f56d84d9.png)<br /> <br /> 
 &ensp;&ensp;4. Add python code in the lambda function ([test](https://github.com/Richie-Kwon/ecommercedata/blob/main/1.%20streaming/lambda_streaming/test.py))<br /> 
 &ensp;&ensp;![image](https://user-images.githubusercontent.com/56697877/118363829-1ce9cd00-b58e-11eb-8a6a-14a0fe9312ec.png)<br /> <br /> 


## Create API gateway in AWS <br />
&ensp;&ensp;1. Build new REST API in APIgateway <br />
&ensp;&ensp;![image](https://user-images.githubusercontent.com/56697877/118364378-1eb49000-b590-11eb-9efc-e666c74d0cb7.png)<br /><br />

&ensp;&ensp;2. Create resource and method (POST and GET) <br />
&ensp;&ensp;![image](https://user-images.githubusercontent.com/56697877/118364470-6f2bed80-b590-11eb-978c-5c1baab79903.png)<br /><br />
&ensp;&ensp;3. Create connections to lamda function and configure things with GET and POST methods <br />
&ensp;&ensp;&ensp; A. Integration type: Lambday function <br />
&ensp;&ensp;&ensp; B. Lambda function: test (in my case) <br />
&ensp;&ensp;&ensp; C. Lambda region: your region <br />
&ensp;&ensp;&ensp; D. Integration Request > Mapping templates > Content-Type: application/json <br />
&ensp;&ensp;&ensp; E. Integration Request > Mapping templates > Generate template: Method Request passthrough <br />
&ensp;&ensp;![image](https://user-images.githubusercontent.com/56697877/118364512-9d113200-b590-11eb-9a4b-3b248013c196.png)<br /><br />

&ensp;&ensp;4. Create a new stage <br />
&ensp;&ensp;![image](https://user-images.githubusercontent.com/56697877/118364808-ea41d380-b591-11eb-9064-d5866feb46ae.png)<br /><br />
&ensp;&ensp;5. Select Deploy API in actions in Resouces <br />
![image](https://user-images.githubusercontent.com/56697877/118364685-6851aa80-b591-11eb-9394-cde38ad8df1c.png)<br /><br />
&ensp;&ensp;6. Check invoke URL(end point) in stages to post & get data <br />
&ensp;&ensp;![image](https://user-images.githubusercontent.com/56697877/118364808-ea41d380-b591-11eb-9064-d5866feb46ae.png)<br /><br />

## Create Kinesis in AWS
&ensp;&ensp;1. Create one data stream in Kinesis<br />
&ensp;&ensp;![image](https://user-images.githubusercontent.com/56697877/118364997-c468fe80-b592-11eb-9616-7fb2cc713c3b.png)<br /><br />
&ensp;&ensp;2. Configure the number of shard (the bigger the better in case of big data)<br />
&ensp;&ensp;![image](https://user-images.githubusercontent.com/56697877/118365092-304b6700-b593-11eb-8e3b-98c5a2d68e61.png)<br /><br />


## Run Insert_tempalte.py
&ensp;&ensp;Put down the URL (endpoint) in the python code ([insert_template.py](https://github.com/Richie-Kwon/ecommercedata/blob/main/1.%20streaming/1.%20data_%20ingestion/insert_template.py)) and run the code to ingest data
