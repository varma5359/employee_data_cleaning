def transform_data(df):
    """Create useful calculated columns from cleaned data."""

    if "Employee Name" in df:
        df["Employee Name"]=df["Employee Name"].str.title()

    if "Salary" in df:
        df["Annual Salary"]=df["Salary"]

    if all(col in df for col in ["Basic Salary","HRA","Allowances"]):
        df["Calculated Gross Salary"]=df[
            ["Basic Salary","HRA","Allowances"]
        ].sum(axis=1,min_count=1)

    if all(col in df for col in ["Basic Salary","HRA","Allowances","Bonus","Overtime Pay","Deductions"]):
        df["Calculated Net Salary"]=(
            df["Basic Salary"].fillna(0)
            +df["HRA"].fillna(0)
            +df["Allowances"].fillna(0)
            +df["Bonus"].fillna(0)
            +df["Overtime Pay"].fillna(0)
            -df["Deductions"].fillna(0)
        )

    return df