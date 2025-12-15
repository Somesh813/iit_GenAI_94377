import pandas as pd
import streamlit as st

st.title("csv Data Viewer")
data_file=st.file_uploader("Upload CSV", type=["csv"]) 
if data_file:
    df=pd.read_csv(data_file)
    st.dataframe(df)