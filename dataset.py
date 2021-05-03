import pandas as pd

df = pd.read_csv(r"data.csv", encoding='unicode_escape')

print(df.isnull().sum())
# print(df.isna().sum(axis=0), end='\n')
# print(len(df))'

df2 = df.copy()
# df2.to_json("testdata-batch.json", orient='records')
df2["CustomerID"].fillna("Unknown", inplace=True)

print(df2.isnull().sum())
