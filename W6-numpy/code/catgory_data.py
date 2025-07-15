import numpy as np

# Set a seed for reproducibility
np.random.seed(42)

# Number of samples
n_samples = 50

# Define categories
categories = ['A', 'B', 'C']

# Randomly assign categories to samples
categorical_data = np.random.choice(categories, size=n_samples)

print("Simulated Categorical Data (first 10 samples):\n", len(categorical_data))
# print("Simulated Categorical Data (first 10 samples):\n", categorical_data[:10])