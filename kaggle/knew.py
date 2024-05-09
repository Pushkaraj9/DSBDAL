import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


print(pd.__version__)


df = pd.read_csv("D:\Pushkaraj\kaggle\pokemon.csv")
print(df)

"""print(df.info())

print(df.describe())


null_values = df.isnull()

print(df)
print("\nMissing values")
print(null_values)


data_types = df.dtypes

dimensions = df.shape

print("Number of Rows and Columns:")
print(dimensions)"""

print("Dataset before handling missing values")
print(df)
print()


missing_values = df.isnull().sum()
print(missing_values)
print()