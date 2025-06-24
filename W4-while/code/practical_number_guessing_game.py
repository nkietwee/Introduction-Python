import random
"""
    Guess a number between 1 and 30: hello
    ❌ Please enter a number!
    Guess a number between 1 and 30: 15
    ⬆️ Higher!
    Guess a number between 1 and 30: 25
    ⬇️ Lower!
    Guess a number between 1 and 30: 20
    🎉 Congratulations! You guessed it in 3 attempts.
    Thanks for playing! 😊
"""

print("=== Number Guessing Game ===")
max_num = 30
target = random.randint(1, max_num)
attempts = 0
print(f"Guess a number between 1–{max_num}")

while True:
    guess = input(f"Round {attempts+1} — Guess your number: ")
    if not guess.isdigit():
        print("❌ Please enter a number!")
        continue

    guess = int(guess)
    attempts += 1

    if guess == target:
        print(f"🎉 Congratulations! You guessed it in {attempts} attempts")
        break
    elif guess < target:
        print("⬆️ Higher!\n")
    else:
        print("⬇️ Lower!\n")

print("Thank You! 😊")
