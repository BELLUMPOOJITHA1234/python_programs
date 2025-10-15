import numpy as np

# Create a sample NumPy array
data = np.array([12, 5, 25, 7, 30, 18, 9, 45, 15])

# Define the range to filter by
min_val = 10
max_val = 20

print("Original array:", data)
print(f"Filtering for numbers between {min_val} and {max_val}...")

# Use boolean indexing to create a mask for elements in the range
filtered_data = data[(data > min_val) & (data < max_val)]

print("Extracted numbers:", filtered_data)
