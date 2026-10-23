# 🔹 Question 1 – List Coding Problem
# Topic: Lists, Loops and Conditional Statements
# Write a Python program to find the second-largest unique number in a list without using sorting.
# Example:
# nums = [10, 5, 20, 8, 20, 15]
# Expected output:
# Second Largest: 15
# Requirements:
# 1. Get a list of integers from the user.
# 2. Find the second-largest unique number.
# 3. Display the result.
# 4. Handle the case where a second-largest unique number does not exist.
# Conditions:
# - Use loops and conditional statements.
# - Do not use sort() or sorted().
# - Do not use max() or min().
# - Do not import libraries.
# - Do not hardcode the answer.
# - Duplicate values must not be treated as separate unique numbers.
# Example 2:
# nums = [7, 7, 3]
# Expected output:
# Second Largest: 3
# Example 3:
# nums = [5, 5, 5]
# Expected output:
# No second-largest unique number

nums = list(map(int, input("Enter numbers: ").split()))

largest = None
second_largest = None

for i in nums:
    if largest is None or i > largest:
        if i != largest:
            second_largest = largest
            largest = i

    elif i != largest and (second_largest is None or i > second_largest):
        second_largest = i

if second_largest is not None:
    print(f"Second Largest: {second_largest}")
else:
    print("No second-largest unique number")


