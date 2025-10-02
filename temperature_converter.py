#Temperature Converter

def goodbye(name):
    print(f"Thank you for using my Temperature Converter, {name}! Come again soon!")    

def temp_converter(name):
    print(f'Hi there, {name}, welcome to our Temperature Converter')

    while True:
        decision = input('Would you like to convert to Fahrenheit or Celsius?\n').lower()
        
        # Allow multiple variations
        if decision in ['fahrenheit', 'f', 'fa']:
            temp_c = input('Enter a temperature in Celsius:\n')
            try:
                temp_c = float(temp_c)
                F = (temp_c * 9/5) + 32
                print(f'{temp_c}°C = {F:.2f}°F')
            except ValueError:
                print('Invalid input! Numbers only.')
                continue

        elif decision in ['celsius', 'c', 'ce']:
            temp_f = input('Enter a temperature in Fahrenheit:\n')
            try:
                temp_f = float(temp_f)
                C = (temp_f - 32) * 5/9
                print(f'{temp_f}°F = {C:.2f}°C')
            except ValueError:
                print('Invalid input! Numbers only.')
                continue

        else:
            print("Invalid choice! Please type 'Celsius' or 'Fahrenheit'.")
            continue

        convert_another = input('Would you like to convert another temperature (Y/N)?\n').lower()
        if convert_another not in ['yes', 'y']:
            goodbye(name)
            break


player_name = input("Hi! What's your name?\n")
temp_converter(player_name)
