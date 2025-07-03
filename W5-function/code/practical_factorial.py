def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

nbr = int(input("Enter a number to calculate its factorial: "))
print(factorial(nbr))
