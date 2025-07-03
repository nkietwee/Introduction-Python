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

def number_guessing_game(max_num=30):
    """
    Simple number guessing game.
    The player must guess the number between 1 and max_num.
    """
    print("=== Number Guessing Game ===")
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
            print(f"🎉 Congratulations! You guessed it in {attempts} attempts.")
            break
        elif guess < target:
            print("⬆️ Higher!\n")
        else:
            print("⬇️ Lower!\n")

    print("Thanks for playing! 😊")

# Run the game
number_guessing_game()
