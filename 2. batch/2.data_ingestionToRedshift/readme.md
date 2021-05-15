## ETL process with Glue

1. Create a table in Redshift 
```
create table batchprocess(
	InvoiceNo int,
	StockCode varchar(200),
	Description varchar(200),
	Quantity int,	
	InvoiceDate varchar(200),
	UnitPrice float,
	CustomerID varchar(200),  	
 	Country varchar(200)
);
```
2. Create Crawlers for data in S3 to create Datacatalog <br />
&ensp;&ensp;‣ Crawler name: create your crawler name <br />
&ensp;&ensp;‣ Crawler source type: S3 and its path <br />
&ensp;&ensp;‣ IAM: Access in S3 and Redshift, and Glue service role <br />
&ensp;&ensp;‣ Frequency: set up frequecy <br />
&ensp;&ensp;‣ Database: create your database name <br />

3. Create Crawlers for the table in Redshift to create Datacatalog<br />
&ensp;&ensp;‣ Crawler name: create your crawler name <br />
&ensp;&ensp;‣ Cawler source type: JDBC and Redshift path <br />
&ensp;&ensp;‣ IAM: Access in S3 and Redshift, and Glue service role<br />
&ensp;&ensp;‣ Frequency: set up frequecy<br />
&ensp;&ensp;‣ Database: create your database name<br />

4. Run crawlers

5. Add jobs in ETL <br />
&ensp;&ensp;‣ Name: Give ETL name <br />
&ensp;&ensp;‣ IAM: Access in S3 and Redshift, and Glue service role <br />
&ensp;&ensp;‣ Type: Spark <br />
&ensp;&ensp;‣ Number of workers: incresae workers in case of big data <br />
&ensp;&ensp;‣ Worker type: higher version of type in case of big data <br />
&ensp;&ensp;‣ Choose source (S3 datacatalog) and target (Redshift datacatalog) <br />
&ensp;&ensp;‣ Edit schema <br />
&ensp;&ensp;‣ Create endpoint in VPC to connect VPC to S3 <br />
&ensp;&ensp;‣ Run the job <br />

![image](https://user-images.githubusercontent.com/56697877/118375672-1887d900-b5bb-11eb-825b-5dcf7325aad7.png)

6. Check ETL result
![image](https://user-images.githubusercontent.com/56697877/118376120-fba0d500-b5bd-11eb-834d-2bbbb7e53176.png)
