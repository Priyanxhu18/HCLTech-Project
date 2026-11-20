# Parkinson Voice Measurements EDA

**Student:** Priyanshu Singh  
**Class / Section:** CSE 11  
**Course:** B.Tech - Computer Science and Engineering  
**Project Type:** Individual project

## 1. Introduction

This project performs Exploratory Data Analysis (EDA) on the supplied Parkinson voice-measurement dataset. It uses Python, NumPy, Pandas and Matplotlib to inspect the data, calculate basic statistics, compare measurements by status, and create charts.

This is a basic data-analysis project. It does not train a machine-learning model, make predictions, or diagnose any person.

## 2. Objectives

- Load the supplied dataset and inspect its rows, columns and data types.
- Check for missing values and duplicate rows.
- Calculate mean, median, minimum and maximum for selected measurements using NumPy.
- Use Pandas to count, filter, sort and group records.
- Compare selected measurement averages by status.
- Create two charts and record three observations from the data.

## 3. Dataset Description

- **Dataset:** Parkinsons Disease Data Set (Oxford Parkinson's Disease Detection Dataset)
- **Source:** [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/174/parkinsons)
- **File used:** `parkinsons.data`
- **Rows in the supplied file:** 195
- **Columns in the supplied file:** 24
- **Status field:** 0 = healthy; 1 = Parkinson's disease, as described in `parkinsons.names`.

The supplied `parkinsons.data` file is used as it is. Its actual row and column counts are read by the Python program. The metadata at the beginning of `parkinsons.names` lists 197 instances and 23 attributes, while its detailed dataset description refers to 195 recordings. The supplied data file itself contains 195 rows and 24 columns, so those are the counts reported by this project.

## 4. Technologies Used

- Python
- NumPy
- Pandas
- Matplotlib

## 5. Project Structure

```text
Parkinson-Voice-Measurements-EDA/
|
|-- parkinsons_eda.py
|-- parkinsons.data
|-- parkinsons.names
|-- README.md
|-- requirements.txt
|-- .gitignore
`-- Priyanshu_Singh_Parkinsons_EDA_SRS.docx
```

The `eda_outputs` folder is not included in the starter ZIP. It is created automatically when you run the Python program.

## 6. Installation Requirements

Install Python 3 and open Command Prompt or the VS Code terminal in the project folder. On this Windows setup, the Python launcher command `py` is used.

Install the required packages:

```powershell
py -m pip install -r requirements.txt
```

## 7. How to Run

Keep `parkinsons_eda.py` and `parkinsons.data` in the same folder. Run:

```powershell
py parkinsons_eda.py
```

The program displays the analysis in the terminal and opens the two charts. Close the chart windows to let the program finish. The CSV files and PNG charts are saved in `eda_outputs`.

## 8. Analysis Performed

1. Display the first and last five rows using `head()` and `tail()`.
2. Display the dataset shape, information and descriptive summary.
3. Check missing values and duplicate rows.
4. Count records in each status group using `value_counts()`.
5. Filter records where `status` is 1.
6. Use NumPy arrays to calculate mean, median, minimum and maximum for `MDVP:Fo(Hz)`, `MDVP:Jitter(%)` and `MDVP:Shimmer`.
7. Compare the selected averages by status using `groupby()`.
8. Sort records by `MDVP:Shimmer` and save the top 10 records.
9. Create a status-count bar chart and an `MDVP:Shimmer` histogram.

## 9. Key Findings

The following findings are based on the supplied `parkinsons.data` file:

- The file contains **195 records and 24 columns**.
- It contains **48 records with status 0** and **147 records with status 1**.
- The average `MDVP:Shimmer` is approximately **0.017615** for status 0 and **0.033658** for status 1.
- The inspection finds **0 missing values** and **0 fully duplicated rows**.

These are descriptive observations about this dataset only. They do not show that a measurement causes a condition or provide a medical diagnosis.

## 10. Generated Outputs

The program creates these files inside `eda_outputs`:

- `average_measurements_by_status.csv` - average selected measurements for each status group.
- `dataset_column_summary.csv` - column names, data types and missing-value counts.
- `top_10_shimmer_records.csv` - ten records with the highest `MDVP:Shimmer` values.
- `status_count_bar_chart.png` - number of records in each status group.
- `shimmer_histogram.png` - distribution of `MDVP:Shimmer` values.

## 11. Limitations

- The project uses only the supplied dataset and performs basic descriptive analysis.
- The data contains repeated voice recordings from 31 people; a row represents a recording, not a separate person.
- The dataset is relatively small and may not represent all people or all recording conditions.
- The status field is used as supplied in the dataset. This project does not validate clinical status.
- No machine-learning model, prediction, diagnosis or clinical recommendation is included.

## 12. References

1. UCI Machine Learning Repository, [Parkinsons Disease Data Set](https://archive.ics.uci.edu/dataset/174/parkinsons).
2. `parkinsons.names`, dataset description file supplied with the assignment.
3. `Project Details - Google Sheets.pdf`, project requirements supplied for the assignment.
