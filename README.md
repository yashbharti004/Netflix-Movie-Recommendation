# Netflix Data Analysis and Recommendation System
## Overview
This project leverages data analytics, geospatial visualization, and interactive dashboards to provide meaningful insights into Netflix content. It also features a recommendation system that suggests top-performing content based on user preferences.

## Key Features
1.**Data Cleaning & Integration:** Merges multiple Netflix datasets, cleans inconsistencies, and adds IMDb ratings.

2.**Recommendation Engine:** Recommends top movies or shows based on genre, type, year range, and watchtime.

3.**Geospatial Visualization:** Uses GeoPandas to show Netflix content distribution across countries.

4.**Interactive Dashboard:** Built with Streamlit to visualize trends, user preferences, and content analytics.

5.**Insight Generator:** Provides business insights, purchase recommendations, and user feedback simulations for Netflix decision-makers.

## Methodology
1.**Data Preprocessing (clean.py, merge_data.py):**
-Cleans ranking and watchtime columns.
-Merges IMDb ratings into the FlixPatrol dataset.

2.**Recommendation System (recommend.py, main.py.py, app.py):**
-Filters content by genre, type, and year range.
-Ranks results based on watchtime to suggest high-performing titles.

3.**Visualization & Analysis (analysis.py, geopandas_analysis.py):**
-Bar charts of top 10 watched shows.
-Choropleth map showing Netflix content distribution globally.

4.**Interactive Web App (main.py.py, app.py):**
-Streamlit dashboard allows users to explore data, get recommendations, and analyze feedback/insights.
