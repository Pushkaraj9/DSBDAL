#pokemon dataset and use of various attributes to perform on the given dataset
#2 line leave new attribute


import pandas as pd


print(pd.__version__)


df = pd.read_csv("D:\Pushkaraj\kaggle\pokemon.csv")
print (df)


print (df.info())


print(df.describe())  


null_values = df.isnull()

print(df)
print("\nMissing Values:")
print(null_values)


data_types = df.dtypes

print("Data Types of Columns:")
print(data_types)


dimensions = df.shape

print("Number of Rows and Columns:")
print(dimensions)	

