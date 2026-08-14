# 🔹 Question 1 – Exception Handling: Safe Integer List
# Write a Python program to take 5 integers from the user and store them in a list.
# Program Flow
# Use a try block to take the input.
# Convert each input into an integer.
# Store the numbers in a list.
# If the user enters a non-integer value, handle the exception.
# Display:
# Numbers: [10, 20, 30, 40, 50]
# If invalid input is entered:
# Invalid Input ❌
# Please enter integers only.
# Example
# Input:
# Enter Number 1: 10
# Enter Number 2: 20
# Enter Number 3: abc
# Output:
# Invalid Input ❌
# Please enter integers only.
# ⚠️ Conditions
# ✅ Use try
# ✅ Use except ValueError
# ✅ Use a loop
# ✅ Use a list
# ✅ Take input from the user
# ❌ Don't check using isdigit()
# ❌ Don't import any libraries

numbers = []

try:
    for i in range(5):
        number = int(input(f"Enter Number {i+1}: "))
        numbers.append(number)
    print(f"Numbers: {numbers}")

except ValueError:
    print("Invalid Input ❌")
    print("Please enter integers only.")


