import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the Iris dataset
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
column_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']
iris_df = pd.read_csv(url, names=column_names)

# Step 1: List down the features and their types
print("Features and their types:")
print(iris_df.dtypes)
print()

# Step 2: Create histograms for each feature
iris_df.hist(figsize=(10, 8))
plt.suptitle('Histograms of Iris Dataset Features')
plt.show()

# Step 3: Create boxplots for each feature
plt.figure(figsize=(10, 8))
iris_df.boxplot()
plt.title('Boxplots of Iris Dataset Features')
plt.show()

# Step 4: Identify outliers
# We can visually inspect the boxplots to identify outliers
