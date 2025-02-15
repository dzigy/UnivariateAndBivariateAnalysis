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


############### CONTINUOUS VARIABLES ########################
# create new figure for plotting with 14x6 size
plt.figure(figsize=(14, 6))

# Plot for Age
plt.subplot(1, 2, 1)
sns.histplot(df['age'], kde=True, color='skyblue')
plt.title('Distribution of Age')
print('Convert from object to numeric 3:')

# Plot for Score
plt.subplot(1, 2, 2)
sns.histplot(df['score'], kde=True, color='lightgreen')
plt.title('Distribution of Score')

plt.tight_layout() #adjust the layout of the plot
plt.show() # function that displays the plot.

############### CATEGORICAL VARIABLES ########################

# Bar plot for Sex distribution
plt.subplot(1, 2, 1)
sns.countplot(x='sex', data=df)
plt.title('Distribution of Sex')
plt.xlabel('Sex')
plt.ylabel('Count')

# Bar plot for Smoker distribution
plt.subplot(1, 2, 2)
sns.countplot(x='smoker', data=df)
plt.title('Distribution of Smoker Status')
plt.xlabel('Smoker')
plt.ylabel('Count')

plt.tight_layout() #adjust the layout of the plot
plt.show() # function that displays the plot.