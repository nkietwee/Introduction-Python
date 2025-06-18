"""
- Append data
	Take `n` inputs from the user and store them in a list
	Input
		$> Enter your number : 3
		Enter string : Hello
		Enter string : world
		Enter string : end
	Output
		['Hello', 'world', 'end']
"""

try:
	nbr = int(input("Enter number : "))
	lst = []
	for i in range(nbr):
		txt = input("Enter string : ")
		lst.append(txt)
	print(lst)
except ValueError:
	print("Please enter a valid integer.")
