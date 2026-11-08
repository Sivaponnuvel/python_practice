# Question 1: Check Whether a Number Is Prime
# Interview Topic: Loops, Conditional Statements, Functions
# Write a Python function named is_prime(n) to check whether a given number is prime or not.
# Requirements:
# 1. Create a function named is_prime(n).
# 2. A prime number must be greater than 1.
# 3. A prime number should be divisible only by 1 and itself.
# 4. Return True if the number is prime.
# 5. Otherwise, return False.
# 6. Do not use external libraries.
# Example 1:
# Input:
# n = 7
# Expected Output:
# True
# Example 2:
# Input:
# n = 10
# Expected Output:
# False
# Example 3:
# Input:
# n = 1
# Expected Output:
# False

def is_prime(n):
    if n <= 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False
        
    return True

n = int(input("Enter number: "))
print(is_prime(n))


