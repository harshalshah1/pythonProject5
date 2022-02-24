import pandas as pd
import numpy as np
import seaborn as sns  # visualisation
import matplotlib.pyplot as plt  # visualisation
from sklearn.linear_model import LinearRegression

df = pd.read_excel(r'C:\Data\Copy of Comm Primacy 2021_12_new.xlsx', sheet_name='data')

df.head(10)
df.dtypes

df.boxplot(column='lns_eom_m25')
df.boxplot(column='dep_adb_m25')
df.boxplot(column='total_rev_ann')
df.boxplot(column='total_econ_capital_m25')
df.boxplot(column='marginal_raroc')

print(df.isnull().sum())

plt.figure(figsize=(20, 10))
c = df.corr()
sns.heatmap(c, cmap='BrBG', annot=True)

df.shape
# Rows containing duplicate data
duplicate_rows_df = df[df.duplicated()]
print("number of duplicate rows:", duplicate_rows_df.shape)

df_describe = df[
    ['lns_eom_m25', 'dep_adb_m25', 'total_rev_ann', 'rar_ann', 'marginal_net_income_ann', 'total_econ_capital_m25',
     'marginal_raroc']].describe()

df.plot(kind='scatter', x='Trans', y='marginal_raroc')

sns.pairplot(df)
df.plot(kind='scatter', x='total_rev_ann', y='marginal_raroc')

