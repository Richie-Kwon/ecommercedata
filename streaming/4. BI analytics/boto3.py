import pandas as pd
import io
from boto.s3.connection import S3Connection

AWS_KEY = ''
AWS_SECRET = ''

# Create connection
aws_connection = S3Connection(
    AWS_KEY, AWS_SECRET, host='s3.eu-west-2.amazonaws.com')

# your bucket name and file name
bucket = aws_connection.get_bucket('your bucket name')
fileName = 'your file name'

# create pandasDataFrame
content = bucket.get_key(fileName).get_contents_as_string()
reader = pd.read_parquet(io.BytesIO(content))
