## Create a token by using AWS cognito

For security, it would be required to use a token when posting or getting data in AWS

1. Go to AWS cognito and then create a user pool
2. Domain name: create your own cognito domain
3. Configure things in settings <br /> 
   ‣ App clients: add client <br /> 
   ‣ App client settings: <br /> 
   &ensp; - Callback URL/Sing out URL (such as example.com)<br /> 
   &ensp; - Tick: Authorization code grant/ Implicit grant/email/ openid<br /> 
   &ensp; - Add domain in HostedUI<br /> 
![image](https://user-images.githubusercontent.com/56697877/118374503-5b927e00-b5b4-11eb-8176-e34bba7e9371.png)

4. Launch HostedUI <br /> 
   ‣ Create username and password <br /> 
   ‣ Sign in <br /> 
   ‣ Check a new webpage and code in URL <br /> 
![image](https://user-images.githubusercontent.com/56697877/118374610-05720a80-b5b5-11eb-857c-6976e32f3f8d.png)

5. Go to API gateway

   ‣ Change setting in Method request for GET and POST method <br /> 

   &ensp;- Athorization: select cognito user pool authorizers made <br /> 
   &ensp;- OAuth Scopes: select default anyone (phone, email, and so on) <br /> 
   &ensp;- Deploy <br /> 
![image](https://user-images.githubusercontent.com/56697877/118374674-64d01a80-b5b5-11eb-9713-a2331a1a1dcc.png)

   ‣ Create new authorizer in the type of congnito and select the user pool made in cognito <br /> 
   ![image](https://user-images.githubusercontent.com/56697877/118374911-461e5380-b5b6-11eb-9b12-880e08cf3a17.png)

   ‣ Type down in Token source: authorization <br /> <br /> 
   ‣ Luach HostedUI again <br /> <br /> 
   ‣ Replace code&scope with token&scope in the URL <br /> 
   ![image](https://user-images.githubusercontent.com/56697877/118374743-be384980-b5b5-11eb-92a8-83ae9f725f62.png)

   ‣ Use access token when posting or getting data in aws<br /> 

6. Run [insert_cognito.py](https://github.com/Richie-Kwon/ecommercedata/blob/main/3.%20cognito/insert_cognito.py) to ingest data
```
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
```
7. Run [transaction_cognito.py](https://github.com/Richie-Kwon/ecommercedata/blob/main/3.%20cognito/transaction_cognito.py) to send a query to DynamoDB

```
import requests

URL = 'your endpoint'
params = {'InvoiceNo': '536365', 'StockCode': '85123A'}

accesstoken = 'your access token'

headers = {'authorization': accesstoken}

response = requests.get(URL, params=params, headers=headers)

print(response.json()['body'])
```
