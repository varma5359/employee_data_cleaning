from .reader import read_file
from .profiler import profile_data
from .cleaner import clean_data
from .string_cleaner import clean_strings
from .numeric_cleaner import clean_numbers
from .date_cleaner import clean_dates
from .validator import validate_data
from .transformer import transform_data
from .exporter import export_data


def run_pipeline(input_path,output_path,rejected_path=None,employee_ids=None,department_ids=None):
    """Run the complete cleaning pipeline for one dataset."""
    df=read_file(input_path)
    print("\n===== RAW DATA =====")
    profile_data(df)
    df=clean_data(df)
    df=clean_strings(df)
    df=clean_numbers(df)
    df=clean_dates(df)
    df=validate_data(df,employee_ids,department_ids)
    df=transform_data(df)
    export_data(df,output_path,rejected_path)
    return df