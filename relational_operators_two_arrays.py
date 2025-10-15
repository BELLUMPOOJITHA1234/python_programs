import numpy as np

# Create two sample arrays
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([1, 2, 3, 4, 5.000000001])
print("Array 1:", arr1)
print("Array 2:", arr2)

# Element-wise comparisons
print("\nGreater than:", arr1 > arr2)
print("Greater than or equal to:", arr1 >= arr2)
print("Less than:", arr1 < arr2)

