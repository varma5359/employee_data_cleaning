from src.numeric_cleaner import money_to_number,clean_numbers


def test_money_to_number():
    """Check common money formats."""
    assert money_to_number("₹6,50,000")==650000
    assert money_to_number("30K")==30000
    assert money_to_number("4.8 LPA")==480000
    assert money_to_number("1.2 Crore")==12000000


def test_clean_numbers():
    """Check that numeric values are cleaned."""
    import pandas as pd
    df=pd.DataFrame({"Age":["25","abc","150","30"]})
    df=clean_numbers(df)
    assert df["Age"].iloc[0]==25
    assert pd.isna(df["Age"].iloc[1])
    assert pd.isna(df["Age"].iloc[2])