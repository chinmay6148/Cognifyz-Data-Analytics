import os
import pandas as pd
import matplotlib.pyplot as plt

print('='*60)
print('LEVEL 1 - TASK 2 : CITY ANALYSIS')
print('='*60)

# -------------------------------------------------
# Load Dataset
# -------------------------------------------------
df = pd.read_csv('datasets/Dataset.csv')

print('\nDataset Loaded Successfully!')

# -------------------------------------------------
# Top 5 cities with most restaurants
# -------------------------------------------------
city_counts = df['City'].value_counts().head(5)

print('\nTop 5 Cities by Number of Restaurants')
print(city_counts)

# -------------------------------------------------
# Average rating by city (minimum 20 restaurants)
# -------------------------------------------------
city_stats = (
    df.groupby('City')
      .agg(Restaurant_Count=('Restaurant ID', 'count'),
           Avg_Rating=('Aggregate rating', 'mean'))
)

top_rated_cities = (
    city_stats[city_stats['Restaurant_Count'] >= 20]
    .sort_values('Avg_Rating', ascending=False)
    .head(5)
)

print('\nTop 5 Cities by Average Rating (min 20 restaurants)')
print(top_rated_cities)

# -------------------------------------------------
# Create output folder
# -------------------------------------------------
os.makedirs('output', exist_ok=True)

# Save CSV files
city_counts.to_csv('output/top_cities.csv')
top_rated_cities.to_csv('output/top_rated_cities.csv')

# -------------------------------------------------
# Bar chart - Top 5 cities
# -------------------------------------------------
plt.figure(figsize=(8,5))
plt.bar(city_counts.index, city_counts.values)
plt.title('Top 5 Cities by Number of Restaurants')
plt.xlabel('City')
plt.ylabel('Number of Restaurants')
plt.xticks(rotation=15)
plt.tight_layout()
plt.savefig('output/top_cities.png')
plt.close()

# -------------------------------------------------
# Bar chart - Top Rated Cities
# -------------------------------------------------
plt.figure(figsize=(8,5))
plt.bar(top_rated_cities.index, top_rated_cities['Avg_Rating'])
plt.title('Top 5 Cities by Average Rating')
plt.xlabel('City')
plt.ylabel('Average Rating')
plt.xticks(rotation=15)
plt.tight_layout()
plt.savefig('output/top_rated_cities.png')
plt.close()

print('Top Rated Cities Chart Saved!')

print('\nBar Chart Saved!')
print('CSV Files Saved!')
print('\nTASK COMPLETED SUCCESSFULLY!')