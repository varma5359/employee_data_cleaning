import pandas as pd


def read_file(path):
    """Read a CSV or Excel file and return a DataFrame."""
    if path.lower().endswith(".csv"):
        return pd.read_csv(path)
    if path.lower().endswith((".xlsx",".xls")):
        return pd.read_excel(path)
    raise ValueError("Only CSV and Excel files are supported.")