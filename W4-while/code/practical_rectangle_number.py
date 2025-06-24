"""
Display Rectangle Number Pattern 1

Print the numbers 1…C on each row for R rows, using nested while.

Input :
	Rows: 7
	Columns: 10

Output :

	1 2 3 4 5 6 7 8 9 10
	1 2 3 4 5 6 7 8 9 10
	1 2 3 4 5 6 7 8 9 10
	1 2 3 4 5 6 7 8 9 10
	1 2 3 4 5 6 7 8 9 10
	1 2 3 4 5 6 7 8 9 10
	1 2 3 4 5 6 7 8 9 10
"""

rows = int(input("\nEnter the total number of rows: "))
cols = int(input("Enter the total number of columns: "))

i = 0
while i < rows:
	j = 1
	while j <= cols:
		print(j, end=" ")
		j += 1
	print()
	i += 1