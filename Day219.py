# 🔹 Question 1 – List Coding Problem
# Topic: Lists, Loops and Conditional Statements
# Write a Python program to find the missing number in a list containing distinct numbers from 1 to n.
# Example:
# nums = [1, 2, 4, 5, 6]n = 6
# Expected output:
# Missing Number: 3
# Requirements:
# 1. Get the list of numbers and n from the user.
# 2. Find the number missing from the range 1 to n.
# 3. Display the missing number.
# 4. Your program should work for different input lists.
# Conditions:
# - Use a loop and conditional statements.
# - Do not use external libraries.
# - Do not hardcode the missing number.
# - Do not use sorting.
# - Do not use the mathematical sum formula \(n(n+1)/2\).

n = int(input("Enter the value of n: "))

nums = []
print("Enter the numbers:")

for i in range(n - 1):
    num = int(input())
    nums.append(num)

missing_number = 0

for number in range(1, n + 1):
    if number not in nums:
        missing_number = number
        break

print("Missing Number:", missing_number)


