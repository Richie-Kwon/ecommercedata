## Create S3 buckets and upload
Create S3 buckets to store raw data and transforemd adta

## Create a lambda function to clean or transform raw data
Create a lambda fucntion and put lambda code ([ingestForbatch.py](https://github.com/Richie-Kwon/ecommercedata/blob/main/2.%20batch/1.%20data_ingestionToS3/ingestForbatch.py)) to clean or transform raw data

## Scheduling lambda fuction
1. Go to Cloudwatch<br />
2. Create a rule <br />
   ‣ Schedule: set up rate <br />
   ‣ Add target: select your lambda function <br /><br />
![image](https://user-images.githubusercontent.com/56697877/118375461-b4b0e080-b5b9-11eb-9e92-79674c604d2e.png)
