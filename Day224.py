# 🔹 Question 1 – List Coding Problem
# Topic: Lists, Loops and Conditional Statements
# Write a Python program to rotate a list to the right by k positions.
# Example 1:
# nums = [1, 2, 3, 4, 5]k = 2
# Expected output:
# Rotated List: [4, 5, 1, 2, 3]
# Example 2:
# nums = [10, 20, 30, 40]k = 1
# Expected output:
# Rotated List: [40, 10, 20, 30]
# Requirements
# 1. Get a list of integers from the user.
# 2. Get the rotation count k from the user.
# 3. Rotate the list to the right by k positions.
# 4. If k is greater than the list length, handle it correctly.
# 5. Display the rotated list.
# 6. Handle an empty list without errors.
# Conditions
# - Use loops and conditional statements.
# - Do not use sort() or sorted().
# - Do not use external libraries.
# - Do not hardcode the output.
# - Do not use built-in rotation functions.
# - You may use list slicing.

nums = list(map(int, input("Enter a numbers: ").split()))
k = int(input("Enter Rotation count: "))

if len(nums) == 0:
    print("Rotated List: []")

else:
    k %= len(nums)
    roated_list = nums[-k:] + nums[:-k]
    print(f"Rotated List: {roated_list}")


