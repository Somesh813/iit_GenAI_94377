import streamlit as st

with st.form(key="reg_form"):
    st.header("Registration Form")
    first_name=st.text_input(key="fname",label="First Name")
    last_name=st.text_input(key="lname",label="Last Name")
    age=st.slider("Age", 10, 100, 25, 1)
    addr=st.text_area("address")
    submit_btn=st.form_submit_button("submit",type="primary")
    st.toast("Please fill the form and submit")

if submit_btn:
    err_message=""
    is_error=False
    if not first_name:
        is_error=True
        err_message+="First Name is required\n"
    if not last_name:
        is_error=True
        err_message+="Last Name is required\n"
    if not addr:
        is_error=True
        err_message+="Address is required\n"
    if is_error:
        st.error(err_message)
    else:
        message=f"Successfully Registered\nName:{first_name} {last_name}\nAge:{age}\nAddress:{addr}" 
    
    st.success(message)               