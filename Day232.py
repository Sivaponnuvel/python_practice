# 🔹 Question 1 – Find Duplicate Elements in a List
# Topic: Lists, Sets, Dictionaries and Loops
# Write a Python program to find all duplicate elements in a list and display each duplicate only once, preserving the order in which duplicates are first detected.
# Example 1
# Input:
# numbers = [10, 20, 30, 20, 40, 10, 50, 30, 20]
# Expected output:
# Duplicate Elements: [20, 10, 30]
# Example 2
# Input:
# numbers = [1, 2, 3, 4, 5]
# Expected output:
# Duplicate Elements: []
# Requirements
# 1. Get a list of integers from the user.
# 2. Identify elements that appear more than once.
# 3. Include each duplicate only once in the result.
# 4. Preserve the order in which duplicates are first detected.
# 5. Display an empty list if there are no duplicates.
# 6. Your solution must work for different input lists.
# Conditions
# - Use Python lists and loops.
# - Do not use collections.Counter.
# - Do not use numbers.count() to identify duplicates.
# - Do not sort the input list.
# - Do not hardcode the output.

numbers = list(map(int, input("Enter numbers: ").split()))

duplicates = []

for i in range(len(numbers)):
    found = False

    for j in range(i + 1, len(numbers)):
        if numbers[i] == numbers[j]:
            found = True
            break

    if found and numbers[i] not in duplicates:
        duplicates.append(numbers[i])

print(f"Duplicate Elements: {duplicates}")


