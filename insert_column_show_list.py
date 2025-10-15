  import pandas as pd
  import numpy as np

  # Sample dictionary data
  exam_data = {
    'name': ['Anastasia', 'Dima', 'Katherine', 'Suresh', 'Emily', 'Michael', 
             'Matthew', 'Laura', 'Kevin', 'Jonas'],
    'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
    'attempts': [1, 3, 2, 3, 2, 3, 3, 1, 2, 1],
    'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']
  }

  labels = ['a','b','c','d','e','f','g','h','i','j']

  # Create DataFrame
  df = pd.DataFrame(exam_data, index=labels)

  # i) Insert a new column 'grade'
  df['grade'] = ['A', 'C', 'B', 'B', 'C', 'A', 'B', 'C', 'D', 'A']

  # ii) Get list of column headers
  columns_list = df.columns.tolist()

  # Display updated DataFrame and column headers list
  print("Updated DataFrame with new column:")
  print(df)
  print("\nList of column headers:")
  print(columns_list)
