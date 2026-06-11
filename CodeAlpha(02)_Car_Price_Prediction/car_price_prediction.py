import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

df = pd.read_csv("car data.csv")

# Convert text columns into numbers
df = pd.get_dummies(df, drop_first=True)

# Features (X) and Target (y)
X = df.drop("Selling_Price", axis=1)
y = df["Selling_Price"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict and evaluate 
y_pred = model.predict(X_test)

score = r2_score(y_test, y_pred)

print("R2 Score:", score)

#Create a graph to visualize the relationship between the features and the target variable.
plt.scatter(y_test, y_pred)
plt.xlabel("Actual Price")
plt.ylabel("Predicted Price")
plt.title("Actual vs Predicted Car Prices")
plt.savefig("car_price_prediction.png")
plt.show()

print("Model trained successfully!")