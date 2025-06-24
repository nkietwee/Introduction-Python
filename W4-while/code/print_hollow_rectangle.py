"""
Print a Hollow Rectangle

Ask for rows and columns, then use nested while loops to print a rectangle of * with hollow interior.

Input :
Rows: 3
Columns: 10

Output :
* * * * * * * * * *
*                 *
* * * * * * * * * *

"""

rows = int(input("\nEnter the total number of rows: "))
cols = int(input("Enter the total number of columns: "))

i = 1
while i <= rows:
	j = 1
	while j <= cols:
		# border cells are printed as "*", interior as space
		if i == 1 or i == rows or j == 1 or j == cols:
			print("*", end=" ")
		else:
			print(" ", end=" ")
		j += 1
	print()
	i += 1