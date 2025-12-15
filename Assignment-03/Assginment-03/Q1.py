import streamlit as st
import pandas as pd
from pandasql import sqldf  

st.title("Product Data Analysis")
file=st.file_uploader("Upload csv file",type=["csv"])
if file:
    df=pd.read_csv(file)
    st.dataframe(df)

    query=st.text_area("Enter SQL Query (table name:df)",
        "SELECT category, AVG(price) FROM df GROUP BY category")

if st.button("Run"):
    result=sqldf(query,{"df":df})
    st.dataframe(result)    