# 🔹 Question 1 – List Coding Problem
# Topic: Lists, Loops and Conditional Statements
# Write a Python program to find all duplicate elements in a list without using a set.
# Example:
# nums = [10, 20, 30, 20, 40, 10, 50, 20]
# Expected output:
# Duplicate Elements: [10, 20]
# Requirements:
# 1. Get a list of integers from the user.
# 2. Find all elements that appear more than once.
# 3. Display each duplicate element only once.
# 4. Preserve the order in which each duplicate first appears in the original list.
# Conditions:
# - Use loops and conditional statements.
# - Do not use set() or set operations.
# - Do not use count().
# - Do not use sorting.
# - Do not import libraries.
# - Do not hardcode the output.
# Example 2:
# nums = [1, 2, 3, 4]
# Expected output:
# Duplicate Elements: []

nums = list(map(int, input("Enter a numbers: ").split()))

duplicates = []

for i in range(len(nums)):
    found = False

    for j in range(i + 1, len(nums)):
        if nums[i] == nums[j]:
            found = True
            break

    if found and nums[i] not in duplicates:
        duplicates.append(nums[i])

print(f"Duplicate Elements: {duplicates}")


