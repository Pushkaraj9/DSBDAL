# Step 1: Import necessary libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Step 2: Load the dataset
boston_data = pd.read_csv('D:\Pushkaraj\kaggle\BostonHousing.csv')

# Step 3: Explore the dataset
print(boston_data.head())  # View the first few rows of the dataset
print(boston_data.info())  # Get information about the dataset

# Step 4: Preprocess the data
# In this step, you may need to handle missing values, encode categorical variables (if any), etc.
# For the Boston Housing dataset, preprocessing might not be necessary as it's a clean dataset.

# Step 5: Split the data into training and testing sets
X = boston_data.drop('medv', axis=1)  # Features
y = boston_data['medv']  # Target variable

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 6: Train the linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Step 7: Evaluate the model
y_pred = model.predict(X_test)

# Calculate Mean Squared Error
mse = mean_squared_error(y_test, y_pred)
print('Mean Squared Error:', mse)

# Calculate R-squared
r2 = r2_score(y_test, y_pred)
print('R-squared:', r2)
