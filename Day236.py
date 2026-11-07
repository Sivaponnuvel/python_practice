# Question 1: Find the Factorial of a Number
# Interview Topic: Functions, Loops, Conditional Statements
# Write a Python function named factorial(n) to calculate the factorial of a given number.
# Requirements:
# 1. Create a function named factorial(n).
# 2. Calculate factorial using a loop.
# 3. Do not use math.factorial().
# 4. If the input is 0, return 1.
# 5. If the input is negative, return "Invalid input".
# Example 1:
# Input:
# n = 5
# Expected Output:
# 120
# Example 2:
# Input:
# n = 0
# Expected Output:
# 1
# Example 3:
# Input:
# n = -3
# Expected Output:
# Invalid input

def factorial(n):
    if n < 0:
        return "Invalid input"
    
    fact = 1

    for i in range(1, n + 1):
        fact *= i
    
    return fact

n = int(input("Enter number: "))
print(factorial(n))


