# 🔹 Question 1 – Recursion Coding Problem
# Topic: Functions, Recursion and Conditional Statements
# Write a Python program to find the Greatest Common Divisor (GCD) of two positive integers using recursion.
# The GCD is the largest positive integer that divides both numbers without leaving a remainder.
# Example 1:
# a = 48b = 18
# Expected output:
# GCD: 6
# Example 2:
# a = 25b = 15
# Expected output:
# GCD: 5
# Example 3:
# a = 17b = 13
# Expected output:
# GCD: 1
# Requirements
# 1. Get two integers from the user.
# 2. Create a recursive function named find_gcd(a, b).
# 3. Calculate the GCD using recursion.
# 4. Return the GCD from the function.
# 5. Display the final result.
# 6. Handle invalid inputs where either number is zero or negative by displaying Invalid input.
# Conditions
# - Use recursion.
# - Use conditional statements.
# - Do not use math.gcd().
# - Do not use loops inside the recursive function.
# - Do not import libraries.
# - Do not hardcode the output.
# - Your solution should work for different positive integers.

def find_gcd(a, b):
    if b == 0:
        return a

    return find_gcd(b, a % b)

a  = int(input("Enter first positive number: "))
b  = int(input("Enter second positive number: "))

if a <= 0 or b <= 0:
    print("Invalid input")

else:
    print(f"GCD: {find_gcd(a, b)}")


