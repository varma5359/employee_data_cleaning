import streamlit as st
import pandas as pd
from src.cleaner import clean_data
from src.string_cleaner import clean_strings
from src.numeric_cleaner import clean_numbers
from src.date_cleaner import clean_dates
from src.validator import validate_data
from src.transformer import transform_data

st.set_page_config(page_title="Employee Data Cleaning",layout="wide")

st.title("Employee Data Cleaning & Quality Pipeline")
st.write("Upload a CSV file to clean, validate and transform employee data.")

uploaded_file=st.file_uploader("Upload CSV file",type=["csv"])

if uploaded_file:
    df=pd.read_csv(uploaded_file)

    st.subheader("Raw Data")
    st.dataframe(df,use_container_width=True)

    if st.button("Clean Data"):
        df=clean_data(df)
        df=clean_strings(df)
        df=clean_numbers(df)
        df=clean_dates(df)
        df=validate_data(df)
        df=transform_data(df)

        valid_df=df[df["valid"]]
        rejected_df=df[~df["valid"]]

        st.success("Data cleaning completed.")

        col1,col2,col3=st.columns(3)

        col1.metric("Total Records",len(df))
        col2.metric("Valid Records",len(valid_df))
        col3.metric("Rejected Records",len(rejected_df))

        st.subheader("Cleaned Data")
        st.dataframe(valid_df,use_container_width=True)

        st.subheader("Rejected Data")
        st.dataframe(rejected_df,use_container_width=True)

        clean_csv=valid_df.to_csv(index=False)
        rejected_csv=rejected_df.to_csv(index=False)

        st.download_button(
            "Download Cleaned CSV",
            clean_csv,
            "cleaned_data.csv",
            "text/csv"
        )

        st.download_button(
            "Download Rejected CSV",
            rejected_csv,
            "rejected_data.csv",
            "text/csv"
        )