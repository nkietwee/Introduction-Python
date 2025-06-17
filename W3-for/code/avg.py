"""
Find average in a List
	Write a program that checks the numeric values ​​in a list and find average.
"""

summ = 0
lsts = [10, 20, 30, 40, 50]
for lst in lsts:
	summ += lst
 
print(f'avg : {summ / len(lsts)}')
