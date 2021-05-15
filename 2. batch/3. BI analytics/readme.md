## Create EMR and Zeppline

1. Create EMR <br />
&ensp;‣ Select Cluster with Zeppelin <br />
&ensp;‣ IAM role: Download key pairs (.pem) in EC2 <br /> 
&ensp;‣ Inbound rule in security group: SSH(Type), TCP(Protocol), 22(port), 0.0.0.0/0 (Source) <br />

2. Configuration in SSH connection <br />
&ensp;‣ Click Enable web connection and then type down commands in terminal <br />
&ensp;‣ Downlaod and install [foxyProxy](https://chrome.google.com/webstore/detail/foxyproxy-standard/gcknhkkoolaabfmlnjonogaaifnjlfnp?hl=en) <br />
&ensp;‣ Configure proxy with [foxyproxy-settings.xml](https://github.com/Richie-Kwon/ecommercedata/blob/main/2.%20batch/3.%20BI%20analytics/foxyproxy-settings.xml)<br />

3. Access the Zeppelin
Open new browser with [URL](http://master-public-dns-name:8890/)

## Connect Redshift with PowerBI
Please refer to the steaming process:[BI analytics](https://github.com/Richie-Kwon/ecommercedata/tree/main/1.%20streaming/4.%20BI%20analytics)

