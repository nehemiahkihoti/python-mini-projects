import math

def goodbye(name):
    print(f"Thank you for using my Complicated Calculator, {name}! Come again soon!")

def math_exercise(name):
    print(f'Hi there, {name}, welcome to my complicated calculator.')

    while True:
        function = input('Which function would you like to use? (sqrt / log10 / sin)\n').lower()
        
        if function in ['sqrt', 'square root', 'root']:
            while True:
                num = input('Enter a positive number:\n')
                try:
                    num = float(num)
                    if num <= 0:
                        print("Number must be positive!")
                        continue
                    print(f'The square root of {num} is {round(math.sqrt(num), 3)}')
                    break
                except ValueError:
                    print('Invalid input! Numbers only.')
        
        elif function in ['log', 'log10', 'log base 10']:
            while True:
                num = input('Enter a positive number:\n')
                try:
                    num = float(num)
                    if num <= 0:
                        print("Number must be positive!")
                        continue
                    print(f'The log base 10 of {num} is {round(math.log10(num), 3)}')
                    break
                except ValueError:
                    print('Invalid input! Numbers only.')
        
        elif function in ['sine', 'sin']:
            while True:
                num = input('Enter a number:\n')
                try:
                    num = float(num)
                    print(f'The sine of {num} is {round(math.sin(num), 3)}')
                    break
                except ValueError:
                    print('Invalid input! Numbers only.')
        
        else:
            print("Invalid function choice! Please choose sqrt, log10, or sin.")
            continue
        
        another = input('Would you like to complicate another number? (Y/N)\n').lower()
        if another not in ['yes', 'y']:
            goodbye(name)
            break

user_name = input('Hello, what is your name?\n')
math_exercise(user_name)
