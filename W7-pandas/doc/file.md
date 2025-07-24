# Introduction to pandas

---

## Table of Contents

1. [What Is pandas?](#what-is-pandas)  
2. [What is pandas used for?](#what-is-pandas-used-for) 
2. [Installing pandas](#installing-pandas)
3. [Core Data Structures](#core-data-structures)
   - [Series](#series)
   - [DataFrame](#dataframe)
4. [Loading Data](#loading-data)
   - [Reading CSV files](#reading-csv-files)
   - [Inspecting the data](#inspecting-the-data)
5. [Indexing & Selection](#indexing--selection)
   - [Label-based (](#label-based-loc)[`.loc`](#label-based-loc)[)](#label-based-loc)
   - [Position-based (](#position-based-iloc)[`.iloc`](#position-based-iloc)[)](#position-based-iloc)
6. [Basic Operations](#basic-operations)
   - [Filtering rows](#filtering-rows)
   - [Adding & dropping columns](#adding--dropping-columns)
   - [Sorting](#sorting)
7. [Handling Missing Data](#handling-missing-data)
8. [GroupBy & Aggregation](#groupby--aggregation)
9. [Merging & Joining](#merging--joining)
10. [Quick Visualization](#quick-visualization)

---

## What Is pandas?

**pandas** is a data manipulation package in Python for tabular data. That is, data in the form of rows and columns, also known as DataFrames. Intuitively, you can think of a DataFrame as an Excel sheet. 

---

## What is pandas used for?

pandas is used throughout the data analysis workflow. With pandas, you can:

- Import datasets from databases, spreadsheets, comma-separated values (CSV) files, and more.
- Clean datasets, for example, by dealing with missing values.
- Tidy datasets by reshaping their structure into a suitable format for analysis.
- Aggregate data by calculating summary statistics such as the mean of columns, correlation between them, and more.
- Visualize datasets and uncover insights

---

## Installing pandas

Install via pip:

```bash
pip install pandas
```



---

## Core Data Structures

### Series

A **Series** is a one‑dimensional labeled array (like a column in a table).

```python
import pandas as pd

# Create a Series from a list
s = pd.Series([10, 20, 30, 40], index=['a', 'b', 'c', 'd'])
print(s)
```

**Output:**

```
a    10
b    20
c    30
d    40
dtype: int64
```

### DataFrame

A **DataFrame** is a two‑dimensional labeled data structure (like a spreadsheet).

```python
# Create a DataFrame from a dictionary
data = {
    'Name':    ['Alice', 'Bob', 'Charlie'],
    'Age':     [25, 30, 35],
    'Country': ['USA', 'Canada', 'UK']
}
df = pd.DataFrame(data)
print(df)
```

**Output:**

```
      Name  Age Country
0    Alice   25     USA
1      Bob   30  Canada
2  Charlie   35      UK
```

---

## Loading Data

### Reading CSV files
ref : https://www.geeksforgeeks.org/machine-learning/dataset-for-linear-regression/
```python
# Reading csv file
df_file = pd.read_csv('./dataset/StudentsPerformance[1].csv')
df = pd.read_csv('https://media.geeksforgeeks.org/wp-content/uploads/20240522153243/StudentsPerformance%5B1%5D.csv')
```

### Inspecting the data

```python
df.head() # Returns the first 5 rows 
df.head(20) # Returns the first 20 rows 
df.tail() # Returns the last 5 rows 
df.info() # Shows information on each of the columns, such as the data type and number of missing values.
df.shape # Returns the number of rows and columns of the DataFrame.
df.describe() # Calculates a few summary statistics for each column.
df.dtypes # Returns a Series with the data type of each column.
df.values # Return a Numpy representation of the DataFrame.
df.value_counts() # Return a Series containing the frequency of each distinct row in the Dataframe.

```

---

## Indexing & Selection

### Label‑based (`.loc`)

```python
# Select row with index label 2
row2 = df.loc[2]

# Select rows 0–3 and columns 'Name' & 'Age'
subset = df.loc[0:3, ['Name', 'Age']]
```

### Position‑based (`.iloc`)

```python
# Select the first row
first_row = df.iloc[0]

# Select first 3 rows and first 2 columns
subset = df.iloc[0:3, 0:2]
```

---

## Basic Operations

### Filtering rows

```python
# All rows where population > 1000
population_more1000 = df[df['population'] > 1000]

```

### Adding & dropping columns

```python
# Add a new column
df['rooms_per_household'] = df['total_rooms'] / df['households']

# Drop a column
df = df.drop(columns=['rooms_per_household'])
```

### Sorting

```python
# Sort by population descending (ascending=False)
df.sort_values(by='population', ascending=False)
```

---

## Handling Missing Data

```python
# Detect missing values
df.isnull().sum()

# Drop rows with any missing values
df_clean = df.dropna()

# Fill missing values with a default
df_filled = df.fillna({'Age': df['Age'].mean()})
```



