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
  Write a Python script that implements the following game using a while loop.

  **Setup**
   - Import the standard random module.
   - Define max_num = 30.
   - Use random.randint(1, max_num) to choose a secret number between 1 and 30.
   - Initialize an attempt counter to 0.
  **Gameplay Loop**
   - Repeatedly prompt the user with:
   ```
	Round x - Guess Your Number:
   ```
   - If the user enters anything other than digits, print
   ```
	❌ Please enter a number!
   ```
   and ask again (without counting it as an attempt).
   - Convert valid input to an integer, increment the attempt counter, and compare to the secret number:
     - If the guess is correct, print
	```🎉 Congratulations! You guessed it in X attempts.```
     and exit the loop.
			- If the guess is lower than the secret number, print
		   	```⬆️ Higher!```
		   	- If the guess is higher, print
		   	```⬇️ Lower!```
		 - End of Game
		   After a correct guess, the program should print a farewell message, for example:
		   ```
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
