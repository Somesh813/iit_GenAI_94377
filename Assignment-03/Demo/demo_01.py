import pandas as pd
import pandasql as ps

filepath="emp_hdr.csv"
df=pd.read_csv(filepath)
print(df.dtypes)
print("\nEmp Data:")
print(df)
query="SELECT JOB,SUM(sal)total FROM data GROUP BY JOB"
result=pd.sqlf(query,{"data":df})
print("\nQuery Result:")
print(result) 
