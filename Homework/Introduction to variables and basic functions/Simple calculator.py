# Simple calculator

# Get operation from user
operation = input('Enter an operation: ').lower()

# Get two numbers from user
variable_1 = int(input('Enter a number 1: '))
vriable_2 = int(input('Enter a number 2: '))

print('Please specify +, -')

# Perform operation based on user input
if operation == '+':
    print(variable_1 + vriable_2)
elif operation == '-':
    print(variable_1 - vriable_2)
    
