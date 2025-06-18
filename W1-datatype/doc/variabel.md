# Python Data Types and Input Values

## Table of Contents
1. [Common Data Types](#common-data-types)
   - [Numeric Types](#1-numeric-types)
   - [Sequence Types](#2-sequence-types)
   - [Mapping Type](#3-mapping-type)
   - [Set Types](#4-set-types)
   - [Boolean Type](#5-boolean-type)
2. [Input Values](#input-values)
   - [Basic Input](#basic-input)
   - [Type-Specific Input](#type-specific-input)
   - [Safe Input Handling](#safe-input-handling)
3. [Type Conversion Table](#type-conversion-table)
4. [Additional Resources](#additional-resources)

---

## Common Data Types in Python

### 1. Numeric Types

#### Integer
Represents whole numbers (positive or negative).

```python
num_int = 42
num_int_cast = int(3.9)  # Converts float to int (truncates decimal)
```

#### Float
Represents decimal numbers.

```python
num_float = 3.14159
num_float_cast = float("7.5")  # Converts string to float
```

#### Complex
Represents complex numbers.

```python
num_complex = 3 + 4j
num_complex_cast = complex(2, 3)  # Creates 2+3j
```

### 2. Sequence Types

#### String
Text data (immutable sequence of characters).
```python
text = "Hello, World!"
text_cast = str(123)  # Converts integer to string
```

#### List
**Mutable** ordered sequence of items.

```python
my_list = [1, 2, 3, "apple", "banana"]
list_cast = list((1, 2, 3))  # Converts tuple to list
list_from_str = list("abc")  # Converts string to list of characters
```

#### Tuple
**Immutable** ordered sequence of items.
```python
my_tuple = (10, 20, "red", "blue")
tuple_cast = tuple([1, 2, 3])  # Converts list to tuple
```

### 3. Mapping Type

#### Dictionary
Key-value pairs (unordered, **mutable**).

```python
my_dict = {"name": "Alice", "age": 30}
dict_cast = dict([(1, 'a'), (2, 'b')])  # Converts list of tuples to dictionary
```

### 4. Set Types

#### Set
Unordered collection of unique items (**mutable**).

```python
my_set = {1, 2, 3}
set_cast = set([1, 2, 2, 3])  # Converts list to set (removes duplicates)
```

### 5. Boolean Type

#### Boolean Type
Represents True or False values.

```python
is_valid = True
bool_cast = bool(1)  # Converts integer to boolean (True)
bool_from_str = bool("False")  # Non-empty string evaluates to True
```

## Input Values

### Basic Input

```python
user_input = input("Enter a value: ")  # Always returns a string datatype
```

### Type-Specific Input


```python
# For numeric input
age = int(input("Enter your age: "))
price = float(input("Enter price: "))

# For boolean input
is_active = input("Active? (y/n): ").lower() == 'y'
```

### Safe Input Handling

**syntax :**
```python
    try:
        # Some Code
    except:
        # Executed if error in the
        # try block
```
**example:**
```python
try:
    number = int(input("Enter a number: "))
except ValueError:
    print("Invalid input! Please enter a valid number.")
```

ref exception : https://www.programiz.com/python-programming/exceptions




