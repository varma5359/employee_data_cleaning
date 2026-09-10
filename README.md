# Employee Data Cleaning & Quality Pipeline

A Python-based data cleaning and validation pipeline designed to process messy employee-related datasets and convert them into clean, validated, analysis-ready CSV files.

The project demonstrates a complete data-processing workflow using **Python, Pandas, validation rules, data transformation, automated testing, and Streamlit**.

## Features

* Read CSV and Excel files
* Clean column names and missing values
* Remove duplicate records
* Clean and standardize employee names
* Standardize department names
* Normalize gender and status values
* Convert salary and monetary values into numeric values
* Convert mixed date and time formats
* Validate employee records
* Validate email addresses
* Standardize phone numbers
* Validate employee and department references
* Detect invalid ages and employee counts
* Validate work hours and overtime hours
* Calculate derived salary fields
* Separate valid and rejected records
* Export cleaned and rejected datasets
* Run automated tests with Pytest
* Upload and process CSV files through a Streamlit interface

## Project Architecture

```text
Raw CSV / Excel
      |
      v
    Reader
      |
      v
   Profiler
      |
      v
    Cleaner
      |
      v
 String Cleaner
      |
      v
 Numeric Cleaner
      |
      v
  Date Cleaner
      |
      v
   Validator
      |
      v
  Transformer
      |
      v
   Exporter
      |
      +------------------+
      |                  |
      v                  v
Cleaned Data        Rejected Data
```

## Project Structure

```text
employee_data_cleaning/
│
├── data/
│   ├── raw/
│   │   ├── employees.csv
│   │   ├── departments.csv
│   │   ├── attendance.csv
│   │   └── payroll.csv
│   │
│   ├── processed/
│   └── rejected/
│
│
├── src/
│   ├── __init__.py
│   ├── reader.py
│   ├── profiler.py
│   ├── cleaner.py
│   ├── string_cleaner.py
│   ├── numeric_cleaner.py
│   ├── date_cleaner.py
│   ├── validator.py
│   ├── transformer.py
│   ├── exporter.py
│   └── pipeline.py
│
├── tests/
│   ├── test_reader.py
│   ├── test_cleaner.py
│   ├── test_numeric_cleaner.py
│   ├── test_date_cleaner.py
│   └── test_validator.py
│
├── config/
│   └── cleaning_rules.yaml
│
├── conftest.py
├── main.py
├── app.py
├── requirements.txt
└── README.md
```

## Datasets

The project contains four deliberately messy datasets.

### 1. Employees

Contains employee information such as:

* Employee ID
* Employee Name
* Age
* Gender
* Department
* Job Title
* Email
* Phone
* City
* Joining Date
* Joining Time
* Salary
* Bonus
* Employment Status
* Manager ID

Example problems:

```text
Rahul Kumar
PRIYA123
Sneha@123
Ramesh!!!
98765 43210
+91-9988776655
₹6,50,000
650000 INR
₹4.8 LPA
15/02/2024
March 5 2024
```

### 2. Departments

Contains department information including:

* Department ID
* Department Name
* Department Head
* Location
* Employee Count
* Annual Budget
* Created Date
* Status

The dataset contains inconsistent department names, locations, numbers, budgets, dates, missing values and duplicate records.

### 3. Attendance

Contains:

* Attendance ID
* Employee ID
* Employee Name
* Attendance Date
* Check In
* Check Out
* Work Hours
* Status
* Location
* Shift

The dataset contains invalid dates, invalid times, negative work hours, missing values, duplicate records and unknown employee IDs.

### 4. Payroll

Contains:

* Payroll ID
* Employee ID
* Employee Name
* Pay Month
* Basic Salary
* HRA
* Allowances
* Deductions
* Bonus
* Overtime Hours
* Overtime Pay
* Net Salary
* Payment Date
* Payment Status
* Bank Account

The dataset contains different salary formats, mixed dates, invalid overtime hours, missing values, duplicate records and unknown employee IDs.

## Cleaning Pipeline

### Step 1 — Read Data

`reader.py` loads CSV and Excel files using Pandas.

```python
df=read_file(path)
```

### Step 2 — Profile Data

`profiler.py` displays:

* Number of rows
* Number of columns
* Column names
* Missing values
* Duplicate rows
* Data types

### Step 3 — Basic Cleaning

`cleaner.py`:

* Removes spaces from column names
* Removes duplicate rows
* Removes completely empty rows
* Converts common missing-value strings into `NaN`

### Step 4 — String Cleaning

`string_cleaner.py`:

* Cleans employee names
* Removes unwanted numbers and symbols
* Standardizes department names
* Standardizes gender values
* Standardizes status values
* Cleans location and job-title text

Example:

```text
PRIYA123     → Priya
Sneha@123    → Sneha
male         → Male
F            → Female
engineering  → Engineering
Human Resources → HR
```

### Step 5 — Numeric Cleaning

`numeric_cleaner.py` converts different monetary formats into numbers.

Examples:

```text
₹6,50,000    → 650000
30K          → 30000
4.8 LPA      → 480000
1.2 Crore    → 12000000
```

It also validates numeric ranges such as:

```text
Age: 18–65
Employee Count: >= 0
Work Hours: 0–24
Overtime Hours: >= 0
```

### Step 6 — Date and Time Cleaning

`date_cleaner.py` handles different date and time formats.

Examples:

```text
2024-01-15
15/02/2024
2023/12/01
01-03-2024
March 5 2024
```

Times are converted into a standard format such as:

```text
09:30:00
```

Invalid dates and times are converted to missing values and later handled by validation.

### Step 7 — Validation

`validator.py` checks whether records satisfy the required rules.

Examples:

* Missing Employee ID
* Missing Employee Name
* Invalid Age
* Invalid Email
* Invalid Employee ID reference
* Invalid Department reference
* Invalid Attendance Date
* Invalid Payment Date
* Invalid Work Hours
* Invalid Overtime Hours
* Negative salary values
* Negative budget values

Each record receives:

```text
valid
rejection_reason
```

Example:

```text
valid = False
rejection_reason = "Invalid Age"
```

Multiple validation errors can also be recorded for the same record.

### Step 8 — Transformation

`transformer.py` creates useful calculated fields.

For payroll data:

```text
Calculated Gross Salary
Calculated Net Salary
```

The calculated net salary uses:

```text
Basic Salary
+ HRA
+ Allowances
+ Bonus
+ Overtime Pay
- Deductions
```

### Step 9 — Export

`exporter.py` separates the records into:

```text
data/processed/
```

and

```text
data/rejected/
```

For example:

```text
employees_cleaned.csv
employees_rejected.csv

departments_cleaned.csv
departments_rejected.csv

attendance_cleaned.csv
attendance_rejected.csv

payroll_cleaned.csv
payroll_rejected.csv
```

## Streamlit Application

The project also includes a simple Streamlit interface.

Run:

```bash
streamlit run app.py
```

The application allows you to:

1. Upload a CSV file
2. Preview raw data
3. Clean and validate the data
4. View valid records
5. View rejected records
6. Download the cleaned CSV
7. Download the rejected CSV

## Running the Project

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd employee_data_cleaning
```

### 2. Create a virtual environment

Windows:

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the complete pipeline

```bash
python main.py
```

### 5. Run tests

```bash
pytest
```

### 6. Run the Streamlit application

```bash
streamlit run app.py
```

## Test Results

The project includes automated tests for:

* CSV reading
* Basic data cleaning
* Money conversion
* Numeric validation
* Date parsing
* Email validation
* Phone number cleaning
* Record validation

Run:

```bash
pytest
```

Expected result:

```text
8 passed
```

## Example Pipeline Result

The current test datasets produce approximately:

```text
Dataset       Valid     Rejected
--------------------------------
Employees       20         10
Departments     17          3
Attendance      30          5
Payroll         27          5
```

These numbers are based on the deliberately messy sample datasets included with the project.

## Technologies Used

* Python
* Pandas
* Pytest
* Streamlit
* OpenPyXL
* Regular Expressions
* CSV / Excel
* Git / GitHub

## What This Project Demonstrates

This project demonstrates practical data-engineering and software-development concepts:

* Data ingestion
* Data profiling
* Data cleaning
* Data normalization
* Data validation
* Data transformation
* Error handling
* Rejected-record management
* Modular Python development
* Automated testing
* File-based data pipelines
* Basic data-processing UI

## Future Improvements

Possible future improvements include:

* YAML-based configurable validation rules
* Automated data-quality reports
* Logging instead of print statements
* Database integration
* PostgreSQL support
* Batch processing of multiple files
* More advanced schema validation
* Pipeline configuration
* Data-quality dashboards
* Docker deployment
* Cloud deployment
* CI/CD with GitHub Actions

## Author

**RaviVarma Yalla**

B.Tech — Computer Science and Engineering

GitHub: `https://github.com/varma5359`

