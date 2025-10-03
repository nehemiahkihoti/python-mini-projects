# main.py

import mini_projects

def main():
    name = input("Hello! What is your name?\n")
    while True:
        print(f"""
==========================
 Welcome, {name} 👋
 Choose an option:
 1. Guessing Game
 2. Dice Roller
 3. Password Generator
 4. Complicated Calculator
 5. Quit
==========================
""")
        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            mini_projects.guessing_game(name)
        elif choice == "2":
            mini_projects.dice_game(name)
        elif choice == "3":
            mini_projects.password_generator(name)
        elif choice == "4":
            mini_projects.math_exercise(name)
        elif choice == "5":
            mini_projects.goodbye(name)
            break
        else:
            print("Invalid choice. Please pick 1–5.")

if __name__ == "__main__":
    main()
