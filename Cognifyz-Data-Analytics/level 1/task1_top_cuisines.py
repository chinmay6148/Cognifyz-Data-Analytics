import os
import pandas as pd
import matplotlib.pyplot as plt

print("="*60)
print("LEVEL 1 - TASK 1 : TOP CUISINES")
print("="*60)

# ----------------------------------------
# Load Dataset
# ----------------------------------------

df = pd.read_csv("datasets/Dataset.csv")

print("\nDataset Loaded Successfully!")
print(df.head())

# ----------------------------------------
# Check Columns
# ----------------------------------------

print("\nColumns in Dataset:")
print(df.columns)

# ----------------------------------------
# Split Multiple Cuisines
# ----------------------------------------

all_cuisines = (
    df["Cuisines"]
    .dropna()
    .str.split(", ")
    .explode()
)

# ----------------------------------------
# Count Cuisines
# ----------------------------------------

top_cuisines = all_cuisines.value_counts().head(3)

print("\nTop 3 Cuisines")
print(top_cuisines)

# ----------------------------------------
# Percentage
# ----------------------------------------

percentage = (
    top_cuisines / len(df)
) * 100

print("\nPercentage of Restaurants")

for cuisine, value in percentage.items():
    print(f"{cuisine} : {value:.2f}%")

# ----------------------------------------
# Save Output
# ----------------------------------------

os.makedirs("Output", exist_ok=True)

top_cuisines.to_csv(
    "Output/top_cuisines.csv"
)

# ----------------------------------------
# Plot
# ----------------------------------------

plt.figure(figsize=(8,5))

plt.bar(
    top_cuisines.index,
    top_cuisines.values
)

plt.title("Top 3 Most Common Cuisines")

plt.xlabel("Cuisine")

plt.ylabel("Number of Restaurants")

plt.xticks(rotation=15)

plt.tight_layout()

plt.savefig(
    "Output/top_cuisines.png"
)

plt.close()

print("\nBar Chart Saved!")

print("\nCSV Saved!")

print("\nTASK COMPLETED SUCCESSFULLY!")