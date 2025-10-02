# Project Title: Simple Day 1 Calculator
# Purpose: Practice Python
# Author: Nehemiah
# Created: 29/09/2025

# Step 0: Define a reusable exit message function and variables
name = input('What is your name?\n')

def sayhi():
    print('Hi there,',name+', welcome to Simple Calculater.')

def goodbye():
        print('Thankyou for using my simple calculator,',name+', see you soon!')

print('\nHello', name+ ', welcome to Simple Calculator')
print("Type 'quit' in any of the prompts to exit.")
    
# Step 1: Controlled Loop
while True:
    
    # Step 2: Get numbers
    num1 = input('Enter first number: ')
    if num1.lower() == 'quit':
        goodbye()
        break
    num2 = input('Enter second number: ')
    if num2.lower() == 'quit':
        goodbye()
        break

    #Step 3: Convert safely to float

    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        print('Invalid input! Please enter numbers only.')
        continue
    #Step 4: Collect Operation
    
    op = input('Please select one of the following operations:+, -, *, /, **:\n')
    if op.lower() == 'quit':
        goodbye()
        break

    #Step 5: Perform Calculation
    if op == '+':
        result = (num1 + num2)
    elif op == '-':
        result = (num1 - num2)
    elif op == '*':
        result = (num1 * num2)
    elif op == '/':
        if num2 != 0:
            result = (num1 / num2)
        else:
            print("Error can't divide by zero!")
            continue
    elif op == '**':
        result = (num1 ** num2)
    elif op == '//':
        result = (num1 // num2)
    else:
        print('Invalid operator')
        continue
        
    #Step 6: Provide Result
    print(f"{num1} {op} {num2} = {round(result, 2)}")

    # Step 7: Ask user if they want to continue
    decision = input('Would you like to continue (yes/no): ').lower()

    if decision == 'yes' or decision == 'y':
        continue
    elif decision == 'no' or decision == 'n':
        goodbye()
        break
    else:
        print('Invalid input, exiting calculator.')
        goodbye()
        break

    
    