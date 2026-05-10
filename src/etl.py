import pandas as pd
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

INPUT_PATH = BASE_DIR / "input" / "hotel_booking.csv"
OUTPUT_PATH = BASE_DIR / "output" / "cleaned_hotel_booking.csv"
REPORT_PATH = BASE_DIR / "output" / "etl_report.txt"


def load_data(file_path):
    df = pd.read_csv(file_path)
    return df

def save_data(df, output_path):
   output_path.parent.mkdir(parents=True, exist_ok=True)
   df.to_csv(output_path, index=False)


def standardize_column_names(df):
    df.columns = (

        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
        .str.replace("-", "_")
    )
    return df


def get_data_quality_stats(df):
    stats = {
        "total_rows": len(df),
        "total_columns": len(df.columns),
        "missing_values": df.isnull().sum().to_dict(),
        "duplicate_rows": df.duplicated().sum()
    }
    return stats

def remove_duplicates(df):
    df = df.drop_duplicates()
    return df


def handle_missing_values(df):
    df["children"] = df["children"].fillna(0)
    df["country"] = df["country"].fillna("Unknown")
    df["agent"] = df["agent"].fillna(0)
    df["company"] = df["company"].fillna(0)
    return df

def save_report(report, report_path):
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(report)


def generate_report(stats_before, stats_after):
    report = f"""
    ETL Report
    Rows before cleaning: {stats_before['total_rows']}
    Rows after cleaning: {stats_after['total_rows']}

    Columns before cleaning: {stats_before['total_columns']}
    columns after cleaning: {stats_after['total_columns']}

    Missing values before cleaning: {stats_before['missing_values']}
    Missing values after cleaning: {stats_after['missing_values']}

    Duplicate rows before cleaning: {stats_before['duplicate_rows']}
    Duplicate rows after cleaning: {stats_after['duplicate_rows']}
    
    Columns with missing values before cleaning: {stats_before['missing_values']}
    Columns with missing values after cleaning: {stats_after['missing_values']}

    """
    return report

df = load_data(INPUT_PATH)
df = standardize_column_names(df)

stats_before = get_data_quality_stats(df)

df = remove_duplicates(df)
df = handle_missing_values(df)

stats_after = get_data_quality_stats(df)
save_data(df, OUTPUT_PATH)

report = generate_report(stats_before, stats_after)
save_report(report, REPORT_PATH)



print("CSV loaded successfully")
print("ETL finished successfully")
print(f"Clean data saved to: {OUTPUT_PATH}")
print(f"Report saved to: {REPORT_PATH}")