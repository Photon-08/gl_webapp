import streamlit as st
import pandas as pd
import time

def fetch(file=None,group_number='None'):

    

    df = pd.read_csv(file,on_bad_lines='skip')
    
    bandipur_df = df[df["House"] == "Bandipur House"]

    gl_df = bandipur_df[bandipur_df["GroupId"] == group_number]

    sheet_name = "Allocation_Sheet_Bandipur_" + str(group_number)+".csv"

    return gl_df.to_csv()
    
    
st.title("House Allocation Sheet Generator App || Bandipur House")


file_up = st.file_uploader(label="Please Upload the master list:")
group_number = st.selectbox("Please enter your group number: ",(3,5,7,22,38,39,41,75,100,106,208,241,242,243,263,277,285,287,297,302,325,333,334,338))

if st.button(label="Click Here to Generate Your Sheet!"):

    sheet_name = "Allocation_Sheet_Bandipur_" + str(group_number)+".csv"
    csv = fetch(file=file_up,group_number=group_number)
    st.download_button(label="Click here to download",file_name=sheet_name,data=csv,mime='text/csv')
