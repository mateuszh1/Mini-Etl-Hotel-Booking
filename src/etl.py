import pandas as pd
from pathlib import Path

INPUT_PATH = Path("input") / "hotel_booking.csv"


def load_data(file_path):
    df = pd.read_csv(file_path)
    return df



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

df = load_data(INPUT_PATH)
df = standardize_column_names(df)

stats = get_data_quality_stats(df)

print("CSV file loaded successfully!")
print(stats)