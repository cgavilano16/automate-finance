import streamlit as st
import pandas as pd
import plotly.express as px
import json
import os
# To run app, in terminal "streamlit run <python file name>"
# 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
st.set_page_config(page_title="Simple Finance App", page_icon="🪙", layout='wide')

def load_transactions(file):
    try:
        df = pd.read_csv(file)

        # Clean up data on CSV file
        df.columns = [col.strip() for col in df.columns]   #remove leading and ending spaces
        df["Amount"] = df["Amount"].str.replace(",", "").astype(float)   #replace commas in string with empty spaces, and make them floats
        df["Date"] = pd.to_datetime(df["Date"], format="%d %b %Y")    #conversion in format to dd/mm/yyyy and into a datetime format for operations

        # st.write(df)
        return df

    except Exception as e:
        st.error(f"Error processing file: {str(e)}")
        return None

def main():
    st.title("Simple Finance Dashboard")
    uploaded_file = st.file_uploader("Upload your transaction CSV file", type=["csv"])

    if uploaded_file is not None:
        df = load_transactions(uploaded_file)

        if df is not None:
            #Create a copy of data-frame filtering instance where Debit/Credit column equals Debit or Credit
            debits_df = df[df["Debit/Credit"] == "Debit"].copy()    
            credits_df = df[df["Debit/Credit"] == "Credit"].copy()    

            tab1, tab2 = st.tabs(["Expenses (Debits)", "Payments (Credits)"])

            with tab1:
                st.write(debits_df)

            with tab2:
                st.write(credits_df)

main()