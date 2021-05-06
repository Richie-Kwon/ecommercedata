# Create S3 buckets and upload

- one bucket to store raw data
- the other one to store transformed data

# Create a lambda function to clean or transform raw data

- Create a lambda fucntion
- Run ingestForbatch.py to clean or transform raw data

# Scheduling lambda fuction

1. Go to Cloudwatch
2. Create a rule
   - Schedule: set up rate
   - Add target: select your lambda function
