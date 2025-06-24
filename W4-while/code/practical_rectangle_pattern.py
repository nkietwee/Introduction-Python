"""
Rectangle Pattern with Custom Number

Use two nested while loops: outer for rows, inner for columns. Fill with a user-provided number.
Sample Interaction:

Input:
	Rows: 6
	Columns: 12
	Fill number: 9

Output
	9 9 9 9 9 9 9 9 9 9 9 9
	9 9 9 9 9 9 9 9 9 9 9 9
	9 9 9 9 9 9 9 9 9 9 9 9
	9 9 9 9 9 9 9 9 9 9 9 9
	9 9 9 9 9 9 9 9 9 9 9 9
	9 9 9 9 9 9 9 9 9 9 9 9

"""

rows = int(input("Enter the total number of rows: "))
cols = int(input("Enter the total number of columns: "))
fill = input("Enter any number to fill the rectangle: ")

i = 0
while i < rows:
	j = 0
	while j < cols:
		print(fill, end=" ")
		j += 1
	print()
	i += 1
