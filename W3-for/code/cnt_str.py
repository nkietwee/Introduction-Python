"""
Count character
	Write a program that checks the string and count `c` in string
	**Given**:
	```
		txts = "cat"
		char_to_count = "c"
	```
	**Output**:
	```
	The character 'c' appears 0 times in the string 'bread'.
	```
"""

# Method 1
txts = "cat"
char_to_count = "c"

cnt = 0

for c in txts:
	if c == 'c':
		cnt += 1

print(f'The character {char_to_count} appears {cnt} times in the string {txts}')

# Method 2
txts = "cat"
char_to_count = "c"
print(f'The character {char_to_count} appears {txts.count(char_to_count)} times in the string {txts}')
