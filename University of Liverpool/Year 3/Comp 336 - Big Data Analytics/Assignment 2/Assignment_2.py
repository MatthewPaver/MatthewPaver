# Import necessary libraries
import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import os

# Task 1: Load the data
# Change the current working directory to the directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "stockdata.csv")
data = pd.read_csv(file_path)
print("Task 1: Data loaded successfully into a DataFrame")
print(data.head())  # Display the first few rows of the DataFrame

# Task 2: Identify and sort all stock names
all_names = sorted(data['Name'].unique())
num_names = len(all_names)
first_5_names = all_names[:5]
last_5_names = all_names[-5:]
print(f"Task 2a: {all_names}")
print(f"Task 2b: Total number of names: {num_names}")
print(f"Task 2c: First 5 names: {first_5_names}, Last 5 names: {last_5_names}")

# Task 3: Filter data for names meeting the date criteria
data['date'] = pd.to_datetime(data['date'])
min_date = pd.Timestamp('2019-11-01')
max_date = pd.Timestamp('2022-10-31')

grouped = data.groupby('Name')
valid_names = [
    name for name, group in grouped
    if group['date'].min() <= min_date and group['date'].max() >= max_date
]
removed_names = set(all_names) - set(valid_names)
print(f"Task 3b: Removed names: {removed_names}")
print(f"Task 3c: Remaining valid names: {len(valid_names)}")

# Task 4: Identify common dates and filter
filtered_data = data[data['Name'].isin(valid_names)]

# Identify common dates where all valid stocks have data
common_dates = (
    filtered_data.groupby('date')['Name']
    .nunique()
    .reset_index()
)

# Ensure 'common_dates' is in datetime format
common_dates['date'] = pd.to_datetime(common_dates['date'])

# Filter dates where all valid stocks have data
valid_date_count = len(valid_names)
common_dates = common_dates[common_dates['Name'] == valid_date_count]['date']

# Filter dates based on the required range
filtered_dates = common_dates[
    (common_dates >= min_date) & (common_dates <= max_date)
]

# Check if filtered_dates is empty
if filtered_dates.empty:
    print("Warning: No common dates found after filtering!")

# Convert dates to a more readable format
filtered_dates = filtered_dates.dt.strftime('%Y-%m-%d')

# Calculate remaining dates and extract first/last 5 dates
num_remaining_dates = len(filtered_dates)
first_5_dates = filtered_dates[:5]
last_5_dates = filtered_dates[-5:]

# Print results
print(f"Task 4c: Remaining dates: {num_remaining_dates}")
print(f"Task 4d: First 5 dates: {list(first_5_dates)}, Last 5 dates: {list(last_5_dates)}")

# Task 5: Create a DataFrame of 'close' values
pivot_data = filtered_data.pivot(index='date', columns='Name', values='close')
pivot_data = pivot_data.loc[filtered_dates]
print("Task 5b: Close value DataFrame:")
print(pivot_data)

# Task 6: Calculate returns
returns = pivot_data.pct_change().dropna()
print("Task 6b: Returns DataFrame:")
print(returns)

# Task 7: Perform PCA
pca = PCA()
pca.fit(returns.fillna(0))
top_5_components = pca.components_[:5]
print("Task 7b: Top 5 principal components by eigenvalue:")
print(top_5_components)

# Task 8: Explained variance ratio and plot
explained_variance_ratio = pca.explained_variance_ratio_
first_component_variance = explained_variance_ratio[0] * 100
print(f"Task 8b: Variance explained by the first component: {first_component_variance:.2f}%")
plt.figure()
plt.bar(range(1, 21), explained_variance_ratio[:20])
plt.xlabel('Principal Component')
plt.ylabel('Explained Variance Ratio')
plt.title('Top 20 Explained Variance Ratios')
plt.axvline(x=5, color='r', linestyle='--', label='Elbow')
plt.legend()
plt.show()

# Task 9: Cumulative variance plot
cumulative_variance = np.cumsum(explained_variance_ratio)
plt.figure()
plt.plot(range(1, len(cumulative_variance) + 1), cumulative_variance, marker='o')
plt.xlabel('Principal Component')
plt.ylabel('Cumulative Variance Ratio')
plt.title('Cumulative Variance')
threshold_index = np.argmax(cumulative_variance >= 0.95) + 1
plt.axvline(x=threshold_index, color='r', linestyle='--', label='95% Threshold')
plt.legend()
plt.show()

# Task 10: Normalise data and repeat PCA
normalised_returns = (returns - returns.mean()) / returns.std()
pca_normalised = PCA()
pca_normalised.fit(normalised_returns.fillna(0))
explained_variance_normalised = pca_normalised.explained_variance_ratio_
cumulative_variance_normalised = np.cumsum(explained_variance_normalised)
threshold_index_normalised = np.argmax(cumulative_variance_normalised >= 0.95) + 1

# Repeat plots for normalised data
plt.figure()
plt.bar(range(1, 21), explained_variance_normalised[:20])
plt.xlabel('Principal Component')
plt.ylabel('Explained Variance Ratio')
plt.title('Top 20 Explained Variance Ratios (normalised Data)')
plt.axvline(x=5, color='r', linestyle='--', label='Elbow')
plt.legend()
plt.show()

plt.figure()
plt.plot(range(1, len(cumulative_variance_normalised) + 1), cumulative_variance_normalised, marker='o')
plt.xlabel('Principal Component')
plt.ylabel('Cumulative Variance Ratio')
plt.title('Cumulative Variance (normalised Data)')
plt.axvline(x=threshold_index_normalised, color='r', linestyle='--', label='95% Threshold')
plt.legend()
plt.show()

# Display results for cumulative variance
print(f"Task 9c: Principal component for 95% variance: {threshold_index}")
print(f"Task 10d: Principal component for 95% variance (normalised): {threshold_index_normalised}")
