import pandas as pd    
import numpy as np
import matplotlib.pyplot as plt

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

# Fill NaN scores for visualization
df['score'].fillna(df['score'].mean(), inplace=True)

# Create a figure with multiple subplots
plt.figure(figsize=(16,12))

# 1. Line plot
plt.subplot(2,3,1)
plt.plot(df['name'], df['score'], marker='o', linestyle='-', color='b')
plt.title('Line Plot of Scores')
plt.xlabel('Name')
plt.ylabel('Score')
plt.xticks(rotation=45)

# 2. Bar plot
plt.subplot(2,3,2)
plt.bar(df['name'], df['score'], color='orange')
plt.title('Bar Plot of Scores')
plt.xlabel('Name')
plt.ylabel('Score')
plt.xticks(rotation=45)

# 3. Histogram
plt.subplot(2,3,3)
plt.hist(df['score'], bins=5, color='green', edgecolor='black')
plt.title('Histogram of Scores')
plt.xlabel('Score')
plt.ylabel('Frequency')

# 4. Box plot
plt.subplot(2,3,4)
plt.boxplot(df['score'])
plt.title('Box Plot of Scores')
plt.ylabel('Score')

# 5. Scatter plot (Score vs Attempts)
plt.subplot(2,3,5)
plt.scatter(df['attempts'], df['score'], color='red')
plt.title('Scatter Plot: Score vs Attempts')
plt.xlabel('Attempts')
plt.ylabel('Score')

plt.tight_layout()
plt.show()
