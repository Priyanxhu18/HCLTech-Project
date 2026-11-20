"""Parkinson Voice Measurements EDA

This program performs basic Exploratory Data Analysis (EDA) on the supplied
parkinsons.data file. It uses NumPy, Pandas and Matplotlib.

This is an educational EDA project only. It does not diagnose or predict
Parkinson's disease.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Find the folder containing this Python file.
project_folder = Path(__file__).resolve().parent

# Set the locations of the dataset and output folder.
data_file = project_folder / "parkinsons.data"
output_folder = project_folder / "eda_outputs"
output_folder.mkdir(exist_ok=True)

# Stop with a clear message if the dataset is not in the project folder.
if not data_file.exists():
    raise FileNotFoundError(
        "parkinsons.data was not found. Keep it in the same folder as this script."
    )

# 1. Load the dataset using Pandas.
df = pd.read_csv(data_file)

print("\n===== FIRST FIVE ROWS =====")
print(df.head())

print("\n===== LAST FIVE ROWS =====")
print(df.tail())

print("\n===== DATASET SHAPE (ROWS, COLUMNS) =====")
print(df.shape)

print("\n===== DATASET INFORMATION =====")
df.info()

print("\n===== NUMERICAL SUMMARY =====")
print(df.describe())

# 2. Check the dataset for missing values and duplicate rows.
print("\n===== MISSING VALUES BY COLUMN =====")
missing_values = df.isnull().sum()
print(missing_values)
print("Total missing values:", int(missing_values.sum()))

duplicate_count = int(df.duplicated().sum())
print("Duplicate rows:", duplicate_count)

# 3. Count the records in each status group.
# In the supplied dataset, 0 means healthy and 1 means Parkinson's disease.
print("\n===== STATUS COUNTS =====")
status_counts = df["status"].value_counts().sort_index()
print(status_counts)
print("Status meaning: 0 = healthy, 1 = Parkinson's disease (dataset label).")

# 4. Use Pandas filtering to display records with status 1.
print("\n===== FIRST FIVE RECORDS WITH STATUS 1 =====")
status_1_records = df[df["status"] == 1]
print(status_1_records.head())

# 5. Use NumPy to calculate statistics for three selected measurements.
selected_columns = ["MDVP:Fo(Hz)", "MDVP:Jitter(%)", "MDVP:Shimmer"]

print("\n===== NUMPY STATISTICS =====")
for column in selected_columns:
    # Convert the selected Pandas column into a NumPy array.
    values = df[column].dropna().to_numpy()

    print("\n", column)
    print("Mean:", np.mean(values))
    print("Median:", np.median(values))
    print("Minimum:", np.min(values))
    print("Maximum:", np.max(values))

# 6. Compare the average selected measurements for each status group.
print("\n===== AVERAGE MEASUREMENTS BY STATUS =====")
group_means = df.groupby("status")[selected_columns].mean()
print(group_means)

# Save the group averages as a CSV file.
group_means.reset_index().to_csv(
    output_folder / "average_measurements_by_status.csv", index=False
)

# 7. Sort the data and display the 10 highest MDVP:Shimmer records.
print("\n===== TOP 10 RECORDS BY MDVP:SHIMMER =====")
top_10_records = df.sort_values(
    by="MDVP:Shimmer", ascending=False
).head(10)
print(top_10_records[["name", "MDVP:Shimmer", "status"]].to_string(index=False))

# Save the 10 records as a CSV file.
top_10_records.to_csv(
    output_folder / "top_10_shimmer_records.csv", index=False
)

# 8. Save a summary of the dataset columns and their data types.
column_summary = pd.DataFrame(
    {
        "column": df.columns,
        "data_type": [str(data_type) for data_type in df.dtypes],
        "missing_values": missing_values.values,
    }
)
column_summary.to_csv(
    output_folder / "dataset_column_summary.csv", index=False
)

# 9. Create a bar chart showing the number of records in each status group.
plt.figure(figsize=(7, 5))
status_labels = status_counts.rename(
    index={0: "Healthy (0)", 1: "Parkinson's (1)"}
)
status_labels.plot(kind="bar")
plt.title("Number of Voice Records by Status")
plt.xlabel("Status group")
plt.ylabel("Number of records")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig(output_folder / "status_count_bar_chart.png", dpi=150)

# 10. Create a histogram showing the distribution of MDVP:Shimmer values.
plt.figure(figsize=(7, 5))
plt.hist(df["MDVP:Shimmer"].dropna(), bins=15, edgecolor="black")
plt.title("Distribution of MDVP:Shimmer")
plt.xlabel("MDVP:Shimmer")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig(output_folder / "shimmer_histogram.png", dpi=150)

# Display both charts. Close the chart windows to let the program finish.
plt.show()

# 11. Print three observations based on the supplied dataset.
print("\n===== THREE DATA OBSERVATIONS =====")
print(
    f"1. The supplied dataset contains {len(df)} records and "
    f"{df.shape[1]} columns."
)

if 0 in status_counts.index and 1 in status_counts.index:
    print(
        f"2. There are {int(status_counts.loc[0])} records with status 0 "
        f"and {int(status_counts.loc[1])} records with status 1."
    )

if 0 in group_means.index and 1 in group_means.index:
    print(
        "3. The average MDVP:Shimmer is "
        f"{group_means.loc[0, 'MDVP:Shimmer']:.6f} for status 0 and "
        f"{group_means.loc[1, 'MDVP:Shimmer']:.6f} for status 1."
    )

print("\nAnalysis complete. Check the eda_outputs folder for the saved files.")
