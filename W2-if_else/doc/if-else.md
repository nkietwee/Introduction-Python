
# 🐍 Python `if...else` Statement

## 🧠 Basic Concept

In Python, we use `if`, `elif`, and `else` to **check conditions** and make decisions based on whether those conditions are true or false.

It’s like asking:
> If this is true, do this  
> Else if something else is true, do that  
> Else do something else

---

## 🔹 Syntax

```python
if condition:
    # code when condition is True
elif condition2:
    # code when condition2 is True (optional)
else:
    # code when none of the conditions are True (optional)
```

---

## 🔸 Example 1: Simple if...else

```python
x = 10

if x > 5:
    print("x is greater than 5")
else:
    print("x is less than or equal to 5")
```

---

## 🔸 Example 2: if...elif...else

```python
score = 75

if score >= 90:
    print("Grade A")
elif score >= 80:
    print("Grade B")
elif score >= 70:
    print("Grade C")
else:
    print("Grade D or lower")
```

---

## 🔸 Example 3: One-liner if...else (Ternary Operator)

```python
age = 18
status = "Adult" if age >= 18 else "Minor"
print(status)
```

---

## 🔹 Comparison Operators Table

| Operator | Meaning                   | Example                          |
|----------|---------------------------|----------------------------------|
| `==`     | Equal to                  | `if x == 10:`                    |
| `!=`     | Not equal to              | `if name != "admin":`            |
| `>`      | Greater than              | `if age > 18:`                   |
| `<`      | Less than                 | `if score < 50:`                 |
| `>=`     | Greater than or equal to  | `if level >= 3:`                 |
| `<=`     | Less than or equal to     | `if temp <= 100:`                |
| `and`    | Logical AND (both true)   | `if x > 5 and x < 10:`           |
| `or`     | Logical OR (either true)  | `if user == "admin" or is_admin:`|
| `not`    | Logical NOT               | `if not logged_in:`              |

---

## 🎓 Practice Exercise

```python
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")
```

---

## ✅ Tips

- Don't forget the `:` at the end of each `if`, `elif`, or `else`
- Indentation is critical (use 4 spaces or a tab)
- Using multiple `if` statements checks all conditions
- Using `if...elif...else` stops at the first true condition