# 🔹 Question 1 – List Coding Problem
# Topic: Lists, Loops and Conditional Statements
# Write a Python program to move all zeros to the end of a list while maintaining the original order of non-zero elements.
# Example:
# nums = [0, 1, 0, 3, 12]
# Expected output:
# Updated List: [1, 3, 12, 0, 0]
# Another example:
# nums = [4, 0, 5, 0, 2, 0, 8]
# Expected output:
# Updated List: [4, 5, 2, 8, 0, 0, 0]
# Requirements
# 1. Get a list of integers from the user.
# 2. Move all zeros to the end of the list.
# 3. Maintain the original order of non-zero elements.
# 4. Display the updated list.
# 5. Your program should work for different input lists.
# Conditions
# - Use loops and conditional statements.
# - Do not use sort() or sorted().
# - Do not use remove() or pop().
# - Do not import libraries.
# - Do not hardcode the output.
# - Do not create a separate list; modify the original list.

nums = list(map(int, input("Enter numbers: ").split()))

position = 0

for i in range(len(nums)):
    if nums[i] != 0:
        nums[position], nums[i] = nums[i], nums[position]
        position += 1

print(f"Updated List: {nums}")


