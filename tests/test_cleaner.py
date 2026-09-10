from src.reader import read_file
from src.cleaner import clean_data


def test_clean_data():
    """Check that duplicate rows are removed."""
    df=read_file("data/raw/employees.csv")
    before=len(df)
    df=clean_data(df)
    assert len(df)<=before
    assert df.duplicated().sum()==0