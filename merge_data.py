import pandas as pd
import os

flixpatrol_df = pd.read_csv("data/flixpatrol_cleaned.csv")

folder_path = "data/NetflixDataSet/"
all_files = [f for f in os.listdir(folder_path) if f.endswith(".csv")]

df_list = [pd.read_csv(os.path.join(folder_path, file)) for file in all_files]
netflix_data = pd.concat(df_list, ignore_index=True)

if "title" in netflix_data.columns and "imdb_rating" in netflix_data.columns:
    imdb_data = netflix_data[["title", "imdb_rating"]].drop_duplicates()

    flixpatrol_df["Title"] = flixpatrol_df["Title"].str.strip().str.lower()
    imdb_data["title"] = imdb_data["title"].str.strip().str.lower()

    merged_df = flixpatrol_df.merge(imdb_data, left_on="Title", right_on="title", how="left")

    missing_titles = merged_df[merged_df["imdb_rating"].isna()]["Title"].unique()
    print(f"⚠️ Titles without IMDB ratings: {len(missing_titles)}")
    print(missing_titles[:10])  # Print only 10 missing titles

    merged_df.to_csv("data/flixpatrol_with_imdb.csv", index=False)
    print("✅ Merged dataset saved as 'flixpatrol_with_imdb.csv'")
else:
    print("❌ 'title' or 'imdb_rating' column not found in NetflixDataSet!")
