import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data/flixpatrol_fully_cleaned.csv")

df["Premiere"] = pd.to_numeric(df["Premiere"], errors='coerce')

df["Watchtime in Million"] = df["Watchtime in Million"].str.replace("M", "").astype(float)  # Convert watchtime to numeric

st.title("Netflix Movie Recommendation System")

movie_type = st.selectbox("Select Type:", ["Movie", "TV Show"])
genre = st.selectbox("Select Genre:", df["Genre"].unique())
year_range = st.slider("Select Year Range:", 2000, 2023, (2010, 2020))
view_option = st.radio("Select Viewing Preference:", ["Most Viewed", "Least Viewed"])
analysis_option = st.selectbox("Select Analysis Type:", [
    "Netflix Insights",
    "Movie Purchase Recommendation",
    "Customer Complaints & Suggestions"
])

filtered_data = df[(df["Type"] == movie_type) & (df["Genre"].str.contains(genre, na=False)) & (df["Premiere"].between(year_range[0], year_range[1], inclusive="both"))]

if view_option == "Most Viewed":
    filtered_data = filtered_data.sort_values(by="Watchtime in Million", ascending=False)
else:
    filtered_data = filtered_data.sort_values(by="Watchtime in Million", ascending=True)

st.subheader("Filtered Data Table (Sorted by Watchtime)")
st.write(filtered_data[["Title", "Genre", "Premiere", "Watchtime in Million"]].reset_index(drop=True).head(10))

if analysis_option == "Netflix Insights":
    st.subheader("Insights for Netflix")
    netflix_problems = [
        "Find the most popular genre in different regions.",
        "Analyze trends in movie watchtime over the years.",
        "Identify underperforming movies and genres.",
        "Recommend suitable movie categories for different seasons.",
        "Analyze audience preference for new vs. old movies."
    ]
    st.write("### 5 Key Insights Netflix Can Use:")
    st.write("\n".join([f"- {problem}" for problem in netflix_problems]))

elif analysis_option == "Movie Purchase Recommendation":
    st.subheader("Movie Purchase Recommendation for Netflix")
    if not filtered_data.empty:
        top_movie = filtered_data.iloc[0]
        st.write(f"**Recommendation:** Purchase movies similar to '{top_movie['Title']}' as it has high watchtime in its category.")
    else:
        st.write("No suitable recommendation found based on the current filters.")

elif analysis_option == "Customer Complaints & Suggestions":
    st.subheader("Customer Feedback Based on Data")
    cust_feedback = [
        "More diversity in content with different genres.",
        "Adding more classic movies based on audience interest.",
        "Increasing availability of highly watched but discontinued shows.",
        "Better regional content selection based on viewing trends.",
        "More frequent updates on trending movie lists."
    ]
    st.write("### Customer Complaints & Suggestions:")
    st.write("\n".join([f"- {feedback}" for feedback in cust_feedback]))

if not filtered_data.empty:
    st.subheader("Watchtime Distribution by Movie (Bar Plot)")

    top_movies = filtered_data[["Title", "Watchtime in Million"]].head(10)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(top_movies["Title"], top_movies["Watchtime in Million"], color='blue', alpha=0.7, edgecolor='black')

    ax.set_xticklabels(top_movies["Title"], rotation=45, ha="right", fontsize=10)

    ax.set_xlabel("Movie Title")
    ax.set_ylabel("Watchtime in Million (Worldwide)")
    ax.set_title("Top 10 Movies by Watchtime")

    st.pyplot(fig)

    st.subheader("Alternative Visualization: Seaborn Style Histogram")

    fig2, ax2 = plt.subplots(figsize=(10, 5))
    sns.barplot(x=top_movies["Title"], y=top_movies["Watchtime in Million"], palette="coolwarm", ax=ax2)

    ax2.set_xticklabels(top_movies["Title"], rotation=45, ha="right", fontsize=10)

    ax2.set_xlabel("Movie Title")
    ax2.set_ylabel("Watchtime in Million (Worldwide)")
    ax2.set_title("Seaborn Styled Watchtime Histogram")

    st.pyplot(fig2)

else:
    st.write("No data available to generate a histogram based on the selected filters.")
