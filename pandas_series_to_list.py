import pandas as pd

# Create a Pandas Series
series = pd.Series([10, 20, 30, 40, 50])

# Convert Series to Python list
py_list = series.tolist()

# Display the Python list and its type
print("Python List:", py_list)
print("Type:", type(py_list))
