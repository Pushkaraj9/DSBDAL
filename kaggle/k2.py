import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Define the columns of the dataset
columns = ['Student_ID', 'Name', 'Grade_Level', 'Math_Score', 'Science_Score', 'English_Score']

# Generate sample data
data = {
    'Student_ID': [101, 102, 103, 104, 105],
    'Name': ['Jatin', 'Aditya', 'Shyam', 'Ram', 'Sundar'],
    'Grade_Level': [10, 11, np.nan, 10, 12],
    'Math_Score': [85, 90, 75, np.nan, 88],
    'Science_Score': [92, 88, 80, 75, 90],
    'English_Score': [78, np.nan, 85, 88, 82]
}

# Create DataFrame
df = pd.DataFrame(data)

# Print the dataset before handling missing values and inconsistencies
print("Dataset before handling missing values and inconsistencies:")
print(df)
print()

# Scan for missing values and inconsistencies
missing_values = df.isnull().sum()
print("Missing values:")
print(missing_values)
print()

# Handling missing values
df['Grade_Level'].fillna(df['Grade_Level'].median(), inplace=True)
df['Math_Score'].fillna(df['Math_Score'].mean(), inplace=True)
df['Science_Score'].fillna(df['Science_Score'].mean(), inplace=True)
df['English_Score'].fillna(df['English_Score'].mean(), inplace=True)

# Print the dataset after handling missing values
print("Dataset after handling missing values:")
print(df)

# Step 3: Scan for outliers in numeric variables and handle them
# Visualize outliers using boxplots
plt.figure(figsize=(10, 6))
sns.boxplot(data=df[['Grade', 'Math_Score', 'Science_Score', 'English_Score']])
plt.title('Boxplot of Numeric Variables')
plt.xlabel('Variable')
plt.ylabel('Value')
plt.xticks(rotation=45)
plt.show()

