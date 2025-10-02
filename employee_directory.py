#second try
# Open the file in read mode
# Loop over each line in the file
# Split line into name and role
# Print the list in an orderly manner.
#Ask the User to Add a New Employee
def sayhi():
    print('Hi there welcome to our employee directory')
def good_bye(): 
    print('Thankyou for visiting our directory come back again!')

sayhi()

with open('employees.txt', 'r') as employee_list:
    for line in employee_list:
        parts = line.strip().split(', ')
        name = parts[0]
        role = parts[1]
        print('Name:', name, '| Role:', role)


decision = input('Would you like to add a member(Y/N):\n').lower()

with open('employees.txt', 'a') as employee_add:
    while True:
        if decision in ['yes', 'y']:
            name = input("Enter employee's name:\n")
            role = input("Enter employee's role:\n")
            employee_add.write(f'\n{name}, {role}')
            add_more = input('Would you like to add another member?\n').lower()
            if add_more in ['yes', 'y']:
                continue
            else:
                good_bye()
                break
        else:
            good_bye()
            break
