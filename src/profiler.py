import pandas as pd

def profile_data(df):
    """Show basic information and data quality problems."""
    print("\n===== DATASET PROFILE =====")
    print("Rows:",df.shape[0],"| Columns:",df.shape[1])
    print("\nColumns:",df.columns.tolist())
    print("\nMissing Values:\n",df.isna().sum())
    print("\nDuplicate Rows:",df.duplicated().sum())
    print("\nData Types:\n",df.dtypes)
    return df