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


# Question 2: Find the Sum of Digits of a Number
# Interview Topic: Loops, Arithmetic Operators, Conditional Statements
# Write a Python function named sum_of_digits(n) to calculate the sum of all digits in a given integer.
# Requirements:
# 1. Create a function named sum_of_digits(n).
# 2. Calculate the sum using a loop.
# 3. Do not convert the number into a string.
# 4. Handle negative numbers by considering their absolute value.
# 5. Return the sum of digits.
# Example 1:
# Input:
# n = 12345
# Expected Output:
# 15
# Example 2:
# Input:
# n = 908
# Expected Output:
# 17
# Example 3:
# Input:
# n = -456
# Expected Output:
# 15
# Example 4:
# Input:
# n = 0
# Expected Output:
# 0

def sum_of_digits(n):
    n = abs(n)
    sum_num = 0

    while n > 0:
        digit = n % 10
        sum_num += digit
        n = n // 10

    return sum_num

number = int(input("Enter number: "))
print(sum_of_digits(number))