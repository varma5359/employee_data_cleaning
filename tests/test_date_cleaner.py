import pandas as pd
from src.date_cleaner import clean_dates


def test_clean_dates():
    """Check that valid dates are converted."""
    df=pd.DataFrame({"Joining Date":["2024-01-15","15/02/2024","2024-02-30"]})
    df=clean_dates(df)
    assert pd.notna(df["Joining Date"].iloc[0])
    assert pd.notna(df["Joining Date"].iloc[1])
    assert pd.isna(df["Joining Date"].iloc[2])