# Get a number from the user
user_num = int(input("Enter a number: "))

# Check if the number is divisible by 3
if user_num % 3 == 0:
    print("The number is divisible by 3")

# Check if the number is greater than 10
elif user_num > 10:
    print("The number is greater than 10")

# Otherwise
else:
    print("The number does not meet the conditions")
