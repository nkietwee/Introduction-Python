# NumPy

##  Objective

NumPy aims to provide an array object that is up to 50x faster than traditional Python lists.
The array object in NumPy is called ndarray, it provides a lot of supporting functions that make working with ndarray very easy. Arrays are very frequently used in data science, where speed and resources are very important.


| Feature                       | Python `list`                  | NumPy `ndarray`                        | Key Difference Summary                     |
| ----------------------------- | ------------------------------ | -------------------------------------- | ------------------------------------------ |
| **Type**                      | Built-in Python data structure | NumPy array object                     | Native vs. library object                  |
| **Data Type Consistency**     | Can store mixed types          | All elements must be of the same type  | NumPy is homogeneous                       |
| **Performance**               | Slower for numerical ops       | Much faster for large-scale operations | NumPy is optimized with C under the hood   |
| **Vectorized Operations**     | <span style="color:red"> Not supported </span>                | <span style="color:green"> Supported </span> (e.g. `a + b`, `a * 2`)    | NumPy enables math on whole arrays         |
| **Broadcasting**              | <span style="color:red"> Not supported </span>               |  <span style="color:green"> Supported </span>                            | Efficient size-flexible operations         |
| **Memory Efficiency**         | Less efficient                 | More compact memory layout             | NumPy uses fixed-size elements             |
| **Multi-dimensional Support** | Manually nested lists          | Native support (`ndarray.ndim`)        | NumPy handles dimensions naturally         |
| **Indexing/Slicing**          | Basic                          | Advanced (fancy indexing, slicing)     | NumPy supports slicing, masks              |
| **Functions & Methods**       | Limited                        | Extensive (`np.mean()`, `np.sum()`)    | NumPy is feature-rich                      |
| **Use Case**                  | General-purpose container      | Numerical and scientific computing     | Lists are for flexibility, NumPy for speed |


## 📚 Lesson Plan

### 1. Install Library and Import library
- **Install**
```shell
pip install numpy
```
- **Import**
```python
import numpy as np
```

### 2. Creating Arrays
![alt text](image-5.png)
![alt text](image-4.png)
![alt text](image-8.png)
```python
# Creates a NumPy array from a Python sequence such as list or tuple.
a = np.array([1, 2, 3]) 
b = np.array((1, 2, 3), dtype=np.int16) # define type of data

# Creates 2D NumPy array from a Python sequence such as list or tuple.
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array(((1, 2, 3), (4, 5, 6)))

e = np.zeros((2, 3))       # Create an Array of Zeros
f = np.ones((3, 5))        # Create an Array of Ones
g = np.arange(0, 10, 2)    # Create a Range of Values
h = np.linspace(0, 1, 5)   # Create Evenly Spaced Values

print(f'1D np.array with list: {a}')
print(f'1D np.array with tuple: {b}')
print(f'2D np.array with list: \n{c}')
print(f'2D np.array with tuple: \n{d}')
print(f'np.array with zeros: \n{e}')
print(f'np.array with ones: \n{f}')
print(f'np.array with range of numbers: {g}')
print(f'np.array with evenly spaced values: {h}')

```
result
```python
1D np.array with list: [1 2 3]
1D np.array with tuple: [1 2 3]
2D np.array with list: 
[[1 2 3]
 [4 5 6]]
2D np.array with tuple: 
[[1 2 3]
 [4 5 6]]
np.array with zeros: 
[[0. 0. 0.]
 [0. 0. 0.]]
np.array with ones: 
[[1. 1. 1. 1. 1.]
 [1. 1. 1. 1. 1.]
 [1. 1. 1. 1. 1.]]
np.array with range of numbers: [0 2 4 6 8]
np.array with evenly spaced values: [0.   0.25 0.5  0.75 1.  ]
```
### 3. Random Numbers

NumPy's `random` module helps you generate random numbers for simulations, model testing, or creating synthetic datasets. Setting a seed ensures reproducibility.

```python
np.random.seed(42)                  # Set seed for reproducibility

a = np.random.rand(3)               # Generate 3 random floats between 0 and 1
b = np.random.randint(0, 10, (2, 3)) # Generate 2x3 matrix of random integers between 0 and 9

print(f"Random floats (a): {a}")
print(f"Random integers (b):\n{b}")
```

Result :
```python
Random floats (a): [0.59241457 0.04645041 0.60754485]
Random integers (b):
[[4 8 6]
 [1 3 8]]
```

## Summary Table

| Syntax                         | Description                      | Example Output                          | Useful For                              |
|-------------------------------|----------------------------------|------------------------------------------|------------------------------------------|
| `np.array([1, 2, 3])`         | Convert list to NumPy array      | `[1, 2, 3]`                              | Creating basic 1D array for calculations |
| `np.array(((1, 2, 3), (4, 5, 6)))` | Convert tuple to 2D NumPy array | `[[1, 2, 3], [4, 5, 6]]`                 | Working with matrices or tables          |
| `np.zeros((2, 3))`            | Create 2x3 array of zeros        | `[[0. 0. 0.], [0. 0. 0.]]`               | Initializing weights, placeholders       |
| `np.ones((3, 3))`             | Create 3x3 array of ones         | `[[1. 1. 1.], [1. 1. 1.], [1. 1. 1.]]`   | Creating filters, identity-like arrays   |
| `np.arange(0, 10, 2)`         | Range from 0 to 8 with step of 2 | `[0, 2, 4, 6, 8]`                        | Generating sequences, loops              |
| `np.linspace(0, 1, 5)`        | 5 values between 0 and 1         | `[0. , 0.25, 0.5, 0.75, 1. ]`            | Creating axes, testing, interpolation    |


### 4. Array Properties
![alt text](image-2.png)
How to get properties of numpy array

```python
# Create a 2D NumPy array (2 rows, 3 columns) from a tuple of tuples
# dtype is inferred as int64 (or int32 depending on your platform)
a = np.array(((1, 2, 3), (4, 5, 6)))
print(a.shape)  # Output: (2, 3) — means 2 rows and 3 columns
print(f'dtype of a: {a.dtype}')  # e.g., int64

# Create a 3x3 array filled with ones
# Default dtype is float64 unless specified
ones_array = np.ones((3, 3))
print(ones_array.size)  # Output: 9 — 3 rows * 3 columns = 9 elements
print(f'dtype of ones_array: {ones_array.dtype}')  # float64

```


**Output:**
```python
(2, 3)
9
```
## Summary Table

| Expression             | Description                                    | Output   | dtype     |
|------------------------|------------------------------------------------|----------|-----------|
| `a.shape`              | Returns the shape (rows, columns) of the array | `(2, 3)` | `int64`*  |
| `a.dtype`              | Returns the data type of the array elements    | `int64`* | `int64`*  |
| `np.ones((3, 3)).size` | Total number of elements in the array          | `9`      | `float64` |


### 5. Indexing and Slicing
![alt text](image-3.png)
![alt text](image-1.png)
how to access specific elements, rows, columns, and slices in a NumPy array.

```python
a = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

# [row, column]

# Basic Indexing
print(f'Access row 0: {a[0]}')
print(f'Access row 1 to end:\n{a[1:]}')
print(f'Access element at (0,2): {a[0, 2]}')

# Slicing
print(f'Access all rows, column 1: {a[:, 1]}')
print(f'Access row 1, first 2 columns: {a[1, :2]}')
print(f'Access full array:\n{a[:, :]}')
print(f'Access top-left 1x2 block: {a[:1, :2]}')
print(f'Access last row: {a[-1]}')

# Boolean Indexing

print(f'Boolean mask (a > 3):\n{a > 3}')
print(f'Elements greater than 3: {a[a > 3]}')
```


**Output:**
```python
Access row 0: [1 2 3]
Access row 1 to end:
[[4 5 6]
 [7 8 9]]
Access element at (0,2): 3
Access all rows, column 1: [2 5 8]
Access row 1, first 2 columns: [4 5]
Access full array:
[[1 2 3]
 [4 5 6]
 [7 8 9]]
Access top-left 1x2 block: [[1 2]]
Access last row: [7 8 9]
Boolean mask (a > 3):
[[False False False]
 [ True  True  True]
 [ True  True  True]]
Elements greater than 3: [4 5 6 7 8 9]
```

### 6. Array Operations
![alt text](image-9.png)
![alt text](image-12.png)
![alt text](image-6.png)
![alt text](image-13.png)
![alt text](image-11.png)
Perform basic mathematical operations on arrays. These are essential for machine learning tasks like vectorized computation, feature scaling, and matrix math.

```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Element-wise operations
print(f"a + b = {a + b}")
print(f"a - b = {a - b}")
print(f"a * b = {a * b}")
print(f"a / b = {a / b}")
print(f"a ** 2 = {a ** 2}")
print(f"a * 2 = {a * 2}")

# Aggregation functions on b
print(f"Sum of b: {np.sum(b)}")
print(f"Mean of b: {np.mean(b)}")
print(f"Max of b: {np.max(b)}")
print(f"Min of b: {np.min(b)}")
print(f"Standard deviation of b: {np.std(b):.4f}")

# Dot product
print(f"Dot product of a and b: {np.dot(a, b)}")

# Concatenation
print(f"Concatenate a and b: {np.concatenate((a, b))}")

# Sorting
unsorted = np.array([3, 1, 5])
print(f"Sorted array: {np.sort(unsorted)}")

# Comparisons
print(f"a > 2: {a > 2}")
print(f"b == 5: {b == 5}")

```
result :
```python
a + b = [5 7 9]
a - b = [-3 -3 -3]
a * b = [ 4 10 18]
a / b = [0.25 0.4  0.5 ]
a ** 2 = [1 4 9]
a * 2 = [2 4 6]
Sum of b: 15
Mean of b: 5.0
Max of b: 6
Min of b: 4
Standard deviation of b: 0.8165
Dot product of a and b: 32
Concatenate a and b: [1 2 3 4 5 6]
Sorted array: [1 3 5]
a > 2: [False False  True]
b == 5: [False  True False]
```

### 7. Reshaping Arrays
![alt text](image.png)
![alt text](image-10.png)
NumPy allows easy reshaping of arrays to change their structure without changing the data.
```python
a = np.arange(6)                     # Create array: [0, 1, 2, 3, 4, 5]
b = a.reshape((2, 3))                # Reshape into 2 rows × 3 columns
c = b.flatten()                      # Return a copy of the array collapsed into one dimension.

print(f"Original a: {a}")
print(f"Reshaped b (2x3):\n{b}")
print(f"Flattened c: {c}")
```

result :
```python
Original a: [0 1 2 3 4 5]
Reshaped b (2x3):
[[0 1 2]
 [3 4 5]]
Flattened c: [0 1 2 3 4 5]
```

### 8. Stacking Arrays
![alt text](image-7.png)
NumPy provides stacking functions to join arrays vertically (`vstack`)
or horizontally (`hstack`). These are helpful when combining data from multiple sources.
```python
a = np.array([[1, 2],
              [3, 4]])

b = np.array([[5, 6]])

# Vertical stack: combine a and b row-wise
v = np.vstack([a, b])

# Horizontal stack: combine a and transpose of b column-wise
h = np.hstack([a, b.T])

print(f"Vertical stack (vstack):\n{v}")
print(f"Horizontal stack (hstack):\n{h}")
```
result :
```python
Vertical stack (vstack):
[[1 2]
 [3 4]
 [5 6]]
Horizontal stack (hstack):
[[1 2 5]
 [3 4 6]]
```

| Function           | Purpose                             | Resulting Shape | Axis Behavior         | Requirements                                |
| ------------------ | ----------------------------------- | --------------- | --------------------- | ------------------------------------------- |
| `np.concatenate()` | Joins arrays along an existing axis | Customizable    | Default `axis=0`      | Shapes must match **except** on concat axis |
| `np.vstack()`      | Stack arrays **vertically**         | (rows added)    | Always axis=0         | 1D arrays become rows                       |
| `np.hstack()`      | Stack arrays **horizontally**       | (columns added) | Depends on array rank | 1D arrays become columns                    |

## Performance and Efficiency Comparison: Python List vs NumPy Array
```python
import numpy as np
import time
import random

# Set size for the large random data
size = 1_000_000

# Generate a Python list of random integers between 0 and 100 using a for loop
python_list = []
for _ in range(size):
    python_list.append(random.randint(0, 100))

# Convert Python list to a NumPy array for comparison
numpy_array = np.array(python_list)

# 1. Adding 1 to each element
# Time the operation for Python list (slow, non-vectorized)
start_time = time.time()
python_list_result = []
for x in python_list:
    python_list_result.append(x + 1)
end_time = time.time()
print(f"List addition time: {end_time - start_time:.5f} seconds")

# Time the operation for NumPy array (fast, vectorized)
start_time = time.time()
numpy_array_result = numpy_array + 1
end_time = time.time()
print(f"NumPy addition time: {end_time - start_time:.5f} seconds")

# 2. Calculating the mean value
# Calculate mean manually for Python list
start_time = time.time()
python_list_mean = sum(python_list) / len(python_list)
end_time = time.time()
print(f"List mean: {python_list_mean:.2f}, time: {end_time - start_time:.5f} seconds")

# Calculate mean using NumPy's built-in method
start_time = time.time()
numpy_array_mean = np.mean(numpy_array)
end_time = time.time()
print(f"NumPy mean: {numpy_array_mean:.2f}, time: {end_time - start_time:.5f} seconds")

# 3. Comparing memory usage
# Display the memory size of the Python list
print(f"List memory usage: {python_list.__sizeof__()} bytes (approx)")

# Display the exact memory usage of the NumPy array
print(f"NumPy memory usage: {numpy_array.nbytes} bytes (exact)")

```

Result:
```python
List addition time: 0.5737 seconds
NumPy addition time: 0.00137 seconds
List mean: 50.00, time: 0.00294 seconds
NumPy mean: 50.00, time: 0.00126 seconds
List memory usage: 8448712 bytes (approx)
NumPy memory usage: 8000000 bytes (exact)
```