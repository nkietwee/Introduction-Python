"""
Calculator
	The program takes two user inputs and performs addition, subtraction, division, and multiplication, then prints the results if input value not equal 40
	Input
		$> python3 calculator.py
		Give me the first number: 5
		Give me the second number: 2
	Output
	5 + 2 = 7
	5 - 2 = 3
	5 * 2 = 10
	5 / 2 = 2.50
"""
try:
	num1 = int(input("Give me the first number: "))
	num2 = int(input("Give me the second number: "))

	if num1 == 40 or num2 == 40:
		print("Input is equal 40")
		exit()

	print(f"{num1} + {num2} = {num1 + num2}")
	print(f"{num1} - {num2} = {num1 - num2}")
	print(f"{num1} * {num2} = {num1 * num2}")

	try:
		div = num1 / num2
		print(f"{num1} / {num2} = {div:.2f}")
	except ZeroDivisionError:
		print("Cannot divide by zero.")


except ValueError:
	print("Invalid input. Please enter integers only.")
