"""
Multiplication Table**
	Ask the user for a **positive integer** n and print its multiplication table up to 10 using a while loop.
	Sample Interaction:
	
	Enter a number: 7
	7 × 1 = 7
	7 × 2 = 14
	…
	7 × 11 = 77
	7 × 12 = 84
"""
try:
	nbr = int(input("Enter a number : "))
	if nbr < 0:
		print("Please enter a non-negative number.")
	else:
		i = 1
		while i <= 12:
			print(f'{nbr} x {i} = {nbr * i}')
			i += 1
except ValueError:
	print("Can't change datatype of number")