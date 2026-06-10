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