import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Load the data from the CSV log file
df = pd.read_csv('experiment_log.csv')

# Define the complexity function for comparison
n_values = np.linspace(1, max(df['Main Ring Size']), 100)
linear_n = n_values  # Linear complexity for O(n)

# Create the figure for plotting
plt.figure(figsize=(20, 10))

# Plot 1: Main Ring Size vs Messages
plt.subplot(2, 2, 1)
plt.scatter(df['Main Ring Size'], df['Messages'], color='blue', label='Messages')
plt.title('Main Ring Size vs Messages')
plt.xlabel('Main Ring Size')
plt.ylabel('Messages')
plt.legend()
plt.grid(True)

# Plot 2: Subnetwork Size vs Messages
plt.subplot(2, 2, 2)
plt.scatter(df['Subnetwork Size'], df['Messages'], color='green', label='Messages')
plt.title('Subnetwork Size vs Messages')
plt.xlabel('Subnetwork Size')
plt.ylabel('Messages')
plt.legend()
plt.grid(True)

# Plot 3: Number of Subnetworks vs Messages
plt.subplot(2, 2, 3)
plt.scatter(df['Number of Subnetworks'], df['Messages'], color='purple', label='Messages')
plt.title('Number of Subnetworks vs Messages')
plt.xlabel('Number of Subnetworks')
plt.ylabel('Messages')
plt.legend()
plt.grid(True)

# Plot 4: Main Ring Size vs Rounds with O(n) comparison
plt.subplot(2, 2, 4)
plt.scatter(df['Main Ring Size'], df['Rounds'], color='orange', label='Rounds')
plt.plot(n_values, linear_n, label='O(n)', linestyle='--', color='green')
plt.title('Main Ring Size vs Rounds (O(n) Complexity Comparison)')
plt.xlabel('Main Ring Size')
plt.ylabel('Rounds')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()
