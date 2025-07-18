# Python `while` Loop

The `while` loop in Python allows you to repeat a block of code **as long as** a given condition remains true. It’s ideal for situations where **you don’t know beforehand how many times you need to iterate.**
_
---

## 1. Syntax

```python
while condition:
    # loop body
    statement_1
    statement_2
    ...
```

- **condition**: A Boolean expression evaluated before each iteration.
- **loop body**: One or more indented statements that execute on each iteration.

---

## 2. How It Works

1. Evaluate `condition`.
2. If `True`, execute the loop body, then go back to step 1.
3. If `False`, exit the loop 

---

## 3. Simple Example: Counting

```python
count = 1
while count <= 5:
	print("Count is:", count)
	count += 1
print("Done counting!")
```

**Output:**
```
Count is: 1
Count is: 2
Count is: 3
Count is: 4
Count is: 5
Done counting!
```

---

## 4. Using `break`

Prompt the user until they type “QUIT”:

```python
prompt = ""
while True:
	prompt = input("Enter command (type 'QUIT' to exit): ")
	if prompt == "QUIT":
		break
print("Goodbye!")
```

**Output:**
```
Enter command (type 'QUIT' to exit): hello
Enter command (type 'QUIT' to exit): Hello
Enter command (type 'QUIT' to exit): quit
Enter command (type 'QUIT' to exit): QUIT
Goodbye!
```
---

## 5. Using `break` and `continue`

- **`break`**: Exit the loop immediately.
- **`continue`**: Skip the rest of the current iteration and return to condition check.

```python
n = 0
while True:
	n += 1
	if n % 2 == 0:
		continue   # skip even numbers
	print(n)
	if n >= 9:
		break      # exit when n reaches 9
```

---

## 6. Common Pitfalls

1. **Infinite loops**  
   ```python
   while True:
       # remember to include a break or change the condition!
       …
   ```
2. **Forgetting to update loop variables**  
   ```python
   x = 0
   while x < 5:
       print(x)
       # missing: x += 1
   ```
---

## `for` Loop vs `while` Loop in Python

| Aspect                | `for` Loop                                      | `while` Loop                                       |
|-----------------------|-------------------------------------------------|----------------------------------------------------|
| **Use case**          | Iterating over a known sequence (list, range, etc.) | Repeating until a condition changes (unknown count) |
| **Syntax**            | `for item in iterable: …`                      | `while condition: …`                               |
| **Initialization**    | Built into the loop (takes elements from iterable) | You must initialize loop variables before the loop |
| **Termination**       | Automatically ends when iterable is exhausted   | Ends when `condition` evaluates to `False`         |
| **Control flow**      | Can use `break`/`continue`                      | Can use `break`/`continue`                         |
| **Predictability**    | Deterministic number of iterations              | May be non-deterministic—risk of infinite loops    |
| **Typical examples**  | – Looping over list of names<br>– `for i in range(10): …` | – Waiting for user input<br>– Polling a sensor until value drops below threshold |

---
