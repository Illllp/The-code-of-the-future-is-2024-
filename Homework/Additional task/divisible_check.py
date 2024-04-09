# Write a Python program to check whether two given integers are coprime or not.

# Entering 2 numbers
a = int(input('Enter the first number: '))
b = int(input('Enter the second number: '))


# Checking if they are coprime or not
if a % b == 0 or b % a == 0:
    print("SHARES")
else:
    print("NOT SHARED")
