import pandas as pd


def clean_data(df):
    """Clean column names, missing values and duplicate rows."""
    df.columns=df.columns.str.strip()
    df=df.drop_duplicates().dropna(how="all")
    missing=["","unknown","UNKNOWN","Unknown","null","NULL","None","none","N/A","n/a","NA","-"]
    df=df.replace(missing,pd.NA)
    return df