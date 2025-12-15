import streamlit as st

st.title("Sunbeam Infotech")

def show_aboutus_page():
    st.header("About Us")
    st.write(
        "At Sunbeam we believe retaining a competitive edge is imperative for any individual "
        "in today's professional world. Companies are restructuring their organizations & "
        "reengineering their business processes."
    )

def show_internship_page():
    st.header("Internship")
    st.write("""
    It is really difficult to sustain competitive edge of an industry.
    No matter you are an employer, employee or an entrepreneur.

    Technology, innovations and business trends has added diversified change
    to the organizational process.
    """)

def show_courses_page():
    st.header("Courses")

def show_contactus_page():
    st.header("Contact Us")
    st.markdown("### Sunbeam Hinjewadi")
    st.write("""
    "Sunbeam IT Park", Second Floor, Phase 2 of Rajiv Gandhi Infotech Park,
    Hinjawadi, Pune - 411057, MH-INDIA
    """)

if 'page' not in st.session_state:
    st.session_state.page = "About Us"

with st.sidebar:
    if st.button("About Us", use_container_width=True):
        st.session_state.page = "About Us"
    if st.button("Internship", use_container_width=True):
        st.session_state.page = "Internship"
    if st.button("Courses", use_container_width=True):
        st.session_state.page = "Courses"
    if st.button("Contact Us", use_container_width=True):
        st.session_state.page = "Contact Us"

if st.session_state.page == "About Us":
    show_aboutus_page()
elif st.session_state.page == "Internship":
    show_internship_page()
elif st.session_state.page == "Courses":
    show_courses_page()
elif st.session_state.page == "Contact Us":
    show_contactus_page()
