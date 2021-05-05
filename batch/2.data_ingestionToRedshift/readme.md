# ETL process with Glue

1. Create a table in Redshift: refer to creating_table.txt
2. Create Crawlers for data in S3 to create Datacatalog

- crawler name: create your crawler name
- crawler source type: S3 and its path
- IAM: Access in S3 and Redshift, and Glue service role
- Frequency: set up frequecy
- Database: create your database name

3. Create Crawlers for the table in Redshift to create Datacatalog

- crawler name: create your crawler name
- crawler source type: JDBC and Redshift path
- IAM: Access in S3 and Redshift, and Glue service role
- Frequency: set up frequecy
- Database: create your database name

4. Run crawlers

5. Add jobs in ETL

- Name
- IAM: Access in S3 and Redshift, and Glue service role
- Type: Spark
- Number of workers: incresae workers in case of big data
- Worker type: higher version of type in case of big data
- Choose source (S3 datacatalog) and target (Redshift datacatalog)
- Edit schema
- Create endpoint in VPC to connect VPC to S3
- Run the job
