# Sorting numbers

# Entering different numbers
a = int(input('Enter a number: '))
b = int(input('Enter another number: '))
c = int(input('Enter another number: '))

# Writing numbers to a list
numbers = [ a, b, c ]

# Sorting the list of numbers
numbers.sort()

print('Your input numbers are in ascending order:', *numbers)