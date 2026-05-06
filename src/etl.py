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

df = load_data(INPUT_PATH)
df = standardize_column_names(df)

print("CSV file loaded successfully!")

print("\nColumn names after cleaning:")
print(df.columns.tolist())