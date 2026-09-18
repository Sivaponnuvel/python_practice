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


