import streamlit as st
st.title("hello world")
st.header("This is a header")
st.write("This is a simple Streamlit app.")

if st.button("click me"):
    st.write("Button clicked!")