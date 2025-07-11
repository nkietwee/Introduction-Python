# Python `Function` 

A `function` is a block of code which only runs when it is called.
You can pass data, known as parameters, into a `function`.
A `function` can return data as a result.

---

## 1. Syntax

```python
def name_of_function():
    # statement body
    statement_1
    statement_2
    ...
```

- **name_of_function**: Name it anything that is consistent with the function.
- **statement body**: One or more indentation commands executed in a function.

---

## 2. Creating a Function

In Python a function is defined using the `def` keyword:

```python
def my_function():
    print("Hello from a fucntion")
```

## 3. Calling a Function

```python
def my_function():
    print("Hello from a function")

my_function()
```

**Output:**
```
Hello from a function
```

## 4. Arguments

Information can be passed into functions as arguments.
Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.
The following example has a function with one argument (fname). When the function is called, we pass along a first name, which is used inside the function to print the full name:

```python
def my_function(fname):
  print(fname + " Smite")

my_function("Emil")
my_function("Tobias")
my_function("Linus")
```

**Output:**
```
Emil Smite
Tobias Smite
Linus Smite
```

## 5. Number of Arguments

By default, a function must be called with the correct number of arguments. Meaning that if your function expects 2 arguments, you have to call the function with 2 arguments, not more, and not less.

**This function expects 2 arguments, and gets 2 arguments:**

**✅ Correct**

**
```python
def my_function(fname, lname):
  print(fname + " " + lname)
my_function("Peerapol", "Srisawat")
```
**Output:**
```
Peerapol Srisawat
```

**❌ Not correct**

This function expects 2 arguments, but gets only 1:

```python
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Peerapol")
```

## 6. Arbitrary Arguments, *args

If you do not know how many arguments that will be passed into your function, add a `*` before the parameter name in the function definition.
This way the function will receive a tuple of arguments, and can access the items accordingly:

If the number of arguments is unknown, add a `*` before the parameter name:

```python
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Boat", "Mew", "Placartoon")
```

**Output:**
```
The youngest child is Placartoon
```

## 7. Keyword Arguments

You can also send arguments with the `key = value` syntax.
This way the order of the arguments does not matter.

```python
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Boat", child2 = "Mew", child3 = "Placartoon")
```

## 8. Arbitrary Keyword Arguments, **kwargs

If you do not know how many keyword arguments that will be passed into your function, add two asterisk: `**` before the parameter name in the function definition.
This way the function will receive a dictionary of arguments, and can access the items accordingly:

If the number of keyword arguments is unknown, add a double `**`before the parameter name:

```python
def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Peerapol", lname = "Srisawat")
```

**Output:**
```
His last name is Srisawat
```

## 9. Default Parameter Value

The following example shows how to use a default parameter value.
If we call the function without argument, it uses the default value:

```python
def my_function(country = "Thailand"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")
```

**Output:**
```
I am from Sweden
I am from India
I am from Thailand
I am from Brazil
```

## 10. Passing a List as an Argument

You can send any data types of argument to a function (string, number, list, dictionary etc.), and it will be treated as the same data type inside the function.
E.g. if you send a List as an argument, it will still be a List when it reaches the function:

```python
def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)
```

**Output:**
```
apple
banana
cherry
```

## 11. Return Values

To let a function return a value, use the `return` statement:

```python
def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))
```

**Output:**
```
15
25
45
```

## 12. The pass Statement

function definitions cannot be empty, but if you for some reason have a function definition with no content, put in the pass statement to avoid getting an error.

```python
def myfunction():
  pass
```

## 13. Positional-Only Arguments

You can specify that a function can have ONLY positional arguments, or ONLY keyword arguments.
To specify that a function can have only positional arguments, add `, /` after the arguments:

**✅ Correct**

```python
def my_function(x, /):
  print(x)

my_function(3)
```

**Output:**
```
3
```

Without the `, /` you are actually allowed to use keyword arguments even if the function expects positional arguments:

```python
def my_function(x):
  print(x)

my_function(x = 3)
```

**Output:**
```
3
```

**❌ Not correct**

But when adding the `, /` you will get an error if you try to send a keyword argument:

```python
def my_function(x, /):
  print(x)

my_function(x = 3)
```

## 14. Keyword-Only Arguments

To specify that a function can have only keyword arguments, add `*, ` before the arguments:

**✅ Correct**

```python
def my_function(*, x):
  print(x)

my_function(x = 3)
```

**Output:**
```
3
```

Without the `*, ` you are allowed to use positional arguments even if the function expects keyword arguments:

```python
def my_function(x):
  print(x)

my_function(3)
```

**Output:**
```
3
```

**❌ Not correct**

But with the `*, ` you will get an error if you try to send a positional argument:

```python
def my_function(*, x):
  print(x)

my_function(3)
```

## 15. Combine Positional-Only and Keyword-Only

You can combine the two argument types in the same function.

Any argument before the `/ , ` are positional-only, and any argument after the `*, ` are keyword-only.

```python
def my_function(a, b, /, *, c, d):
  print(a + b + c + d)

my_function(5, 6, c = 7, d = 8)
```

**Output:**
```
26
```

## 16. Recursion

Python also accepts function recursion, which means a defined function can call itself.

Recursion is a common mathematical and programming concept. It means that a function calls itself. This has the benefit of meaning that you can loop through data to reach a result.

The developer should be very careful with recursion as it can be quite easy to slip into writing a function which never terminates, or one that uses excess amounts of memory or processor power. However, when written correctly recursion can be a very efficient and mathematically-elegant approach to programming.

In this example, `tri_recursion()` is a function that we have defined to call itself ("recurse"). We use the `k` variable as the data, which decrements `(-1)` every time we recurse. The recursion ends when the condition is not greater than 0 (i.e. when it is 0).

To a new developer it can take some time to work out how exactly this works, best way to find out is by testing and modifying it.

```python
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("Recursion Example Results:")
tri_recursion(6)
```

**Output:**
```
Recursion Example Results:
1
3
6
10
15
21
```
