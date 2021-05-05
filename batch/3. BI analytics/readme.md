# Create EMR and Zeppline

1. Create EMR

- Select Cluster with Zeppelin
- IAM role: Download key pairs (.pem) in EC2
- Inbound rule in security group: SSH(Type), TCP(Protocol), 22(port), 0.0.0.0/0 (Source)

2. Configuration in SSH connection

- Click Enable web connection and then type down commands in terminal
- Configure proxy with foxyproxy-settings.xml

3. Access the Zeppelin
   Open new browser with URL (http://master-public-dns-name:8890/)

# Connect Redshift with PowerBI

1. Add rule in the inbound rule: TCP, Port number (used for your cluster), IP (e.g. 0.0.0.0/0)
2. Create a connection with the endpoint of the cluster, Database naem, Port, unsername, and password in the Getdata menu
3. Select import or directQuery(if you want to run query in the cluster)
