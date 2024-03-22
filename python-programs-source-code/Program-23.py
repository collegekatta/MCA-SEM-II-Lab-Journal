import pandas as pd
import matplotlib.pyplot as plt

# 1. Read the titanic.csv file
titanic_df = pd.read_csv('titanic-program-23.csv')

# 2. Drop unwanted column
titanic_df.drop(columns=['Cabin'], inplace=True)

# 3. Encode Male as 1 and Female as 2
titanic_df['Sex'] = titanic_df['Sex'].map({'male': 1, 'female': 2})

# 4. Find out the ratio of Male and Female
male_count = (titanic_df['Sex'] == 1).sum()
female_count = (titanic_df['Sex'] == 2).sum()
gender_ratio = male_count / female_count
print("Male to Female ratio:", gender_ratio)

# 5. Treat missing values
titanic_df.fillna(method='ffill', inplace=True)  # Forward fill missing values

# 6. Treat outliers if any (For example, removing outliers from 'Age' column)
Q1 = titanic_df['Age'].quantile(0.25)
Q3 = titanic_df['Age'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
titanic_df = titanic_df[(titanic_df['Age'] >= lower_bound) & (titanic_df['Age'] <= upper_bound)]

# 7. Rename columns
titanic_df.rename(columns={'Sex': 'Gender'}, inplace=True)

# 8. Plot a graph of Gender
gender_counts = titanic_df['Gender'].value_counts()
gender_counts.plot(kind='bar', color=['blue', 'pink'])
plt.title('Gender Distribution')
plt.xlabel('Gender (1: Male, 2: Female)')
plt.ylabel('Count')
plt.xticks(rotation=0)
plt.show()
