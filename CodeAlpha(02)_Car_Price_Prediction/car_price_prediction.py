import pandas as pd #Loads and manipulates data
import matplotlib.pyplot as plt #draws charts
from sklearn.model_selection import train_test_split  #splits data into training and testing portions
from sklearn.linear_model import LinearRegression #The machine learning algorithm used here
from sklearn.metrics import r2_score #a formula to measure how accurate the model is 

df = pd.read_csv("car data.csv")

# Convert text columns into numbers as ml only understands numbers
df = pd.get_dummies(df, drop_first=True)

# X = all columns except Selling_Price (inputs to the model)
# y = Selling_Price only (what we want to predict)
X = df.drop("Selling_Price", axis=1)
y = df["Selling_Price"]

# Split data: 80% for training, 20% for testing
# random_state=42 ensures the same split every run (reproducibility)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = LinearRegression()
model.fit(X_train, y_train) # .fit() is where learning happens — model finds the best relationship between features and price

# Predict  prices and evaluate unseen datasets 
y_pred = model.predict(X_test)

#Evaluate accuracy of predicted values with the actual values  
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