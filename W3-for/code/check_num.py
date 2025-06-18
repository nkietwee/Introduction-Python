"""
Check numeric value
	Write a program that checks the numeric values ​​in a list and only displays values ​​greater than 20.
	Given:
		lsts = [10, 20, 30, 40, 50]
	Output:
		30
		40
		50
"""

lsts = [10, 20, 30, 40, 50]

for lst in lsts:
	if lst > 20:
		print(lst)
