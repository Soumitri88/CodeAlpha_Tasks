#Before running the code make sure to go to the terminal and run the CodeAlpha_Unemployment_Analysis directory.
import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file into a DataFrame (like a table in Python)
df = pd.read_csv("Unemployment_Rate_upto_11_2020.csv")

# Remove leading/trailing spaces from column names to avoid KeyErrors
df.columns = df.columns.str.strip()

# Preview the first 5 rows to verify data loaded correctly
print(df.head())

#Bar chart for the unemployment rate by state.
plt.figure(figsize=(12,6))
plt.bar(df["Region"], df["Estimated Unemployment Rate (%)"])
plt.xticks(rotation=90)
plt.title("Unemployment Rate by State")
plt.tight_layout()  # Prevents labels from getting cut off
plt.savefig("unemployment_rate_by_state.png")
plt.show()

#Pie chart for the top 5 regions with the highest average unemployment rate
region_avg = df.groupby("Region")["Estimated Unemployment Rate (%)"].mean()
plt.figure(figsize=(8,8))

# Plot only the top 5 regions; autopct shows percentage on each slice
plt.pie(
    region_avg.head(5),
    labels=region_avg.head(5).index,
    autopct="%1.1f%%"
)
plt.title("Top 5 Regions by Average Unemployment Rate")
plt.savefig("unemployment_pie_chart.png")
plt.show()

#Line chart for the unemployment analysis over time.
df["Date"] = pd.to_datetime(df["Date"])

# Average unemployment rate across all regions for each date (national trend)
monthly = df.groupby("Date")["Estimated Unemployment Rate (%)"].mean()
plt.figure(figsize=(12,6))
plt.plot(monthly.index, monthly.values)
plt.title("Unemployment Trend Over Time")
plt.xlabel("Date")
plt.ylabel("Unemployment Rate (%)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("unemployment_trend.png")
plt.show()