"""
Count string
	Write a program that checks the string and count `c` in string
"""

# Method 1
txt = "catcc"
cnt = 0

for c in txt:
	if c == 'c':
		cnt += 1

print(f'cnt : {cnt}')

# Method 2
txt = "catcc"
print(f'cnt : {txt.count("c")}')