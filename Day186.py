# 🔹 Question 1 – Find the Second Largest Number
# Write a Python program to find the second largest unique number in a list.
# Example Input:
# Enter numbers: 10 25 8 40 25 30
# Expected Output:
# Second largest number: 30
# Conditions:
# Get numbers from the user.
# Duplicate values should be considered only once.
# Find the second largest unique number.
# Do not use set().
# Do not use sort() or sorted().
# Handle the case where there is no second largest unique number.
# Example:
# Enter numbers: 10 10 5
# Expected:
# Second largest number: 5

numbers = list(map(int, input("Enter numbers: ").split()))

largest = numbers[0]
for i in numbers:
    if i > largest:
        largest = i
second = None
for i in numbers:
    if i != largest:
        if second is None or i > second:
            second = i
print(f"Second largest number: {second}")


# 🔹 Question 2 – Exception Handling
# Create a Python program for a simple division calculator.
# The user should enter two numbers and the program should divide the first number by the second number.
# Example Input:
# Enter first number: 20
# Enter second number: 5
# Expected Output:
# Result: 4.0
# Conditions:
# Use try and except.
# Handle division by zero.
# Handle invalid input such as entering "abc" instead of a number.
# Display user-friendly error messages.
# The program should not crash when an exception occurs.
# Example 2:
# Enter first number: 20
# Enter second number: 0
# Expected:
# Cannot divide by zero ❌
# Example 3:
# Enter first number: abc
# Expected:
# Invalid input ❌
# Please enter numbers only.

try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    divided = num1 / num2

    print(f"Result: {divided}")

except ValueError:
    print("Invalid input ❌")
    print("Please enter numbers only.")

except ZeroDivisionError:
    print("Cannot divide by zero ❌")