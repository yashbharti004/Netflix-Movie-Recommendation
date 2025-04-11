import pandas as pd

df = pd.read_csv("data/flixpatrol_fully_cleaned.csv")

genre = input("Enter preferred genre: ")
year_min = int(input("Enter start year: "))
year_max = int(input("Enter end year: "))

recommendations = df[(df["Genre"].str.contains(genre, case=False, na=False)) & 
                     (df["Premiere"].between(year_min, year_max))].sort_values(by="Watchtime in Million", ascending=False).head(5)

print("\nRecommended Movies/TV Shows:\n", recommendations[["Title", "Watchtime in Million"]])
