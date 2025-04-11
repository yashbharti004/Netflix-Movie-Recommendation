import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data/flixpatrol_fully_cleaned.csv")

top_watched = df.sort_values(by="Watchtime in Million", ascending=False).head(10)

plt.figure(figsize=(12, 6))
sns.barplot(x="Watchtime in Million", y="Title", data=top_watched, palette="coolwarm")
plt.xlabel("Watchtime (Million Hours)")
plt.ylabel("Title")
plt.title("Top 10 Most Watched Shows/Movies on Netflix")
plt.show()
