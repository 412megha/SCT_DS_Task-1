import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the CSV file
df = pd.read_csv('API_SP.POP.TOTL_DS2_en_csv_v2_2788888.csv', skiprows=4)

# Display basic information about the dataset
print(df.info())

# Show the first few rows of the dataset
print(df.head())

# Select the year 2020 for visualization
selected_year = '2020'

# Filter the data for the selected year and drop any NaN values
data_2020 = df[['Country Name', selected_year]].dropna()

# Sort the data by population for better visualization
data_2020_sorted = data_2020.sort_values(by=selected_year, ascending=False).head(10)

# Create a bar plot
plt.figure(figsize=(12, 8))
sns.barplot(x=selected_year, y='Country Name', data=data_2020_sorted, palette='viridis')
plt.title('Top 10 Countries by Population in 2020')
plt.xlabel('Population')
plt.ylabel('Country Name')
plt.show()