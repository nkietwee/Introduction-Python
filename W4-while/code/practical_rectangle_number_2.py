"""
Display Rectangle Number Pattern 2

First number in row i is i; each subsequent number increments by 1. Use nested while.

Input :
	Rows: 5
	Columns: 5

Output :
	1 2 3 4 5
	2 3 4 5 6
	3 4 5 6 7
	4 5 6 7 8
	5 6 7 8 9


"""

rows = int(input("\nEnter the total number of rows: "))
cols = int(input("Enter the total number of columns: "))

i = 1
while i <= rows:
	j = 0
	while j < cols:
		print(i + j, end=" ")
		j += 1
	print()
	i += 1