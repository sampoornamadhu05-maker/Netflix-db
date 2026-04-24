import pandas as pd
import matplotlib.pyplot as plt

# -------------------------
# Load BOTH datasets
# -------------------------
movies_data = pd.read_csv("netflix_movies_detailed_up_to_2025.csv")
tvshows_data = pd.read_csv("netflix_tv_shows_detailed_up_to_2025.csv")

# -------------------------
# Basic Information
# -------------------------
print("Movies Dataset Info")
print("Total Movies:", len(movies_data))
print("\nTop 5 Movie Countries:")
print(movies_data["country"].value_counts().head())

print("\n-----------------------------\n")

print("TV Shows Dataset Info")
print("Total TV Shows:", len(tvshows_data))
print("\nTop 5 TV Show Countries:")
print(tvshows_data["country"].value_counts().head())

# -------------------------
# Count for plotting
# -------------------------
movies_count = len(movies_data)
tvshows_count = len(tvshows_data)

# -------------------------
# Bar Chart
# -------------------------
labels = ["Movies", "TV Shows"]
counts = [movies_count, tvshows_count]

plt.figure()
plt.bar(labels, counts)
plt.xlabel("Type")
plt.ylabel("Count")
plt.title("Movies vs TV Shows")
plt.show()