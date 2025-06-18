"""
Rectangle Pattern with Custom Number**
	Write a Python program that:
	1. Asks the user to input:
		- Total number of rows
		- Total number of columns
		- Any number to fill the rectangle
	2. Prints a rectangle number pattern using the entered number, repeated in the given rows and columns.
	Input
    	$> Enter the Total Number of Rows  : 6
	    Enter the Total Number of Columns  : 12
	    Enter Any Number  : 9
	Output
	    Rectangle Number Pattern
	    9  9  9  9  9  9  9  9  9  9  9  9  
	    9  9  9  9  9  9  9  9  9  9  9  9  
	    9  9  9  9  9  9  9  9  9  9  9  9  
	    9  9  9  9  9  9  9  9  9  9  9  9  
	    9  9  9  9  9  9  9  9  9  9  9  9  
	    9  9  9  9  9  9  9  9  9  9  9  9
"""
try:
    rows = int(input("Enter the Total Number of Rows  : "))
    columns = int(input("Enter the Total Number of Columns  : "))
    number = int(input("Enter Any Number  : "))

    print("Rectangle Number Pattern")
    for i in range(rows):
        for j in range(columns):
            print(number, end='  ')
        print()

except ValueError:
    print("Invalid input! Please enter valid integer values.")
