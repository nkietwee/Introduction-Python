"""
	$> Enter the Total Number of Rows  : 6
	Enter the Total Number of Columns  : 12
	Enter Any Number  : 9
	```
	**Output**
	```
	Rectangle Number Pattern
	9  9  9  9  9  9  9  9  9  9  9  9  
	9  9  9  9  9  9  9  9  9  9  9  9  
	9  9  9  9  9  9  9  9  9  9  9  9  
	9  9  9  9  9  9  9  9  9  9  9  9  
	9  9  9  9  9  9  9  9  9  9  9  9  
	9  9  9  9  9  9  9  9  9  9  9  9  
"""

row = int(input("Enter the Total Number of Rows : "))
column = int(input("Enter the Total Number of columns : "))
nbr = input("Enter Any Number : ")
nbr = nbr + " "
# for i in range(row):
#     for j in range(column):
#         print(nbr, end=" ")
#     print()

for i in range(row):
    # for j in range(column):
    print(nbr * column)
    # print()
