# Question 1 – List Coding Problem
# Topic: Python Lists
# Write a Python program to find the second-largest unique number in a list.
# Example:
# numbers = [10, 20, 4, 45, 99, 99]
# Expected output:
# Second Largest Number: 45
# Requirements:
# 1. Find the second-largest distinct number.
# 2. Don't count duplicate values more than once.
# 3. Don't hardcode the answer.
# 4. Handle the case where a second-largest unique number doesn't exist.

numbers = [10, 20, 4, 45, 99, 99]

unique_list = list(set(numbers))
unique_list.sort()

if len(unique_list) < 2:
    print("Second largest unique number doesn't exist")
else:
    print(f"Second Largest Number: {unique_list[-2]}")


