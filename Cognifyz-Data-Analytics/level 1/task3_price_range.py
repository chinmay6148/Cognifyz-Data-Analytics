import os
import pandas as pd
import matplotlib.pyplot as plt

print("=" * 60)
print("LEVEL 1 - TASK 3 : PRICE RANGE DISTRIBUTION")
print("=" * 60)

# -------------------------------------------------
# Load Dataset
# -------------------------------------------------
df = pd.read_csv("datasets/Dataset.csv")

print("\nDataset Loaded Successfully!")
print(df.head())

# -------------------------------------------------
# Price Range Distribution
# -------------------------------------------------
price_counts = df["Price range"].value_counts().sort_index()

print("\nPrice Range Distribution")
print(price_counts)

# -------------------------------------------------
# Percentage Distribution
# -------------------------------------------------
percentage = round((price_counts / len(df)) * 100, 2)

print("\nPercentage Distribution")

for price, per in percentage.items():
    print(f"Price Range {price} : {per}%")

# -------------------------------------------------
# Create Output Folder
# -------------------------------------------------
os.makedirs("output", exist_ok=True)

price_counts.to_csv("output/price_range_distribution.csv")

# -------------------------------------------------
# Plot Bar Chart
# -------------------------------------------------
plt.figure(figsize=(8,5))
plt.bar(price_counts.index.astype(str), price_counts.values)

plt.title("Restaurant Price Range Distribution")
plt.xlabel("Price Range")
plt.ylabel("Number of Restaurants")

for i, value in enumerate(price_counts.values):
    plt.text(i, value + 20, str(value), ha="center")

plt.tight_layout()

plt.savefig("output/price_range_distribution.png")
plt.close()

print("\nBar Chart Saved!")
print("CSV Saved!")

print("\nTASK COMPLETED SUCCESSFULLY!")