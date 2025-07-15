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
- #### Basic array
```python
a = np.array([1, 2, 3]) # or a = np.array((1, 2, 3))
```
- Creates a NumPy array from a Python sequence such as list tuple.
- Used to convert regular lists into fast, vectorized arrays.

**Output:**
```python
array([1, 2, 3])
```

```python
a = np.array([[1, 2, 3], [4, 5, 6]])  #or a = np.array(((1, 2, 3,), (4, 5, 6)))
```
- Creates a NumPy 2D array from a Python sequence such as list tuple.
- Used to convert regular lists into fast, vectorized arrays.

**Output:**
```python
[[1 2 3]
 [4 5 6]]
```

- #### Create an Array of Zeros
```python
b = np.zeros((2, 3))
```
- Creates a 2x3 matrix filled with zeros.
- Useful for initializing weights in AI models.

**Output:**
```python
array([[0., 0., 0.],
       [0., 0., 0.]])
```

- #### Create an Array of Ones
```python
c = np.ones((3, 5))
```
- Creates a 3x3 matrix filled with ones.
- Often used to simulate filters or constant matrices.

**Output:**
```python
[[1. 1. 1. 1. 1.]
 [1. 1. 1. 1. 1.]
 [1. 1. 1. 1. 1.]]
```

- #### Create a Range of Values
```python
d = np.arange(0, 10, 2) # start stop step
```
- Creates values from 0 to 8, stepping by 2.
- Similar to Python range(), but returns a NumPy array.

**Output:**
```python
array([0, 2, 4, 6, 8])
```

- #### Create Evenly Spaced Values
```python
e = np.linspace(0, 1, 5)
```
- Creates 5 evenly spaced values between 0 and 1.
- Useful for graph axes, test values, or dividing a range smoothly.

**Output:**
```python
array([0.  , 0.25, 0.5 , 0.75, 1.  ])
```

## Summary Table

| Syntax                 | Description                      | Example Output                         |
| ---------------------- | -------------------------------- | -------------------------------------- |
| `np.array([1, 2, 3])`  | Convert list to NumPy array      | `[1, 2, 3]`                            |
| `np.array(((1, 2, 3), (4, 5, 6)))`  | Convert tuple to NumPy array      | `[[1, 2, 3],  [4 5 6]]`                            |
| `np.zeros((2, 3))`     | Create 2x3 array of zeros        | `[[0. 0. 0.], [0. 0. 0.]]`             |
| `np.ones((3, 3))`      | Create 3x3 array of ones         | `[[1. 1. 1.], [1. 1. 1.], [1. 1. 1.]]` |
| `np.arange(0, 10, 2)`  | Range from 0 to 8 with step of 2 | `[0, 2, 4, 6, 8]`                      |
| `np.linspace(0, 1, 5)` | 5 values between 0 and 1         | `[0. , 0.25, 0.5, 0.75, 1. ]`          |

### 3. Array Properties
- #### a.shape

```python
a = np.array(((1, 2, 3,), (4, 5, 6)))
a.shape
```
Returns the shape (rows, columns) of the array a.

**Output:**
```python
(2, 3)
```

- #### b.size

```python
np.ones((3, 3)).size
```
Returns the shape (rows, columns) of the array a.

**Output:**
```python
9
```
## Summary Table

| Property  | Description                        | Example Output |
| --------- | ---------------------------------- | -------------- |
| `a.shape` | Shape of the array (rows, columns) | `(2, 3)`         |
| `c.size`  | Total number of elements           | `9`            |

### 4. Indexing and Slicing


### 5. Array Operations
### 6. Reshaping Arrays
### 7. Stacking Arrays
### 8. Random Numbers


