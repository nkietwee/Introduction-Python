"""
Fizzbuzz
	Uses a for loop to iterate from 1 to 100
	For each number in this range:
	- If the number is divisible by both 3 and 5, print "FizzBuzz"
	- If the number is divisible by 3, print "Fizz"
	- If the number is divisible by 5, print "Buzz"
	- Else, print the number itself
    Output:
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
"""

for i in range(1, 101):
	if i % 3 == 0 and i % 5 == 0:
		print('Fizzbuzz')
	elif i % 3 == 0:
		print('Fizz')
	elif i % 5 == 0:
		print('Buzz')
	else:
		print(i)
		
