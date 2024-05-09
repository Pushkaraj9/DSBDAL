import seaborn as sns
import matplotlib.pyplot as plt


titanic_df = sns.load_dataset('titanic')


print("First few rows of the Titanic dataset:")
print(titanic_df.head())
print()


sns.set(style="whitegrid")


plt.figure(figsize=(8, 6))
sns.countplot(x='survived', hue='sex', data=titanic_df)
plt.title('Survival Count by Sex')
plt.xlabel('Survived')
plt.ylabel('Count')
plt.show()


plt.figure(figsize=(8, 6))
sns.countplot(x='survived', hue='class', data=titanic_df)
plt.title('Survival Count by Passenger Class')
plt.xlabel('Survived')
plt.ylabel('Count')
plt.show()


plt.figure(figsize=(8, 6))
sns.countplot(x='survived', hue='embarked', data=titanic_df)
plt.title('Survival Count by Embarkation Port')
plt.xlabel('Survived')
plt.ylabel('Count')
plt.show()

plt.figure(figsize=(10, 6))
sns.histplot(data=titanic_df, x='fare', bins=30, kde=True)
plt.title("Distribution of Ticket Prices")
plt.xlabel('Fare')
plt.ylabel('Frequency')
plt.show()

sns.pairplot(titanic_df, hue='survived', vars=['age', 'fare', 'pclass'], height=3)
plt.suptitle('Pairplot of Numerical Variables by Survival')
plt.show()