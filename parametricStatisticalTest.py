import pandas as pd
from scipy import stats

### Parametric Statistical Test - Independent samples t-test (Welch’s t-test)
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

# Perform an independent samples t-test (Welch’s t-test)
t_stat, p_value = stats.ttest_ind(smokers, nonSmokers, equal_var=False)

# Print results
print(f"T-Statistic: {t_stat}")
print(f"P-Value: {p_value}")