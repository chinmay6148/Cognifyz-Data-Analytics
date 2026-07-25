import os
import pandas as pd
import matplotlib.pyplot as plt

print("=" * 60)
print("LEVEL 2 - TASK 1 : RESTAURANT RATINGS")
print("=" * 60)

# -------------------------------------------------
# Load Dataset
# -------------------------------------------------

df = pd.read_csv("datasets/Dataset.csv")

print("\nDataset Loaded Successfully!")

# -------------------------------------------------
# Basic Statistics
# -------------------------------------------------

average_rating = round(df["Aggregate rating"].mean(), 2)

print(f"\nAverage Restaurant Rating : {average_rating}")

# -------------------------------------------------
# Rating Distribution
# -------------------------------------------------

rating_counts = (
    df["Aggregate rating"]
    .value_counts()
    .sort_index()
)

print("\nRating Distribution")
print(rating_counts)

# -------------------------------------------------
# Rating Text Distribution
# -------------------------------------------------

rating_text = df["Rating text"].value_counts()

print("\nRating Category Distribution")
print(rating_text)

# -------------------------------------------------
# Most Common Rating
# -------------------------------------------------

most_common = rating_counts.idxmax()

print(f"\nMost Common Rating : {most_common}")

# -------------------------------------------------
# Create Output Folder
# -------------------------------------------------

os.makedirs("output", exist_ok=True)

rating_counts.to_csv("output/rating_distribution.csv")
rating_text.to_csv("output/rating_text_distribution.csv")

# -------------------------------------------------
# Histogram
# -------------------------------------------------

plt.figure(figsize=(8,5))

plt.hist(
    df["Aggregate rating"],
    bins=10,
    edgecolor="black"
)

plt.title("Restaurant Rating Distribution")
plt.xlabel("Aggregate Rating")
plt.ylabel("Number of Restaurants")

plt.tight_layout()

plt.savefig("output/rating_histogram.png")
plt.close()

# -------------------------------------------------
# Rating Text Bar Chart
# -------------------------------------------------

plt.figure(figsize=(8,5))

plt.bar(
    rating_text.index,
    rating_text.values
)

plt.title("Rating Categories")
plt.xlabel("Rating")
plt.ylabel("Number of Restaurants")

plt.xticks(rotation=20)

plt.tight_layout()

plt.savefig("output/rating_category.png")
plt.close()

print("\nCharts Saved!")
print("CSV Files Saved!")

print("\nTASK COMPLETED SUCCESSFULLY!")