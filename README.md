# ecommerce-
Establishing data pipe lines for e-commerce data in AWS to 1) process transactions ad provde purcahse history (or summary) to customers and 2) to analyse the data for business analytics such as average sales, the most popular units, and total number of invoices 


# Dataset
E-commerce data from http://archive.ics.uci.edu/ml/index.php : 8 Columns and 541909 rows
 
Columns
- InvoiceNO: 6 digit integer and unique value for each transaction
  Calleation and bad debt(Prefix 'c' means cancellation and Prefix 'A' means adjust bad debt) won't be used 
- StockCode 
- Description 
- Quantity 
- InvoiceDate
- UnitPrice
- CustomerID 
- Country


# Streaming process
The layout of the streaming process
![image](https://user-images.githubusercontent.com/56697877/116921770-606a4000-ac4c-11eb-98a9-9159b1d17ba6.png)



# Batch process
The layout of the batch process
![image](https://user-images.githubusercontent.com/56697877/116911315-9b657700-ac3e-11eb-8603-a25b5fb612de.png)
