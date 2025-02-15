import pandas as pd
import openpyxl as xl
import seaborn as sns
import matplotlib.pyplot as plt

originalData = pd.read_excel('Health Insurance Dataset.xlsx')
df = pd.DataFrame(originalData)
# remove whitespace from the column names of a DataFrame
df.columns = df.columns.str.strip()
print('print first 10 records:')
print(df.head(10))
print('Print data types:')
print(df.dtypes)

########## BIVARIATE DISTRIBUTION #############################

# 1. Relationship between two continuous variables (Age vs Score)
plt.figure(figsize=(8, 6))
sns.scatterplot(x='age', y='score', data=df, color='blue')
plt.title('Age vs Score')
plt.xlabel('Age')
plt.ylabel('Score')
plt.show()

# Bivariate analysis for categorical variables (Sex & Smoker)
plt.figure(figsize=(12, 5))
sns.countplot(x='sex', hue='smoker', data=df, palette='coolwarm')
plt.title("Smoker  by Sex")
plt.xlabel("Sex")
plt.ylabel("Count")
plt.show()

# Boxplot to analyze Age vs Score by Smoker status
plt.figure(figsize=(12, 5))
sns.boxplot(x='smoker', y='score', data=df, palette='muted')
plt.title("Score by Smoker")
plt.xlabel("Smoker")
plt.ylabel("Score")
plt.show()

# Boxplot for Age by Sex
plt.figure(figsize=(12, 5))
sns.boxplot(x='sex', y='age', data=df, palette='pastel')
plt.title("Age by Sex")
plt.xlabel("Sex")
plt.ylabel("Age")
plt.show()