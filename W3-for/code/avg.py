"""
Find average in a List
	Write a program that checks the numeric values ​​in a list and find average.
	Given:
		lsts = [10, 20, 30, 40, 50]
	Output:
		Averaage of the list [10, 20, 30, 40, 50] is 30
"""

summ = 0
lsts = [10, 20, 30, 40, 50]


# method 1 
for lst in lsts:
	summ += lst
 
print(f'Averaage of the list {lsts} is {summ / len(lsts)}')

# method 2
avg = sum(lsts) / len(lsts)
print(f'Averaage of the list {lsts} is {avg}')
