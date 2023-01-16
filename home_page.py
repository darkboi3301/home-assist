import streamlit as st
import requests
from streamlit_extras.switch_page_button import switch_page
import time
st.set_page_config(
    page_title="Home page",
    page_icon="👋",
)
st.title("Home Page")
from streamlit_card import card


if st.button('Report a Homeless person'):
    st.write('Why hello there')
    switch_page("Report homeless")
if st.button('Become a Volunteer'):
    st.write('Why hello there')
    switch_page("Become volunteer")

