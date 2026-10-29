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


# 🔹 Question 2 – Generator Coding Problem
# Topic: Functions, Generators, yield and Loops
# Write a Python program to create a generator that produces even numbers from 1 to n.
# Example 1:
# n = 10
# Expected output:
# Even Numbers: 2 4 6 8 10
# Example 2:
# n = 7
# Expected output:
# Even Numbers: 2 4 6
# Example 3:
# n = 1
# Expected output:
# Even Numbers:
# Requirements
# 1. Get an integer n from the user.
# 2. Create a generator function named even_numbers(n).
# 3. Generate even numbers from 1 to n, including n if it is even.
# 4. Use yield to produce each even number.
# 5. Use a for loop to iterate through the generator.
# 6. Display the generated numbers in increasing order.
# 7. If n is less than 2, display only Even Numbers: without any numbers.
# Conditions
# - Must use yield, not return, to produce even numbers.
# - Use loops and conditional statements.
# - Do not create a list to store the generated numbers.
# - Do not import libraries.
# - Do not hardcode the output.
# - Your solution should work for different values of n.

def even_numbers(n):
    for i in range(1, n+1):
        if i % 2 == 0:
            yield i

n = int(input("Enter a number: "))

print("Even Numbers:", end=" ")

if n >= 2:
    for num in even_numbers(n):
        print(num, end=" ")