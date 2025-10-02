# Number Guessing Game (Portfolio Version) gpt edits
import random

def goodbye():
    print("Thank you for playing my Guessing Game! Come again soon!")

def play_game(name):
    secret_num = random.randint(1, 20)
    guess_count = 0
    guess_limit = 5
    guess = None

    print(f"\n{name}, I am thinking of a number between 1 and 20. Can you guess it?\n")

    while guess != secret_num and guess_count < guess_limit:
        try:
            guess = int(input("Enter your guess: "))
            guess_count += 1

            if guess < secret_num:
                print("Too low! Try again.\n")
            elif guess > secret_num:
                print("Too high! Try again.\n")
            else:
                print(f"YOU WIN! {guess} was the secret number in {guess_count} tries.\n")
                break
        except ValueError:
            print("Invalid input! Please enter a number.\n")

    if guess != secret_num:
        print(f"You're out of guesses! The number was {secret_num}.\n")

    # Ask to play again
    decision = input("Would you like to play again? (Yes/No): ").strip().lower()
    if decision in ['yes', 'y']:
        print(f"\nWelcome back, {name}!\n")
        play_game(name)  # recursion to restart the game
    else:
        goodbye()

# Start the game
player_name = input("Hi! What's your name? ")
play_game(player_name)
