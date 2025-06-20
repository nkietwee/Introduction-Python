# Python `for` Loop - Detailed Explanation

## Table of Contents
1. [Introduction to `for` Loops](#introduction-to-for-loops)
2. [Basic Syntax](#basic-syntax)
3. [Iterating Over Different Data Types](#iterating-over-different-data-types)
4. [The `range()` Function](#the-range-function)
5. [Loop Control Statements](#loop-control-statements)
6. [Nested `for` Loops](#nested-for-loops)
---

## Introduction to `for` Loops

A `for` loop in Python is used for iterating over a sequence (like a list, tuple, dictionary, set, or string) or other iterable objects. It's one of the most commonly used loops in Python when you want to execute a block of code repeatedly for each item in a sequence.

Key characteristics:
- Executes a block of code for each item in an iterable
- Automatically handles iteration and termination
- More pythonic than `while` loops for sequence iteration

---

## Basic Syntax

```python
for item in iterable:
    # code to execute for each item
    print(item)
```
Components:
- item: A variable that takes the value of each item in the iterable
- iterable: Any Python object capable of returning its members one at a time
- Colon (`:`) marks the start of the loop body
- Indented block contains the code to be executed

**Example**:

```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```

**Output**:

```
apple
banana
cherry
```

## **Iterating Over Different Data Types**

**1. Strings**
```python

txts = "Hello"
for char in txts:
    print(char)
```
**Output**:

```
H
e
l
l
o
```

**2. Lists**
```python

numbers = [1, 2, 3]
for num in numbers:
    print(num * 2)
```
**Output**:

```
2
4
6
```

**3. Tuples**
```python
colors = ("red", "green", "blue")
for color in colors:
    print(color)
```
**Output**:

```
RED
GREEN
BLUE
```

**4. Dictionaries**
```python
person = {"name": "Alice",
            "age": 25}
for key in person:
    # print(key)
    print(f'{key} : {person[key]}')
```
**Output**:

```
name : Alice
age : 25
```
To iterate over items (**key-value pairs**):

```python
person = {"name": "Alice",
            "age": 25}
for key, value in person.items():
    print(f'{key} : {value}')
```
**Output**:

```
name : Alice
age : 25
```

## **The `range()` Function**
`range()` generates a sequence of numbers, commonly used in `for` loops.

syntax
```
range(start, stop, step)
```

Forms:

1. `range(stop)`
```python
for i in range(5):
    print(i)
```

**Output**:

```
0
1
2
3
4
```

2. `range(start, stop)`
```python
for i in range(2, 6):
    print(i)
```

**Output**:

```
2
3
4
5
```

3. `range(start, stop, step)`
```python
for i in range(0, 10, 2):
    print(i)
```

**Output**:

```
0
2
4
6
8
```

```python
for i in range(20, 10, -2):
    print(i)
```

**Output**:

```
20
18
16
14
12
```

4. `range(len(data))`
```python
lsts = [10, 20, 30, 40]
for i in range(len(lsts)):
    print(lsts[i])
```

**Output**:

```
10
20
30
40
```

```python
txts = 'Hello World'
for i in range(len(txts)):
    print(txts[i])
```

**Output**:

```
H
e
l
l
o

W
o
r
l
d
```
## **Loop Control Statements**

1. `break`
Terminates the loop entirely:
```python
for num in range(10):
    if num == 5:
        break
    print(num)
```

**Output**:

```
0
1
2
3
4
```

2. `continue`
Skips the current iteration:

```python
for num in range(10):
    if num % 2 == 0:
        continue
    print(num)
```

**Output**:

```
1
3
5
7
9
```

## Nested for Loops
A for loop inside another for loop:
```python
for i in range(5):
    for j in range(2):
        print(f"i : {i}, j : {j}")
```
**Output**:

```
i : 0, j : 0
i : 0, j : 1
i : 1, j : 0
i : 1, j : 1
i : 2, j : 0
i : 2, j : 1
i : 3, j : 0
i : 3, j : 1
i : 4, j : 0
i : 4, j : 1
```

