---
title: "Pandas"
---

Pandas

Introduction: Open-source Python library for data manipulation, cleaning, and analysis. Built on NumPy.

Core Data Structures:
1. Series (1D): pd.Series(data, index=['A','B','C','D'])
2. DataFrame (2D): pd.DataFrame({'Name':..., 'Age':..., 'City':...})

Data Ingestion:
- CSV: pd.read_csv('file.csv')
- Excel: pd.read_excel('file.xlsx')
- JSON: pd.read_json('file.json')
- SQL: pd.read_sql(query, connection)

Data Exploration:
- .head() / .tail() — first/last 5 rows
- .info() — data types and non-null values
- .describe() — statistical summary

Data Cleaning:
- df.fillna(0) — replace NaN with 0
- df.dropna() — remove rows with NaN
- df.drop_duplicates()
- df.rename(columns={'old': 'new'}, inplace=True)
- df['Age'] = df['Age'].astype(int)

Data Transformation:
- apply: df['Salary'] = df['Salary'].apply(lambda x: x * 1.1)
- GroupBy: df.groupby('City')['Salary'].mean()
- Sort: df.sort_values('Age', ascending=False)

Filtering and Selection:
- .loc[] — Label-based selection
- .iloc[] — Position-based selection
- filtered_df = df[df['Age'] > 30]
- df.loc[0:2, ['Name', 'City']]

Merging and Joining:
- pd.merge(df1, df2, on='common_column', how='inner')
- pd.concat([df1, df2], axis=0)  # Vertical stack
- pd.concat([df1, df2], axis=1)  # Horizontal merge

Time Series:
- pd.to_datetime(df['Date'])
- df.resample('M').sum()  # Resample by month

Writing Data:
- df.to_csv('output.csv', index=False)
- df.to_excel('output.xlsx', index=False)
- df.to_sql('table_name', connection, if_exists='replace')

Performance Tips:
- Avoid .iterrows(); prefer vectorized operations
- Use .query() and .eval() for faster computations
- Convert data types to reduce memory: df['col'].astype('int32')

Real-World Example:
```python
df = pd.read_csv('sales_data.csv')
df.dropna(inplace=True)
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Total Sales'] = df['Quantity'] * df['Price']
sales_summary = df.groupby('Region')['Total Sales'].sum()
sales_summary.to_csv('sales_summary.csv')
```
