import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np

# Create sample time-series data
dates = pd.date_range(start='2025-10-01', periods=10, freq='D')
values = np.random.randint(50, 100, size=10)
df = pd.DataFrame({'Date': dates, 'Value': values})

# Plotting the time-series data
plt.figure(figsize=(10,5))
plt.plot(df['Date'], df['Value'], marker='o', linestyle='-', color='blue')

# Customize axis labels and title
plt.xlabel('Date')
plt.ylabel('Value')
plt.title('Time-Series Data Visualization')
plt.grid(True)

# Format x-axis dates
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d-%b'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator())

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
