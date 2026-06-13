import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

#Load Data from the source provided.
df = pd.read_csv("Advertising.csv")

#Data Cleaning
# Remove unnecessary column
df = df.drop("Unnamed: 0", axis=1)

# Features and target
X = df[["TV", "Radio", "Newspaper"]]
y = df["Sales"]

# TRAIN-TEST SPLIT
# Split data: 80% for training, 20% for testing
# random_state=42 ensures reproducibility of results
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

#Prediction
y_pred = model.predict(X_test)

score = r2_score(y_test, y_pred)
print("R2 Score:", score)
print("Model trained successfully!")

#Scatter plot created 
plt.scatter(y_test, y_pred)

plt.xlabel("Actual Sales")
plt.ylabel("Predicted Sales")
plt.title("Actual vs Predicted Sales")

plt.savefig("sales_prediction.png")

plt.show()


plt.scatter(df["TV"], df["Sales"])
plt.xlabel("TV Advertising Budget")
plt.ylabel("Sales")
plt.title("TV Advertising vs Sales")
plt.savefig("sales_prediction(TV).png")
plt.show()
