"""
Fizzbuzz
	Uses a for loop to iterate from 100 to 1
	For each number in this range:
	- If the number is divisible by both 3 and 5, print "FizzBuzz"
	- If the number is divisible by 3, print "Fizz"
	- If the number is divisible by 5, print "Buzz"
	- Else, print the number itself
    
"""

for i in range(100, 0, -1):
	if i % 3 == 0 and i % 5 == 0:
		print('Fizzbuzz')
	elif i % 3 == 0:
		print('Fizz')
	elif i % 5 == 0:
		print('Buzz')
	else:
		print(i)
		
