# mini_projects.py

import random
import string
import math

# 1️⃣ Goodbye function (shared)
def goodbye(name):
    print(f"Thanks for playing, {name}! Come again soon!")

# 2️⃣ Guessing Game
def guessing_game(name):
    secret = random.randint(1, 20)
    guesses = 0
    limit = 5

    print(f"\n{name}, I'm thinking of a number between 1 and 20. Can you guess it?")
    while guesses < limit:
        guess = input("Enter your guess: ")
        if not guess.isdigit():
            print("Please enter a valid number.")
            continue
        guess = int(guess)
        guesses += 1

        if guess == secret:
            print(f"🎉 Correct! The number was {secret}.")
            break
        elif guess < secret:
            print("Too low.")
        else:
            print("Too high.")
    else:
        print(f"😢 You're out of guesses. The number was {secret}.")

# 3️⃣ Dice Roller
def dice_game(name):
    print(f"\nWelcome to the Dice Roller, {name}!")
    while True:
        sides = input("Number of sides on your dice: ")
        if sides.lower() == "quit": break
        num_dice = input("How many dice? ")
        if num_dice.lower() == "quit": break

        if not (sides.isdigit() and num_dice.isdigit()):
            print("Numbers only!")
            continue

        sides = int(sides)
        num_dice = int(num_dice)

        rolls = [random.randint(1, sides) for _ in range(num_dice)]
        print(f"Rolls: {rolls}")
        print(f"Total: {sum(rolls)}")

        again = input("Roll again? (y/n): ").lower()
        if again not in ["y", "yes"]:
            break

# 4️⃣ Password Generator
def password_generator(name):
    print(f"\nWelcome to the Password Generator, {name}!")
    chars = string.ascii_letters + string.digits + string.punctuation
    while True:
        length = input("Password length: ")
        if length.lower() == "quit": break
        if not length.isdigit():
            print("Enter a number.")
            continue
        length = int(length)
        password = ''.join(random.choice(chars) for _ in range(length))
        print(f"Generated password: {password}")

        again = input("Generate another? (y/n): ").lower()
        if again not in ["y", "yes"]:
            break

# 5️⃣ Math Mini Challenge
def math_exercise(name):
    print(f"\nHi {name}, welcome to the Complicated Calculator.")
    while True:
        func = input("Choose: sqrt, log10, or sine: ").lower()
        num = input("Enter a number: ")

        try:
            num = float(num)
        except ValueError:
            print("Numbers only!")
            continue

        if func in ["sqrt", "square root"]:
            print(f"√{num} = {round(math.sqrt(num), 3)}")
        elif func in ["log", "log10"]:
            print(f"log10({num}) = {round(math.log10(num), 3)}")
        elif func in ["sin", "sine"]:
            print(f"sin({num}) = {round(math.sin(num), 3)}")
        else:
            print("Invalid function.")

        again = input("Try another? (y/n): ").lower()
        if again not in ["y", "yes"]:
            break
