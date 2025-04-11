import pandas as pd

df = pd.read_csv("data/flixpatrol_fully_cleaned.csv")

def recommend_by_genre(genre, year_range):
    filtered = df[(df["Genre"].str.contains(genre, case=False, na=False)) & 
                  (df["Premiere"].between(year_range[0], year_range[1]))]
    return filtered.sort_values(by="Watchtime in Million", ascending=False).head(5)

print(recommend_by_genre("Action", (2000, 2023)))
