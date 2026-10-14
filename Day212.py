# 🟢 Question 1 – Recursion
# Topic: Recursive functions
# Create a recursive function called factorial(n) that calculates the factorial of a positive integer.
# The factorial is calculated as:
# \[
# n! = n \times (n-1) \times \cdots \times 1
# \]
# For example, \(5! = 5 \times 4 \times 3 \times 2 \times 1 = 120\).
# Requirements:
# 1. Define a function named factorial(n).
# 2. Use recursion to calculate the factorial.
# 3. Include a base case to stop the recursion.
# 4. Get an integer from the user.
# 5. Print the factorial result.
# 6. Handle negative input by printing Factorial is not defined for negative numbers.
# Example input:
# Enter a number: 5
# Expected output:
# Factorial of 5: 120
# For negative input:
# Enter a number: -3
# Factorial is not defined for negative numbers.
# Rules:
# - Use recursion; do not use loops to calculate the factorial.
# - Do not use external libraries.
# - Remember that 0! = 1.

def factorial(n):
    if n == 0  or n == 1:
        return 1

    return n * factorial(n - 1)

num = int(input("Enter a number: "))

if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    print(f"Factorial of {num}: {factorial(num)}")


