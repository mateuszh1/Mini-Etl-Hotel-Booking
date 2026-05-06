import pandas as pd
from pathlib import Path

INPUT_PATH = Path("input") / "hotel_booking.csv"

df = pd.read_csv(INPUT_PATH)


df.columns = (

    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
    .str.replace("-", "_")
)

print("CSV file loaded successfully!")

print("\nColumn names after cleaning:")
print(df.columns.tolist())