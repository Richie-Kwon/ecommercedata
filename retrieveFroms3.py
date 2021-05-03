import awswrangler as wr

path = 's3://test-rawstorage/output-14-Apr-2021-060912.parquet'

df = wr.s3.read_parquet(path=path)

print(df)
