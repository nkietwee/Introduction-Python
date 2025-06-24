"""
Print number
	This script should contain a while loop that print number since 0 to 10 except 5
	Output :
		1 2 3 4 6 7 8 9 10
	
"""

# method 1
i = 0
while i < 10:
	i+=1
	if i == 5:
		continue
	print(i, end=" ")
print() # print newline
# method 2
i = 0
while i <= 10:
	if i == 5:
		i += 1      # make sure to increment before continuing
		continue
	print(i, end=" ")
	i += 1
print() # print newline

# method 3
i = 0
while i <= 10:
	if i != 5:
		print(i, end=" ")
	i += 1
print() # print newline

