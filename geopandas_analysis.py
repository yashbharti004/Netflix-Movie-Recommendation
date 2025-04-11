import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
import os

folder_path = "data/NetflixDataSet/"
all_files = [f for f in os.listdir(folder_path) if f.endswith(".csv")]

df_list = [pd.read_csv(os.path.join(folder_path, file)) for file in all_files]
df = pd.concat(df_list, ignore_index=True)

if "ori_country" not in df.columns:
    print("❌ Error: 'ori_country' column not found in dataset!")
    print("Available Columns:", df.columns)
    exit()

world = gpd.read_file("data/natural/ne_110m_admin_0_countries.shp")

country_counts = df["ori_country"].value_counts().reset_index()
country_counts.columns = ["Country", "Movie_Count"]

world = world.merge(country_counts, left_on="NAME", right_on="Country", how="left").fillna(0)

fig, ax = plt.subplots(figsize=(12, 6))
world.plot(column="Movie_Count", cmap="coolwarm", linewidth=0.8, edgecolor="black", legend=True, ax=ax)

plt.title("Netflix Content Distribution by Country")
plt.show()
