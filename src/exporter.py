import os


def export_data(df,processed_path,rejected_path=None):
    """Save cleaned valid records and rejected records."""
    os.makedirs(os.path.dirname(processed_path),exist_ok=True)
    df[df["valid"]].to_csv(processed_path,index=False)

    if rejected_path:
        os.makedirs(os.path.dirname(rejected_path),exist_ok=True)
        df[~df["valid"]].to_csv(rejected_path,index=False)

    print("\nCleaned records:",df["valid"].sum())
    print("Rejected records:",(~df["valid"]).sum())
    print("File saved:",processed_path)