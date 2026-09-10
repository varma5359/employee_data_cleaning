import re
import pandas as pd


def valid_email(value):
    """Check whether an email has a basic valid format."""
    if pd.isna(value):
        return False
    return bool(re.match(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$",str(value)))


def clean_phone(value):
    """Convert a phone number into a standard 10-digit number."""
    if pd.isna(value):
        return pd.NA
    digits=re.sub(r"\D","",str(value))
    if digits.startswith("91") and len(digits)==12:
        digits=digits[2:]
    return digits if len(digits)==10 else pd.NA


def validate_data(df,employee_ids=None,department_ids=None):
    """Validate records using rules suitable for each dataset."""
    df["valid"]=True
    df["rejection_reason"]=""

    def reject(condition,reason):
        df.loc[condition,"valid"]=False
        df.loc[condition,"rejection_reason"]+="; "+reason

    if "Employee ID" in df:
        reject(df["Employee ID"].isna(),"Missing Employee ID")

    if "Employee Name" in df:
        reject(df["Employee Name"].isna(),"Missing Employee Name")

    if "Age" in df:
        reject(df["Age"].isna(),"Invalid Age")

    if "Email" in df:
        reject(df["Email"].notna() & ~df["Email"].map(valid_email),"Invalid Email")

    if "Phone" in df:
        df["Phone"]=df["Phone"].map(clean_phone)

    if "Department ID" in df:
        reject(df["Department ID"].isna(),"Missing Department ID")

    if "Department Name" in df:
        reject(df["Department Name"].isna(),"Missing Department Name")

    if "Employee Count" in df:
        reject(df["Employee Count"].isna(),"Invalid Employee Count")

    if "Attendance ID" in df:
        reject(df["Attendance ID"].isna(),"Missing Attendance ID")

    if "Payroll ID" in df:
        reject(df["Payroll ID"].isna(),"Missing Payroll ID")

    if employee_ids is not None and "Employee ID" in df:
        reject(df["Employee ID"].notna() & ~df["Employee ID"].isin(employee_ids),"Unknown Employee ID")

    if department_ids is not None and "Department" in df:
        reject(df["Department"].notna() & ~df["Department"].isin(department_ids),"Unknown Department")

    if department_ids is not None and "Department Name" in df:
        reject(df["Department Name"].notna() & ~df["Department Name"].isin(department_ids),"Unknown Department")

    if "Attendance Date" in df:
        reject(df["Attendance Date"].isna(),"Invalid Attendance Date")

    if "Payment Date" in df:
        reject(df["Payment Date"].isna(),"Invalid Payment Date")

    if "Joining Date" in df:
        reject(df["Joining Date"].isna(),"Invalid Joining Date")

    if "Work Hours" in df:
        reject(df["Work Hours"].isna(),"Invalid Work Hours")

    if "Overtime Hours" in df:
        reject(df["Overtime Hours"].isna(),"Invalid Overtime Hours")

    for col in ["Salary","Basic Salary","Net Salary"]:
        if col in df:
            reject(df[col].notna() & (df[col]<0),"Negative "+col)

    if "Annual Budget" in df:
        reject(df["Annual Budget"].notna() & (df["Annual Budget"]<0),"Negative Annual Budget")

    df["rejection_reason"]=df["rejection_reason"].str.lstrip("; ").replace("",pd.NA)
    return df