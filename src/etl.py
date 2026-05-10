import pandas as pd
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

INPUT_PATH = BASE_DIR / "input" / "hotel_booking.csv"
OUTPUT_PATH = BASE_DIR / "output" / "cleaned_hotel_booking.csv"


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

df = load_data(INPUT_PATH)
df = standardize_column_names(df)

stats_before = get_data_quality_stats(df)

df = remove_duplicates(df)

stats_after = get_data_quality_stats(df)
save_data(df, OUTPUT_PATH)

print("CSV loaded successfully")
print("Stats before cleaning:")
print(stats_before)


print("\nStats after removing duplicates:")
print(stats_after)
print("\n Clean data saved to {OUTPUT_PATH}")