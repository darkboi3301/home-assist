import streamlit as st
import requests
import time


st.title("Report a homeless person")

with st.form("my_form"):
    st.write("Inside the form")
    hom_name = st.text_input('Name (Optional)', value="Unspecified")
    #gather approx age
    hom_age = st.slider("Approx age of person")
    #gather gender
    hom_gender = st.selectbox('Gender of the person',('Unspecified','Male', 'Female', 'Other'))
    #gather location
    hom_location = st.text_input("Location",value="unpspecified")

    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.balloons()
        row = (str(hom_name),str(hom_gender),str(hom_age),hom_location)
        import csv
        # open the file in the append mode
        f = open('store.csv', 'a')
        # create the csv writer
        writer = csv.writer(f)
        # write a row to the csv file
        writer.writerow(row)
        # close the file
        f.close()
        st.success("submit succesfull")
        time.sleep(1)
        st.experimental_rerun()

        
