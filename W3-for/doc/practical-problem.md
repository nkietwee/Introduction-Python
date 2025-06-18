## **Practical Examples**
### numerical
- **Check numeric value**
	Write a program that checks the numeric values ​​in a list and only displays values ​​greater than 20.
	**Given**:
	```
	lsts = [10, 20, 30, 40, 50]
	```
	**Output**:
	```
	30
	40
	50
	```
- **Find average in a List**
	Write a program that checks the numeric values ​​in a list and find average.
	**Given**:
	```
	lsts = [10, 20, 30, 40, 50]
	```
	**Output**:
	```
	Averaage of the list [10, 20, 30, 40, 50] is 30
	```	
- **Fizzbuzz_asd**
	Uses a for loop to iterate from 1 to 100
	For each number in this range:
	- If the number is divisible by both 3 and 5, print "FizzBuzz"
	- If the number is divisible by 3, print "Fizz"
	- If the number is divisible by 5, print "Buzz"
	- Else, print the number itself
	**Output**:
	```
	1
	2
	Fizz
	4
	Buzz
	Fizz
	7
	8
	Fizz
	Buzz
	11
	Fizz
	13
	14
	Fizzbuzz
	...
	Fizzbuzz
	91
	92
	Fizz
	94
	Buzz
	Fizz
	97
	98
	Fizz
	Buzz
	```	
- **Fizzbuzz_des**
	Uses a for loop to iterate from 100 to 1
	For each number in this range:
	- If the number is divisible by both 3 and 5, print "FizzBuzz"
	- If the number is divisible by 3, print "Fizz"
	- If the number is divisible by 5, print "Buzz"
	- Else, print the number itself
	**Output**:
	```
	Buzz
	Fizz
	98
	97
	Fizz
	Buzz
	94
	Fizz
	92
	91
	Fizzbuzz
	...
	Fizzbuzz
	14
	13
	Fizz
	11
	Buzz
	Fizz
	8
	7
	Fizz
	Buzz
	4
	Fizz
	2
	1
	```
- **Calculator**
	The program takes two user inputs and performs addition, subtraction, division, and multiplication, then prints the results if input value not equal 40
	**Input**
	```shell
	$> python3 calculator.py
	Give me the first number: 5
	Give me the second number: 2
	```
	**Output**
	```shell
	5 + 2 = 7
	5 - 2 = 3
	5 * 2 = 10
	5 / 2 = 2.50
	```


### string
- **Count character**
	Write a program that checks the string and count `c` in string
	**Given**:
	```
	txts = "cat"
	char_to_count = "c"
	```
	**Output**:
	```
	The character c appears 1 times in the string cat.
	```
- **Find string in list**
	Write a program that checks the string ​​in a list and displays `Found` is string equal `green`.
	**Given**:
	```
	lsts = ['red', 'green', 'blue']
	```
	**Output**:
	```
	found
	```

### dict
- **Filter Students Who Passed**
	Write a Python program that filters and prints the names of students who scored above a passing threshold using a dictionary and a for loop.
	**Given**:
	```python
	scores = {
    "Alice": 85,
    "Bob": 58,
    "Charlie": 92,
    "David": 49
	}
	threshold = 60

	```
	**Output**:
	```python
	Alice: 85  
	Charlie: 92

	```




### list
- **Append data**
	Take `n` inputs from the user and store them in a list
	**Input**
	```
	$> Enter your number : 3
	Enter string : Hello
	Enter string : world
	Enter string : end
	```
	**Output**
	```
	['Hello', 'world', 'end']
	```
- **Print and Sum data**
	Write a Python program that displays a list of items along with their corresponding prices, and calculates the total cost of all items.
	**Given**:
	```
		items = ["apple", "banana", "milk", "bread"]
		prices = [10, 5, 20, 15]
	```
	**Output**:
	```
		apple: 10 baht
		banana: 5 baht
		milk: 20 baht
		bread: 15 baht

		Total: 50 baht
	```
	
### Nested Loop
- **Rectangle Pattern with Custom Number**
	Write a Python program that:
	1. Asks the user to input:
		- Total number of rows
		- Total number of columns
		- Any number to fill the rectangle
	2. Prints a rectangle number pattern using the entered number, repeated in the given rows and columns.
		**Input**
	```
	$> Enter the Total Number of Rows  : 6
	Enter the Total Number of Columns  : 12
	Enter Any Number  : 9
	```
	**Output**
	```
	Rectangle Number Pattern
	9  9  9  9  9  9  9  9  9  9  9  9  
	9  9  9  9  9  9  9  9  9  9  9  9  
	9  9  9  9  9  9  9  9  9  9  9  9  
	9  9  9  9  9  9  9  9  9  9  9  9  
	9  9  9  9  9  9  9  9  9  9  9  9  
	9  9  9  9  9  9  9  9  9  9  9  9  

	```

- **Display Rectangle Number Pattern**
	Write a Python program that takes the number of `rows` and `columns` from the user and prints a rectangle pattern of numbers.

	Each row should display numbers starting from 1 up to the number of columns, and this pattern should be repeated for the total number of rows.
	**Input**
	```
	$> Enter the Total Number of Rows  : 7
	Enter the Total Number of Columns  : 10
	```
	**Output**
	```
	Rectangle Number Pattern
	1  2  3  4  5  6  7  8  9  10  
	1  2  3  4  5  6  7  8  9  10  
	1  2  3  4  5  6  7  8  9  10  
	1  2  3  4  5  6  7  8  9  10  
	1  2  3  4  5  6  7  8  9  10  
	1  2  3  4  5  6  7  8  9  10  
	1  2  3  4  5  6  7  8  9  10 
	```








