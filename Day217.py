# Question 1 – List Coding Problem
# Topic: Lists, Loops and Conditional Statements
# Write a Python program to find the common elements between two lists without duplicates.
# Example:
# list1 = [10, 20, 30, 40, 20, 50]list2 = [20, 40, 60, 20, 70]
# Expected output:
# Common Elements: [20, 40]
# Requirements:
# 1. Create the two lists shown above.
# 2. Find the elements that appear in both lists.
# 3. Include each common element only once.
# 4. Print the common elements as a list.
# Conditions:
# - Use loops and conditional statements.
# - Do not use set().
# - Do not use external libraries.
# - Your solution should work if the list values change.

list1 = [10, 20, 30, 40, 20, 50]
list2 = [20, 40, 60, 20, 70]

common = []

for i in list1:
    if i in list2:
        if i not in common:
            common.append(i)

print(f"Common Elements: {common}")


# Question 2 – Functions and Recursion
# Topic: Recursive Functions
# Write a recursive Python function named sum_of_digits(n) that calculates the sum of all digits in a positive integer.
# Example 1:
# Enter a number: 1234
# Sum of digits: 10
# Explanation: \(1 + 2 + 3 + 4 = 10\)
# Example 2:
# Enter a number: 507
# Sum of digits: 12
# Requirements:
# 1. Get an integer from user input.
# 2. Create a function named sum_of_digits(n).
# 3. Use recursion to calculate the sum of the digits.
# 4. Print the result.
# Conditions:
# - Use recursion, not a loop, to calculate the sum.
# - Do not convert the number into a string.
# - Do not use built-in functions to calculate the digit sum.
# - Assume the input is a non-negative integer.

def sum_of_digits(n):
    if n < 10:
        return n
    
    return n % 10 + sum_of_digits(n // 10)

number = int(input("Enter a number: "))
print(f"Sum of digits: {sum_of_digits(number)}")