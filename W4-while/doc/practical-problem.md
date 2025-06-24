## **Practical Examples**
### Basic While loop 
- **Multiplication Table**
	Ask the user for a **positive integer** n and print its multiplication table up to 10 using a while loop.
	Sample Interaction:
	**Input :**
	```shell
	$> python3 multiplication.py
	Enter a number: 7
	```
	**Output :**
	```shell
	7 × 1 = 7
	7 × 2 = 14
	…
	7 × 11 = 77
	7 × 12 = 84
	```

- **Prompt**
	This script should contain a while loop that accepts user input, writes a response,
	and only stops when the user enters `STOP` and print `Exit`
	**Output :**
	```shell
	I got that! Anything else? : I like ponies
	I got that! Anything else? : stop
	I got that! Anything else? : stop...
	I got that! Anything else? : STOP
	Exit
	```

- **Print number**
	This script should contain a while loop that print number since 0 to 10 except 5
	**Output :**
	```shell
	0 1 2 3 4 6 7 8 9 10
	```
- **Password prompt**
   Keep asking the user for a password until they enter the correct one. Limit attempts to 3 and then lock them out.
   **Given :**
   ```
	password = PaSsWoRd
	```
	**Output :**
	```shell
	Attempt 1 of 3: Pass
	Invalid password. Attempts left: 2
	Attempt 2 of 3: PaSS
	Invalid password. Attempts left: 1
	Attempt 3 of 3: PaSs
	Access granted!
	```
	```shell
	Attempt 1 of 3: sd
	Invalid password. Attempts left: 2
	Attempt 2 of 3: sd
	Invalid password. Attempts left: 1
	Attempt 3 of 3: sss
	Invalid password. Attempts left: 0
	```

- **Simple Number Guessing Game**  
  Write a Python script that implements the following game using a `while` loop.

  **Setup**  
  1. Import the standard `random` module.  
     ```python
     import random
     ```
  2. Define the maximum number:
     ```python
     max_num = 30
     ```
  3. Choose a secret number between 1 and 30:
     ```python
     target = random.randint(1, max_num)
     ```
  4. Initialize an attempt counter:
     ```python
     attempts = 0
     ```

  **Gameplay Loop**  
  Use a `while True` loop with these steps:
  1. Prompt the user (showing the current round):
     ```plaintext
     Round 1 – Guess Your Number:
     ```
  2. Read input and validate:
     - If input is not all digits, print:
       ```plaintext
       ❌ Please enter a number!
       ```
       and **continue** (do **not** increment `attempts`).
  3. Convert valid input to an integer and increment the counter:
     ```python
     guess = int(user_input)
     attempts += 1
     ```
  4. Compare `guess` to `target`:
     - **Correct**:  
       ```plaintext
       🎉 Congratulations! You guessed it in X attempts.
       ```  
       then **break** out of the loop.
     - **Too low**:  
       ```plaintext
       ⬆️ Higher!
       ```
     - **Too high**:  
       ```plaintext
       ⬇️ Lower!
       ```

  **End of Game**  
  After breaking out of the loop, print:
  ```plaintext
  Thanks for playing! 😊
  ```
### Nested while Loops

- **Rectangle Pattern with Custom Number**

Use two nested while loops: outer for rows, inner for columns. Fill with a user-provided number.
Sample Interaction:

**Input :** 
```
Rows: 6
Columns: 12
Fill number: 9
```

**Output**
```
9 9 9 9 9 9 9 9 9 9 9 9
9 9 9 9 9 9 9 9 9 9 9 9
9 9 9 9 9 9 9 9 9 9 9 9
9 9 9 9 9 9 9 9 9 9 9 9
9 9 9 9 9 9 9 9 9 9 9 9
9 9 9 9 9 9 9 9 9 9 9 9
```


- **Display Rectangle Number Pattern 1**

Print the numbers 1…C on each row for R rows, using nested while.

**Input :**
```
Rows: 7
Columns: 10
```

**Output :**

```
1 2 3 4 5 6 7 8 9 10
1 2 3 4 5 6 7 8 9 10
1 2 3 4 5 6 7 8 9 10
1 2 3 4 5 6 7 8 9 10
1 2 3 4 5 6 7 8 9 10
1 2 3 4 5 6 7 8 9 10
1 2 3 4 5 6 7 8 9 10
```


**Display Rectangle Number Pattern 2**

First number in row i is i; each subsequent number increments by 1. Use nested while.

**Input :**
```
Rows: 5
Columns: 5
```
**Output :**
```
1 2 3 4 5
2 3 4 5 6
3 4 5 6 7
4 5 6 7 8
5 6 7 8 9
```

**Print a Hollow Rectangle**
Ask for rows and columns, then use nested while loops to print a rectangle of * with hollow interior.

**Input :**
```
Rows: 3
Columns: 10
```

**Output :**
```
* * * * * * * * * *
*                 *
* * * * * * * * * *
```
