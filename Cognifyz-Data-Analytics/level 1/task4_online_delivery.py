import os
import pandas as pd
import matplotlib.pyplot as plt

print("=" * 60)
print("LEVEL 1 - TASK 4 : ONLINE DELIVERY ANALYSIS")
print("=" * 60)

# -------------------------------------------------
# Load Dataset
# -------------------------------------------------

df = pd.read_csv("datasets/Dataset.csv")

print("\nDataset Loaded Successfully!")

# -------------------------------------------------
# Online Delivery Count
# -------------------------------------------------

delivery_count = df["Has Online delivery"].value_counts()

print("\nOnline Delivery Count")
print(delivery_count)

# -------------------------------------------------
# Percentage
# -------------------------------------------------

percentage = round((delivery_count / len(df)) * 100, 2)

print("\nPercentage")

for option, value in percentage.items():
    print(f"{option} : {value}%")

# -------------------------------------------------
# Average Rating
# -------------------------------------------------

rating = (
    df.groupby("Has Online delivery")["Aggregate rating"]
    .mean()
    .round(2)
)

print("\nAverage Rating")
print(rating)

# -------------------------------------------------
# Create Output Folder
# -------------------------------------------------

os.makedirs("output", exist_ok=True)

delivery_count.to_csv("output/online_delivery_count.csv")
percentage.to_csv("output/online_delivery_percentage.csv")
rating.to_csv("output/online_delivery_rating.csv")

# -------------------------------------------------
# Chart 1
# -------------------------------------------------

plt.figure(figsize=(6,5))

plt.bar(delivery_count.index, delivery_count.values)

plt.title("Restaurants Offering Online Delivery")
plt.xlabel("Online Delivery")
plt.ylabel("Number of Restaurants")

for i, value in enumerate(delivery_count.values):
    plt.text(i, value + 50, str(value), ha="center")

plt.tight_layout()

plt.savefig("output/online_delivery_bar.png")
plt.close()

# -------------------------------------------------
# Chart 2
# -------------------------------------------------

plt.figure(figsize=(6,5))

plt.bar(rating.index, rating.values)

plt.title("Average Rating vs Online Delivery")
plt.xlabel("Online Delivery")
plt.ylabel("Average Rating")

for i, value in enumerate(rating.values):
    plt.text(i, value + 0.03, str(value), ha="center")

plt.tight_layout()

plt.savefig("output/online_delivery_rating.png")
plt.close()

print("\nCharts Saved!")
print("CSV Files Saved!")

print("\nTASK COMPLETED SUCCESSFULLY!")