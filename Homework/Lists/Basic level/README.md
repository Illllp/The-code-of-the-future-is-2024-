### Basic Level

## Task 1: Working with Lists and Slices (Expanded)

**Objective:**

*   Perform additional slicing operations to access and print different parts of the list

**Instructions:**

1.  Follow the instructions from the Beginner Level task 1.

2.  Additionally, print the following:
    *   The first and last elements of the list using slicing.
        ```python
        print(data_list[0], data_list[-1])
        ```

    *   Elements at even indices of the list.
        ```python
        print(data_list[::2])
        ```

    *   Elements at odd indices of the list.
        ```python
        print(data_list[1::2])
        ```

**Explanation:**

*   Slicing with a single index selects a specific element from the list.
*   Slicing with a step value extracts elements at a specified interval.

## Task 2: Working with Conditions and Loops

**Objective:**

*   Introduce conditional statements (`if`, `elif`, `else`) and loops (`for`)
*   Handle user input and check conditions

**Instructions:**

1.  Get an integer input from the user using `user_num = int(input("Enter a number: "))`.
    ```python
    user_num = int(input("Enter a number: "))
    ```

2.  Check if the `user_num` is divisible by 3 using `if user_num % 3 == 0:` and print a message if it is.
    ```python
    if user_num % 3 == 0:
        print("The number is divisible by 3")
    ```

3.  Check if `user_num` is greater than 10 using `elif user_num > 10:` and print a message if it is.
    ```python
    elif user_num > 10:
        print("The number is greater than 10")
    ```

4.  Use `else:` to print a message if the number doesn't meet the previous conditions.
    ```python
    else:
        print("The number does not meet the conditions")
    ```

**Explanation:**

*   The `input()` function takes user input and converts it to an integer using `int()`.
*   The `if`, `elif`, and `else` statements control the program flow based on conditions.
*   The `%` operator checks for divisibility.

**Additional Notes:**

*   These tasks provide a basic foundation for working with lists, slices, conditional statements, and loops in Python.
*   You can expand on these concepts to tackle more complex programming problems.
*   Refer to the Python documentation
