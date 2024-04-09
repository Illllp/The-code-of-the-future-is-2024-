# Checking the age condition in the store to issue a discount or a delicious chocolate bar

# Entering the user's age
age = int(input('Enter your age: '))

# Checking if the age is negative
if age < 0:
    raise ValueError("The age value is incorrect. It must be non-negative.")

# Calculating the discount
discount = None
chocolate = False

# Checking if the user's age is less than...
if age < 18 and age % 3 == 0:
    discount = 50
elif age > 18 and age % 5 == 0:
    discount = 25
elif age > 50 or age % 12 == 0:
    chocolate = True
else:
    discount = 10

# Displaying the discount if it is not None, otherwise printing "Free chocolate"
if discount is not None:
    print(f'Discond: {discount}%')
elif chocolate:
    print('Free chocolate')
else:
    print("Пупупупупупу, заварю Ка кОфейку")