import pandas as pd
from scipy.stats import mannwhitneyu

### Nonparametric Statistical Test - Mann-Whitney U test
originalData = pd.read_excel('Health Insurance Dataset.xlsx')
df = pd.DataFrame(originalData)
# remove whitespace from the column names of a DataFrame
df.columns = df.columns.str.strip()
print('print first 10 records:')
print(df.head(10))
print('Print data types:')
print(df.dtypes)

#charges column is object and I need to convert to numeric
df["charges"] = pd.to_numeric(df["charges"], errors="coerce")

# Drop NaN values
df = df.dropna(subset=["charges"])

# Separate smokers and non-smokers
smokers = df[df["smoker"] == "yes"]["charges"]
nonSmokers = df[df["smoker"] == "no"]["charges"]

# Perform Mann-Whitney U test
stat, p_value = mannwhitneyu(smokers, nonSmokers)

# Output the result
print(f'Mann-Whitney U statistic: {stat}')
print(f'P-value: {p_value}')