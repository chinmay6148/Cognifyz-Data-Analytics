import os
import pandas as pd
import matplotlib.pyplot as plt

print("=" * 60)
print("LEVEL 2 - TASK 3 : GEOGRAPHIC ANALYSIS")
print("=" * 60)

# -------------------------------------------------
# Load Dataset
# -------------------------------------------------

df = pd.read_csv("datasets/Dataset.csv")

print("\nDataset Loaded Successfully!")
print(f"Total Restaurants : {len(df)}")

# -------------------------------------------------
# Basic Information
# -------------------------------------------------

print("\nLatitude Range")
print(df["Latitude"].min(), "to", df["Latitude"].max())

print("\nLongitude Range")
print(df["Longitude"].min(), "to", df["Longitude"].max())

# -------------------------------------------------
# Create Output Folder
# -------------------------------------------------

os.makedirs("output", exist_ok=True)

# -------------------------------------------------
# Scatter Plot
# -------------------------------------------------

plt.figure(figsize=(10,7))

plt.scatter(
    df["Longitude"],
    df["Latitude"],
    alpha=0.5,
    s=12
)

plt.title("Restaurant Geographic Distribution")
plt.xlabel("Longitude")
plt.ylabel("Latitude")

plt.tight_layout()

plt.savefig("output/geographic_distribution.png")
plt.close()

# -------------------------------------------------
# Top Cities
# -------------------------------------------------

top_cities = df["City"].value_counts().head(10)

top_cities.to_csv("output/top10_cities_geographic.csv")

plt.figure(figsize=(10,6))

plt.bar(top_cities.index, top_cities.values)

plt.title("Top 10 Cities by Restaurant Count")
plt.xlabel("City")
plt.ylabel("Restaurants")

plt.xticks(rotation=45, ha="right")

plt.tight_layout()

plt.savefig("output/top10_cities.png")
plt.close()

print("\nScatter Plot Saved!")
print("Top Cities Chart Saved!")
print("CSV Saved!")

print("\nTASK COMPLETED SUCCESSFULLY!")