"""
Display Rectangle Number Pattern2
	Write a Python program that takes the number of `rows` and `columns` from the user and prints a rectangle pattern of numbers.

	In this pattern:
		- The first number of each row starts from the row number.
		- Each number in the row increases by 1 from the previous one.
	Input
	    $> Enter the Total Number of Rows : 5
	    Enter the Total Number of Columns : 5
	Output
	    1  2  3  4  5  
	    2  3  4  5  6  
	    3  4  5  6  7  
	    4  5  6  7  8  
	    5  6  7  8  9  
"""

try:
    rows = int(input("Enter the Total Number of Rows  : "))
    cols = int(input("Enter the Total Number of Columns  : "))

    for i in range(1, rows + 1):
        for j in range(i, i + cols):
            print(j, end="  ")
        print()

except ValueError:
    print("Invalid input! Please enter integers only.")
