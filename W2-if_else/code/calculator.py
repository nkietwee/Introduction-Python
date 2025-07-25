num1 = float(input("Enter number 1: "))
num2 = float(input("Enter number 2: "))
op = input("Enter operation (+, -, *, /): ")

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    if num2 != 0:
        print(num1 / num2)
    else:
        print("Error: Division by zero")
else:
    print("Invalid operation")