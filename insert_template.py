import pandas as pd
import requests

# End Point of AWS
URL = "https://04iywy4kqg.execute-api.eu-west-2.amazonaws.com/beta/test-resource"

# Reading dataset as dataFrame(df)
df = pd.read_csv('testdata.csv', sep=',')

# Coverting to json and writing rows into api
for i in df.index:
    # Converting to json
    export = df.loc[i].to_json()

    # Writing into api
    response = requests.post(URL, data=export)

    print(response)
