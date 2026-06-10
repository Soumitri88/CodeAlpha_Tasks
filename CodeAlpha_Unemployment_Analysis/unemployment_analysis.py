#Before running the code make sure to go to the terminal and run the CodeAlpha_Unemployment_Analysis directory.
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Unemployment_Rate_upto_11_2020.csv")

df.columns = df.columns.str.strip()

print(df.head())

plt.figure(figsize=(12,6))
plt.bar(df["Region"], df["Estimated Unemployment Rate (%)"])
plt.xticks(rotation=90)
plt.title("Unemployment Rate by State")
plt.tight_layout()
plt.savefig("unemployment_rate_by_state.png")
plt.show()
#Pie chart for the top 5 regions with the highest average unemployment rate
region_avg = df.groupby("Region")["Estimated Unemployment Rate (%)"].mean()

plt.figure(figsize=(8,8))
plt.pie(
    region_avg.head(5),
    labels=region_avg.head(5).index,
    autopct="%1.1f%%"
)
plt.title("Top 5 Regions by Average Unemployment Rate")
plt.savefig("unemployment_pie_chart.png")
plt.show()