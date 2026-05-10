# Mini ETL: Hotel Booking CSV Cleaner

This project is a simple ETL pipeline built with Python and pandas.

The goal of the project is to take a raw hotel booking CSV file, clean the data, save the cleaned dataset, and generate a short ETL report with information about missing values and duplicates.

## What is ETL?

ETL stands for:

- **Extract** - load data from a source
- **Transform** - clean and prepare the data
- **Load** - save the cleaned data to a target location

In this project:
input CSV → pandas cleaning pipeline → cleaned CSV + ETL report

# Technologies:
- Python
- pandas
- pathlib
- Git / GitHub

# Project structure

MiniEtl-csv/
│
├── input/
│   └── hotel_booking.csv
│
├── output/
│   ├── cleaned_hotel_booking.csv
│   └── etl_report.txt
│
├── src/
│   └── etl.py
│
├── requirements.txt
├── .gitignore
└── README.md

# Dataset
The dataset used in this project comes from Kaggle:

## Hotel Booking Dataset
https://www.kaggle.com/datasets/mojtaba142/hotel-booking

# What the pipeline does
The ETL script performs the following steps:

1. Loads the raw CSV file from the input/ folder
2. Standardizes column names
3. Checks data quality statistics
4. Removes duplicated rows
5. Handles missing values
6. Saves the cleaned CSV file to the output/ folder
7. Generates an ETL report

# How to run the project

1. Clone the repository
2. Install dependencies
3. Add the dataset
    Download the dataset from Kaggle and place it in:
        input/hotel_booking.csv