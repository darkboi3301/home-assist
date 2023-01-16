import streamlit as st
import requests
from streamlit_extras.switch_page_button import switch_page
import time
st.set_page_config(
    page_title="Home page",
    page_icon="👋",
)
st.title("Home Page")
st.write("This website would provide a platform for volunteers to report homeless people in need of help and to coordinate with other volunteers to provide assistance. The website would allow volunteers to post about homeless people they have encountered, including their needs and locations. This information would be visible to other volunteers, who could then coordinate efforts to provide assistance. ")

if st.button('Report a Homeless person'):
    st.write('Why hello there')
    switch_page("Report homeless")
if st.button('Become a Volunteer'):
    st.write('Why hello there')
    switch_page("Become volunteer")

