import seaborn as sns
import matplotlib.pyplot as plt


titanic_df = sns.load_dataset('titanic')


print("First few rows of the Titanic dataset:")
print(titanic_df.head())
print()


sns.set(style="whitegrid")


plt.figure(figsize=(10, 6))
sns.boxplot(data=titanic_df, x='sex', y='age', hue='survived')
plt.title("Age distribution by Gender and Survival")
plt.xlabel('Sex')
plt.ylabel('Age')
plt.legend(title='Survived', loc='upper right')
plt.show()