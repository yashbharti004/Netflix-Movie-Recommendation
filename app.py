import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/flixpatrol_fully_cleaned.csv")

df["Premiere"] = pd.to_numeric(df["Premiere"], errors='coerce')

df["Watchtime in Million"] = df["Watchtime in Million"].str.replace("M", "").astype(float)  

st.title("Netflix Movie Recommendation System")

movie_type = st.selectbox("Select Type:", ["Movie", "TV Show"])
genre = st.selectbox("Select Genre:", df["Genre"].unique())
year_range = st.slider("Select Year Range:", 2000, 2023, (2010, 2020))
view_option = st.radio("Select Viewing Preference:", ["Most Viewed", "Least Viewed"])


filtered_data = df[(df["Type"] == movie_type) & (df["Genre"].str.contains(genre, na=False)) & (df["Premiere"].between(year_range[0], year_range[1], inclusive="both"))]

if view_option == "Most Viewed":
    filtered_data = filtered_data.sort_values(by="Watchtime in Million", ascending=False)
else:
    filtered_data = filtered_data.sort_values(by="Watchtime in Million", ascending=True)

st.subheader("Filtered Data Table (Sorted by Watchtime)")
st.write(filtered_data[["Title", "Genre", "Premiere", "Watchtime in Million"]].reset_index(drop=True).head(10))

