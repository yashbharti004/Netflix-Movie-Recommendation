import pandas as pd

df = pd.read_csv("data/flixpatrol.csv")

df["Rank"] = df["Rank"].astype(str).str.replace(".", "", regex=True)
df["Rank"] = pd.to_numeric(df["Rank"], errors="coerce").fillna(0).astype(int)

df["Watchtime in Million"] = df["Watchtime in Million"].str.replace("M", "", regex=True)
df["Watchtime in Million"] = pd.to_numeric(df["Watchtime in Million"], errors="coerce").fillna(0)

df.to_csv("data/flixpatrol_cleaned.csv", index=False)
print("✅ Data Cleaning Completed Successfully!")
