# Pandas Notes

## Introduction to Pandas

Pandas is a powerful library for data manipulation and analysis in Python.

## Data Structures in Pandas

### Series

- One-dimensional array-like object.
- Holds data of similar types.
- Indexing allows for fast lookups.

Example:
```python
import pandas as pd

data = pd.Series([0.25, 0.5, 0.75, 1.0])
print(data)
```

### DataFrame

- Two-dimensional labeled data structure.
- Columns can have different data types (similar to a spreadsheet or SQL table).
- Offers powerful indexing and reshaping capabilities.

Example:
```python
data = {'name': ['Alice', 'Bob', 'Charlie', 'David'],
        'age': [25, 30, 35, 40],
        'city': ['New York', 'Los Angeles', 'Chicago', 'Houston']}

df = pd.DataFrame(data)
print(df)
```

## Data Manipulation with Pandas

### Reading and Writing Data

#### Reading Data

```python
# Reading from CSV
df = pd.read_csv('data.csv')

# Reading from Excel
df = pd.read_excel('data.xlsx')
```

#### Writing Data

```python
# Writing to CSV
df.to_csv('data.csv', index=False)

# Writing to Excel
df.to_excel('data.xlsx', sheet_name='Sheet1', index=False)
```

### Data Inspection

- `df.head()`: Shows the first few rows.
- `df.tail()`: Shows the last few rows.
- `df.info()`: Provides a concise summary of the DataFrame.

Example:
```python
print(df.head())
print(df.info())
```

### Selection and Indexing

#### Selecting Columns

```python
# Selecting a single column
print(df['column_name'])

# Selecting multiple columns
print(df[['column_name1', 'column_name2']])
```

#### Selecting Rows

```python
# Selecting rows by index
print(df.loc[index_label])

# Selecting rows by position
print(df.iloc[row_number])
```

### Data Manipulation

#### Adding and Dropping Columns

```python
# Adding a new column
df['new_column'] = values

# Dropping a column
df.drop('column_to_drop', axis=1, inplace=True)
```

#### Filtering Data

```python
# Filtering based on a condition
filtered_data = df[df['column'] > value]
```

#### Sorting Data

```python
# Sorting by a single column
sorted_df = df.sort_values(by='column_name')

# Sorting by multiple columns
sorted_df = df.sort_values(by=['column1', 'column2'], ascending=[True, False])
```

#### Grouping and Aggregating Data

```python
# Grouping by a column
grouped = df.groupby('column_name')

# Applying an aggregate function
agg_data = grouped.agg({'column1': 'sum', 'column2': 'mean'})
```
