import requests

URL = 'Your end point of API gateway'

# examples with invoice No (536365) and stockCode (85123A)
params = {'InvoiceNo': '536365', 'StockCode': '85123A'}

response = requests.get(URL, params=params)

# Print the result of the query
print(response.json()['body'])
