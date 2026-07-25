import os
import pandas as pd
import matplotlib.pyplot as plt

print("=" * 60)
print("LEVEL 2 - TASK 2 : CUISINE COMBINATION ANALYSIS")
print("=" * 60)

# -------------------------------------------------
# Load Dataset
# -------------------------------------------------

df = pd.read_csv("datasets/Dataset.csv")

print("\nDataset Loaded Successfully!")

# -------------------------------------------------
# Restaurants with Multiple Cuisines
# -------------------------------------------------

multi = df[df["Cuisines"].str.contains(",", na=False)]

print("\nRestaurants Serving Multiple Cuisines:", len(multi))

# -------------------------------------------------
# Top Cuisine Combinations
# -------------------------------------------------

combo = multi["Cuisines"].value_counts().head(10)

print("\nTop 10 Cuisine Combinations")
print(combo)

# -------------------------------------------------
# Average Rating
# -------------------------------------------------

rating = (
    multi.groupby("Cuisines")["Aggregate rating"]
    .mean()
    .sort_values(ascending=False)
    .head(10)
)

print("\nTop 10 Cuisine Combinations by Average Rating")
print(rating)

# -------------------------------------------------
# Output Folder
# -------------------------------------------------

os.makedirs("output", exist_ok=True)

combo.to_csv("output/cuisine_combinations.csv")
rating.to_csv("output/cuisine_combination_ratings.csv")

# -------------------------------------------------
# Plot 1
# -------------------------------------------------

plt.figure(figsize=(12,6))

plt.barh(combo.index, combo.values)

plt.title("Top 10 Cuisine Combinations")
plt.xlabel("Number of Restaurants")

plt.tight_layout()

plt.savefig("output/cuisine_combinations.png")
plt.close()

# -------------------------------------------------
# Plot 2
# -------------------------------------------------

plt.figure(figsize=(12,6))

plt.barh(rating.index, rating.values)

plt.title("Top 10 Cuisine Combinations by Average Rating")
plt.xlabel("Average Rating")

plt.tight_layout()

plt.savefig("output/cuisine_combination_ratings.png")
plt.close()

print("\nCharts Saved!")
print("CSV Files Saved!")

print("\nTASK COMPLETED SUCCESSFULLY!")