import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = r"C:\Users\hetri\OneDrive\Desktop\Task_05_Descriptive_Stats\netflix_titles.csv"
df = pd.read_csv(file_path)

# Drop duplicates and handle missing values
df.drop_duplicates(inplace=True)
df['date_added'] = pd.to_datetime(df['date_added'].str.strip(), errors='coerce')
df['year_added'] = df['date_added'].dt.year
df['month_added'] = df['date_added'].dt.month
df['country'] = df['country'].fillna('Unknown')
df['rating'] = df['rating'].fillna('Unrated')

# Descriptive statistics
print("Total entries:", len(df))
print("Content type counts:\n", df['type'].value_counts())
print("Top 5 countries:\n", df['country'].value_counts().head(5))
print("Top 5 genres:\n", df['listed_in'].value_counts().head(5))
print("Content added per year:\n", df['year_added'].value_counts().sort_index())

# Plot: Content Added Over Time
df['year_added'].value_counts().sort_index().plot(kind='bar', title='Content Added Per Year')
plt.xlabel("Year")
plt.ylabel("Number of Titles")
plt.tight_layout()
plt.savefig("content_added_per_year.png")
plt.show()
