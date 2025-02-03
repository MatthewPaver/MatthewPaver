# Big Data Analytics Assignments

This repository contains the assignments for the Big Data Analytics course. Below are the details and instructions for each assignment.

## Assignment 1: GPS Trajectory Data Analysis

### Description
This assignment involves analyzing GPS trajectory data from the Geolife project using PySpark. The tasks include converting timestamps, filtering records, calculating data points, and more.

### Requirements
- PySpark 3.5.3
- Python 3.10.12
- Ensure the file `dataset.txt` is in the same directory as the script.

### Instructions for Running
1. Open the script `Assignment 1.py` in your desired IDE.
2. Ensure the `dataset.txt` file is in the same directory.
3. Run the script to execute the code.

### Tasks
1. Convert timestamps to local time zone based on longitude.
2. Filter records within Beijing's borders.
3. Calculate the number of days each user recorded more than 10 data points.
4. Calculate the number of weeks each user recorded more than 100 data points.
5. Find the northernmost point for each user.
6. Calculate daily altitude span for each user.
7. Calculate total distance travelled per day for each user.

## Assignment 2: Stock Data Analysis

### Description
This assignment involves analyzing stock data using various data processing and machine learning techniques, including PCA (Principal Component Analysis).

### Requirements
- pandas
- numpy
- scikit-learn
- matplotlib

### Instructions for Running
1. Ensure the `stockdata.csv` file is in the same directory as the script.
2. Run the script `Assignment_2.py` to execute the code.

### Tasks
1. Load the stock data.
2. Identify and sort all stock names.
3. Filter data for names meeting the date criteria.
4. Identify common dates and filter.
5. Create a DataFrame of 'close' values.
6. Calculate returns.
7. Perform PCA.
8. Plot explained variance ratio.
9. Plot cumulative variance.
10. Normalize data and repeat PCA.

### Notes
- The script will output various results and plots as specified in the tasks.
- Ensure all required libraries are installed before running the scripts.
