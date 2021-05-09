import requests

URL = 'your endpoint'
params = {'InvoiceNo': '536365', 'StockCode': '85123A'}

accesstoken = 'your access token'

headers = {'authorization': accesstoken}

response = requests.get(URL, params=params, headers=headers)

print(response.json()['body'])
