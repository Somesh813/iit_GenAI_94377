import pandas as pd
df=pd.read_csv('Products.csv')
print(df.to_string(index=False))
total_rows=len(df)
print("Total number of rows=",total_rows)