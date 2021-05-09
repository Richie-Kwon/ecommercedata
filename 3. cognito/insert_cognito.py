import pandas as pd
import requests

# Putting down your End Point of AWS
URL = "your endpoint"

accesstoken = 'your access token'

headers = {'authorization': accesstoken}

# Reading dataset as dataFrame(df) and putting down the path of raw data in CSV (in my case path is testdata.csv)
df = pd.read_csv('testdata.csv', sep=',')

# Coverting to json and writing rows into api
for i in df.index:
    # Converting to json
    export = df.loc[i].to_json()

    # Writing into api
    response = requests.post(URL, data=export, headers=headers)

    print(response)
