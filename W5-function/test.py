# def hello_world():
#     # print("Hello, World!")
#     return "Hello, World!"

# print(hello_world())
# print(hello_world())
# print(hello_world())
# print(hello_world())
# print(hello_world())
# print(hello_world())


# def what_is_your_age(age, default_age=20):
#     return f"My age is {age}"
# age = input("Enter your age: ")
# print(what_is_your_age(age))

# def what_is_your_name(fname, lname="Smith"):
#     return f"My name is {fname} {lname}"

# name = input("Enter your name: ")
# surname = input("Enter your surname: ")
# print(what_is_your_name(name, surname))

# def my_function(*kids):
#   print("The youngest child is " + kids[2])

# my_function("Boat", "Mew", "Placartoon", "Mewtwo", "Mewthree")

# kids = ["Boat", "Mew", "Placartoon", "Mewtwo", "Mewthree"]

# def my_function(child3, child2, child1):
#   print("The youngest child is " + child3)

# my_function(child1 = "Boat", child3 = "Mew", child2 = "Placartoon")

# def my_function(**kid):
#   print("His last name is " + kid["fname"])

# kid = {
#     "fname": "Peerapol",
#     "lname": "Srisawat"
# }

# my_function(fname = "Peerapol", lname = "Srisawat")

# def my_function(country = "Thailand"):
#   print("I am from " + country)

# my_function("Sweden")
# my_function("India")
# my_function()
# my_function("Brazil")

# def my_function(food):
#   for x in food:
#     print(x)

# fruits = ["apple", "banana", "cherry"]

# my_function(fruits)

# def cal_grade(score):

#     pass

# print("Your score is:")

# def my_function(x, /):
#   print(x)

# my_function(x = 3)

# def my_function(a, b, /, *, c, d):
#   print(a + b + c + d)

# my_function(5, 6, c = 7, d = 8)

# def tri_recursion(k):# 6 5 4 3 2 1 0
# #   print("k =", k)
#   if(k > 0):
#     result = k + tri_recursion(k - 1) # 6 5 4 3 2 1 0
#     print(result) # 1 3
#   else:
#     result = 0
#   return result

# print("Recursion Example Results:")
# tri_recursion(6)


# 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 6765 10946

# import random
# """
#     Guess a number between 1 and 30: hello
#     ❌ Please enter a number!
#     Guess a number between 1 and 30: 15
#     ⬆️ Higher!
#     Guess a number between 1 and 30: 25
#     ⬇️ Lower!
#     Guess a number between 1 and 30: 20
#     🎉 Congratulations! You guessed it in 3 attempts.
#     Thanks for playing! 😊
# """

# def number_guessing_game(max_num=30):
#     """
#     Simple number guessing game.
#     The player must guess the number between 1 and max_num.
#     """
#     print("=== Number Guessing Game ===")
#     target = random.randint(1, max_num)
#     attempts = 0
#     print(f"Guess a number between 1–{max_num}")

#     while True:
#         guess = input(f"Round {attempts+1} — Guess your number: ")

#         if not guess.isdigit():
#             print("❌ Please enter a number!")
#             continue

#         guess = int(guess)
#         attempts += 1

#         if guess == target:
#             print(f"🎉 Congratulations! You guessed it in {attempts} attempts.")
#             break
#         elif guess < target:
#             print("⬇️ Lower!\n")
#         else:
#             print("⬆️ Higher!\n")

#     print("Thanks for playing! 😊")

# # Run the game
# number_guessing_game()

# def say_mew():
#     print("Mew!")

# def say_boat():
#     print("Boat!")

# def say_placartoon():
#     print("Placartoon!")

# def say_hello():
#     print("Hello!")
#     say_boat()
#     say_placartoon()

# say_hello()