import pandas as pd


def parse_date(value):
    """Convert common date formats into a valid date."""
    if pd.isna(value):
        return pd.NaT

    value=str(value).strip()

    for dayfirst in [False,True]:
        try:
            return pd.to_datetime(value,format="mixed",dayfirst=dayfirst,errors="raise")
        except:
            pass

    return pd.NaT


def parse_time(value):
    """Convert common time formats into HH:MM:SS."""
    if pd.isna(value):
        return pd.NaT

    try:
        return pd.to_datetime(str(value).strip(),format="mixed",errors="raise").strftime("%H:%M:%S")
    except:
        return pd.NaT


def clean_dates(df):
    """Clean mixed date, month and time formats."""
    date_cols=["Joining Date","Attendance Date","Created Date","Payment Date","Pay Month"]

    for col in date_cols:
        if col in df:
            df[col]=df[col].map(parse_date)

    time_cols=["Joining Time","Check In","Check Out"]

    for col in time_cols:
        if col in df:
            df[col]=df[col].map(parse_time)

    return df