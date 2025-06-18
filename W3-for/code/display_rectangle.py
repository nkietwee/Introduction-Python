"""
- Display Rectangle Number Pattern
	Write a Python program that takes the number of `rows` and `columns` from the user and prints a rectangle pattern of numbers.

	Each row should display numbers starting from 1 up to the number of columns, and this pattern should be repeated for the total number of rows.
	Input
	    Enter the Total Number of Rows  : 7
	    Enter the Total Number of Columns  : 10
	Output
	    Rectangle Number Pattern
	    1  2  3  4  5  6  7  8  9  10  
	    1  2  3  4  5  6  7  8  9  10  
	    1  2  3  4  5  6  7  8  9  10  
	    1  2  3  4  5  6  7  8  9  10  
	    1  2  3  4  5  6  7  8  9  10  
	    1  2  3  4  5  6  7  8  9  10  
	    1  2  3  4  5  6  7  8  9  10 
"""
# method1
try:
    rows = int(input("Enter the Total Number of Rows  : "))
    columns = int(input("Enter the Total Number of Columns  : "))

    print("Rectangle Number Pattern")
    for i in range(1, rows + 1):
        for j in range(1, columns + 1):
            print(j, end='  ')
        print()

except ValueError:
    print("Invalid input! Please enter an integer number.")
