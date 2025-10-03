import string
import random

def goodbye(name):
    print(f"Thanks for using the password generator, {name}! Come again!")

def password_generator():
    name = input("What is your name?\n")
    print(f"\nHello {name}, welcome to the Password Generator!")
    print('Type "quit" in any prompt to exit.\n')

    while True:
        include_lower = input("Include lowercase letters? (Y/N): ").lower()
        include_upper = input("Include uppercase letters? (Y/N): ").lower()
        include_digits = input("Include digits? (Y/N): ").lower()
        include_symbols = input("Include punctuation/symbols? (Y/N): ").lower()

        chars = ""
        if include_lower in ['y', 'yes']:
            chars += string.ascii_lowercase
        if include_upper in ['y', 'yes']:
            chars += string.ascii_uppercase
        if include_digits in ['y', 'yes']:
            chars += string.digits
        if include_symbols in ['y', 'yes']:
            chars += string.punctuation

        if not chars:
            print("⚠️ You must select at least one character type!")
            continue

        length_input = input("\nHow long do you want your password to be? (number): ").lower()
        if length_input == "quit":
            goodbye(name)
            break

        try:
            length = int(length_input)
            if length < 1:
                print("Password length must be at least 1.")
                continue
        except ValueError:
            print("Invalid input! Please enter a number or 'quit'.")
            continue

        password = ''.join(random.choice(chars) for _ in range(length))
        print(f"\n✅ Here is your password:\n{password}")

        again = input("\nGenerate another password? (Y/N): ").lower()
        if again not in ['y', 'yes']:
            goodbye(name)
            break

password_generator()


