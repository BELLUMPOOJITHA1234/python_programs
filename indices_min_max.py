import numpy as np

# Create a sample 2D NumPy array
arr = np.array([[10, 20, 5],
                [15, 3, 25],
                [30, 8, 12]])

print("Original array:")
print(arr)

# Find the indices of the maximum values along each row (axis=1)
max_indices = np.argmax(arr, axis=1)

# Find the indices of the minimum values along each row (axis=1)
min_indices = np.argmin(arr, axis=1)

print("\nIndices of the maximum values along each row:", max_indices)
print("Indices of the minimum values along each row:", min_indices)

# To verify, you can use these indices to get the actual max and min values
max_values = arr[np.arange(len(arr)), max_indices]
min_values = arr[np.arange(len(arr)), min_indices]

print("\nMaximum values:", max_values)
print("Minimum values:", min_values)
