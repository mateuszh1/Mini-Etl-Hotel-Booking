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

def remove_duplicates(df):
    df = df.drop_duplicates()
    return df

df = load_data(INPUT_PATH)
df = standardize_column_names(df)

stats_before = get_data_quality_stats(df)

df = remove_duplicates(df)

stats_after = get_data_quality_stats(df)

print("CSV loaded successfully")
print("Stats before cleaning:")
print(stats_before)


print("\nStats after removing duplicates:")
print(stats_after)