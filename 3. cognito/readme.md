# Create a token by using AWS cognito

For security, it would be required to use a token when posting or getting data in AWS

1. Go to AWS cognito and then create a user pool
2. Domain name: create your own cognito domain
3. Configure things in settings
   1. App clients: add client
   2. App client settings:
   - callback URL/Sing out URL (such as example.com)
   - Tick: Authorization code grant/ Implicit grant/email/ openid
   - Add domain in HostedUI
4. Launch HostedUI
   1. Create username and password
   2. Sign in
   3. Check a new webpage and code in URL
5. Go to API gateway

   1. Change setting in Method request for GET and POST method

   - Athorization: select cognito user pool authorizers made
   - OAuth Scopes: select default anyone (phone, email, and so on)
   - Deploy

   2. Create new authorizer in the type of congnito and select the user pool made in cognito
   3. Type down in Token source: authorization
   4. Luach HostedUI again
   5. Replace code&scope with token&scope in the URL
   6. Use access token when posting or getting data in aws

6. Run insert_cognito.py to ingest data
7. Run transaction_cognito.py to send a query to DynamoDB
