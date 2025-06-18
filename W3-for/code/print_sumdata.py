"""
- Print and Sum data
	Write a Python program that displays a list of items along with their corresponding prices, and calculates the total cost of all items.
	Given:
		items = ["apple", "banana", "milk", "bread"]
		prices = [10, 5, 20, 15]

	Output:
		Each item with its price in the format: item: price baht
		The total cost of all items in the format: Total: total baht
"""

items = ["apple", "banana", "milk", "bread"]
prices = [10, 5, 20, 15]

total = 0

for i in range(len(items)):
	print(f"{items[i]}: {prices[i]} baht")
	total += prices[i]
print()
print(f"Total: {total} baht")