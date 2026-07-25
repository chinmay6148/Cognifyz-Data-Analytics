import os
import pandas as pd
import matplotlib.pyplot as plt

print("=" * 60)
print("LEVEL 2 - TASK 4 : RESTAURANT CHAINS ANALYSIS")
print("=" * 60)

# -------------------------------------------------
# Load Dataset
# -------------------------------------------------

df = pd.read_csv("datasets/Dataset.csv")

print("\nDataset Loaded Successfully!")

# -------------------------------------------------
# Find Restaurant Chains
# -------------------------------------------------

chains = (
    df["Restaurant Name"]
    .value_counts()
)

chains = chains[chains > 1].head(10)

print("\nTop Restaurant Chains")
print(chains)

# -------------------------------------------------
# Average Rating
# -------------------------------------------------

ratings = (
    df.groupby("Restaurant Name")["Aggregate rating"]
    .mean()
)

top_chain_ratings = ratings.loc[chains.index]

print("\nAverage Ratings")
print(top_chain_ratings)

# -------------------------------------------------
# Create Output Folder
# -------------------------------------------------

os.makedirs("output", exist_ok=True)

chains.to_csv("output/top_restaurant_chains.csv")
top_chain_ratings.to_csv("output/top_chain_ratings.csv")

# -------------------------------------------------
# Chart 1
# -------------------------------------------------

plt.figure(figsize=(10,6))

plt.barh(chains.index, chains.values)

plt.title("Top Restaurant Chains")
plt.xlabel("Number of Outlets")

plt.tight_layout()

plt.savefig("output/top_restaurant_chains.png")
plt.close()

# -------------------------------------------------
# Chart 2
# -------------------------------------------------

plt.figure(figsize=(10,6))

plt.barh(top_chain_ratings.index, top_chain_ratings.values)

plt.title("Average Rating of Top Restaurant Chains")
plt.xlabel("Average Rating")

plt.tight_layout()

plt.savefig("output/top_chain_ratings.png")
plt.close()

print("\nCharts Saved!")
print("CSV Files Saved!")

print("\nTASK COMPLETED SUCCESSFULLY!")