import streamlit as st
import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY=os.getenv("API_KEY")

if "login" not in st.session_state:
    st.session_state.login=False

if not st.session_state.login:

    user=st.text_input("Username")
    pwd=st.text_input("Password",type="password")

    if st.button("Login") and user==pwd:
        st.session_state.login=True

else:
    city=st.text_input("City")

    if st.button("Get Weather"):
        url=f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        data=requests.get(url).json()
        st.write("Temp:", data["main"]["temp"])

    if st.button("Logout"):
        st.session_state.login=False
        st.write("Thanks")
