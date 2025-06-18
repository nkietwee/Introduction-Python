"""
Filter Students Who Passed
	Write a Python program that filters and prints the names of students who scored above a passing threshold using a dictionary and a for loop.
	Given:
	    scores = {
        "Alice": 85,
        "Bob": 58,
        "Charlie": 92,
        "David": 49}
	threshold = 60
	Output:
    	Alice: 85  
	    Charlie: 92

"""

scores = { "Alice": 85,
        "Bob": 58,
        "Charlie": 92,
        "David": 49}
threshold = 60

for key, value in scores.items():
    if value > 60:
        print(f'{key}: {value}')