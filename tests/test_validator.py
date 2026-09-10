import pandas as pd
from src.validator import valid_email,clean_phone,validate_data


def test_valid_email():
    """Check email validation."""
    assert valid_email("test@gmail.com")
    assert not valid_email("test@gmail")


def test_clean_phone():
    """Check phone number cleaning."""
    assert clean_phone("98765 43210")=="9876543210"
    assert clean_phone("+91-9876543210")=="9876543210"
    assert pd.isna(clean_phone("12345"))


def test_validate_data():
    """Check that invalid employee records are rejected."""
    df=pd.DataFrame({"Employee ID":["E001",None],"Employee Name":["Rahul Kumar","Test"],"Age":[25,150]})
    df=validate_data(df)
    assert df["valid"].iloc[0]
    assert not df["valid"].iloc[1]