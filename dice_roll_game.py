import random

name = input('What is your name?\n')

def goodbye():
    print('Thanks for playing Roll the Dice with me,', name + '! Come again!')

print(f'Hello {name}, welcome to my dice rolling game.\nType "quit" in any prompt to exit.\n')

def dice_game():
    while True:
        # Dice sides input
        sides = input('How many sides would you like your dice to have? ').lower()
        if sides == 'quit':
            goodbye()
            break
        try:
            sides = int(sides)
            if sides < 2:
                print("Dice must have at least 2 sides!")
                continue
        except ValueError:
            print("Invalid input! Enter a number or 'quit'.")
            continue

        # Number of dice input
        num_dice = input('How many dice do you want to roll? ').lower()
        if num_dice == 'quit':
            goodbye()
            break
        try:
            num_dice = int(num_dice)
            if num_dice < 1:
                print("You must roll at least 1 die!")
                continue
        except ValueError:
            print("Invalid input! Enter a number or 'quit'.")
            continue

        # Roll dice
        rolls = [random.randint(1, sides) for _ in range(num_dice)]
        total = sum(rolls)

        print("Rolls:", rolls)
        print("Total:", total)

        # Replay prompt
        decision = input("Would you like to play again? (Yes/No): ").lower()
        if decision not in ['yes', 'y']:
            goodbye()
            break
        print(f"\nWelcome back, {name}!\n")

dice_game()

