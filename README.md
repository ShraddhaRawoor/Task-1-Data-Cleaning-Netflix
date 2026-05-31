# Task 1 - Data Cleaning and Preprocessing

## Objective

The objective of this task is to clean and preprocess the Netflix Movies and TV Shows dataset using Python and Pandas.

## Dataset

Netflix Movies and TV Shows Dataset

## Tools Used

* Python
* Pandas
* VS Code

## Data Cleaning Steps Performed

1. Loaded the dataset using Pandas.
2. Checked for missing values using `isnull()`.
3. Removed duplicate records using `drop_duplicates()`.
4. Standardized column names:

   * Converted to lowercase
   * Replaced spaces with underscores
5. Filled missing values in:

   * director
   * cast
   * country
   * rating
   * duration
6. Converted `date_added` column to datetime format.
7. Removed leading and trailing spaces from text columns.
8. Exported the cleaned dataset.

## Files Included

* netflix_titles.csv
* cleaned_netflix_titles.csv
* task1.py
* README.md
* summary.txt

## Outcome

The dataset was successfully cleaned and prepared for further analysis and visualization.


DATA CLEANING SUMMARY

Dataset Name: Netflix Movies and TV Shows

Total Records: 8807
Total Columns: 12

Cleaning Actions Performed:

1. Checked missing values.
2. Removed duplicate rows.
3. Standardized column names.
4. Filled missing values in:
   - Director
   - Cast
   - Country
   - Rating
   - Duration
5. Converted date_added column into datetime format.
6. Trimmed unnecessary spaces in text columns.
7. Verified data types and data quality.

Result:

The dataset is now clean, consistent, and ready for analysis or machine learning tasks.
