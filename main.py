from src.pipeline import run_pipeline


def main():
    """Run the complete cleaning pipeline for all datasets."""

    employee_df=run_pipeline(
        "data/raw/employees.csv",
        "data/processed/employees_cleaned.csv",
        "data/rejected/employees_rejected.csv"
    )

    employee_ids=set(employee_df["Employee ID"].dropna())

    department_df=run_pipeline(
        "data/raw/departments.csv",
        "data/processed/departments_cleaned.csv",
        "data/rejected/departments_rejected.csv"
    )

    department_ids=set(department_df["Department Name"].dropna())

    run_pipeline(
        "data/raw/attendance.csv",
        "data/processed/attendance_cleaned.csv",
        "data/rejected/attendance_rejected.csv",
        employee_ids=employee_ids,
        department_ids=department_ids
    )

    run_pipeline(
        "data/raw/payroll.csv",
        "data/processed/payroll_cleaned.csv",
        "data/rejected/payroll_rejected.csv",
        employee_ids=employee_ids,
        department_ids=department_ids
    )


if __name__=="__main__":
    main()