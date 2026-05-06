import pandas as pd
from pathlib import Path

INPUT_PATH = Path("input") / "hotel_booking.csv"

df = pd.read_csv(INPUT_PATH)

print(INPUT_PATH)
print(INPUT_PATH.exists())
print("CSV file loaded successfully!")
print(f"Rows: {len(df)}")
print(f"Columns: {len(df.columns)}")
print(df.head())