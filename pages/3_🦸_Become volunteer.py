import streamlit as st
import requests



st.title("Become a volunteer")
st.write("Volunteering to help homeless people is a rewarding and meaningful way to make a difference in your community. There are many ways to get involved, such as providing meals, donating clothing and supplies, etc... ")
import pandas as pd

def read_csv_file(filename):
    df = pd.read_csv(filename)
    return df

# Read the csv file
filename = 'store.csv'
df = read_csv_file(filename)

# Display the contents of the csv file
st.dataframe(df,use_container_width=True) 