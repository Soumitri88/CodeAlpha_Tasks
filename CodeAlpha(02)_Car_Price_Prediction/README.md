# 🚗 Car Price Prediction Using Machine Learning

## 📖 Introduction
This project uses Machine Learning to predict the price of a car based on various features such as brand, horsepower, mileage, fuel type, and year of manufacture. The goal is to build a model that can estimate car prices accurately using the dataset provided.

This project helped me understand the complete machine learning workflow, including data preprocessing, feature engineering, model training, evaluation, and visualization.

---

## 🎯 Project Objectives
- Collect and analyze car-related data.
- Clean and preprocess the dataset.
- Convert categorical data into numerical form.
- Train a regression model to predict car prices.
- Evaluate the model's performance.
- Visualize the relationship between actual and predicted prices.

---

## 🛠️ Technologies Used
- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn

---

## 📂 Dataset
The dataset contains information about different cars and their selling prices.

### Features Used
- Brand
- Model
- Year
- Horsepower
- Mileage
- Fuel Type
- Transmission
- Engine Size

### Target Variable
- Car Price

---

## 🔄 Project Workflow

### 1. Data Collection
- Downloaded the car price dataset.
- Loaded the dataset using Pandas.

### 2. Data Preprocessing
- Handled missing values.
- Removed unnecessary columns.
- Encoded categorical features.

### 3. Feature Engineering
- Selected important features affecting car prices.
- Prepared data for model training.

### 4. Model Training
- Split the dataset into training and testing sets.
- Trained a regression model using Scikit-learn.

### 5. Model Evaluation
The model was evaluated using:
- Mean Absolute Error (MAE)
- R² Score

### 6. Visualization
Used Matplotlib to compare:
- Actual Prices
- Predicted Prices

---

## 📊 Results
The machine learning model was able to predict car prices based on the selected features. The evaluation metrics showed the effectiveness of the model in estimating vehicle prices.

---

## 🚀 How to Run the Project

### Step 1: Install Required Libraries
```in terminal:
pip install pandas numpy matplotlib scikit-learn
```

### Step 2: Download the Dataset
Download the dataset and place it in the project folder.

### Step 3: Run the Python Script
```In terminal:
python car_price_prediction.py
```

---

## 📈 Future Improvements
- Use larger datasets for better accuracy.
- Try advanced algorithms like XGBoost.
- Perform hyperparameter tuning.
- Deploy the model as a web application.

---

## 💡 Learning Outcomes
Through this project, I learned:
- Data preprocessing techniques.
- Feature engineering concepts.
- Regression modeling with Scikit-learn.
- Model evaluation methods.
- Data visualization using Matplotlib.
- Real-world applications of machine learning in price prediction.

## Why Linear Regression
- The target variable (Selling Price) is continuous, not categorical, so regression made more sense than classification. Linear Regression was a good baseline to start with before trying more complex models.

---

## 👨‍💻 Author
Soumitri

This project was completed as part of a Data Science Internship Program by CodeAlpha.