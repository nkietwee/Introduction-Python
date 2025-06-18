"""
Print a Rectangle
	Design a Python program that asks the user to input the number of `rows` and `columns` and then prints a hollow rectangle pattern using asterisks (*).

	The pattern should have * on the borders and spaces inside — like a picture frame.

	Input
    	$> Enter the Total Number of Rows  : 3
	    Enter the Total Number of Columns  : 10
	Output
	    * * * * * * * * * * 
	    *                 * 
	    * * * * * * * * * * 
"""

try:
    row = int(input("Enter the no of rows: "))
    col = int(input("Enter the no of columns: "))

    for i in range(row):
        for j in range(col):
            if i == 0 or i == row - 1 or j == 0 or j == col - 1:
                print('*', end=' ')
            else:
                print(' ', end=' ')
        print()

except ValueError:
    print("Invalid input! Please enter integer numbers only.")
