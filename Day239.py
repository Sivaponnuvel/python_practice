# Question 1: Check Whether a Number Is an Armstrong Number
# Interview Topics: While Loop, Arithmetic Operators, Conditional Statements
# Write a Python function named is_armstrong(n) to check whether a given number is an Armstrong number.
# Requirements:
# 1. Create a function named is_armstrong(n).
# 2. Check whether the given number is an Armstrong number using a loop.
# 3. Do not convert the number into a string.
# 4. Return True if it is an Armstrong number; otherwise, return False.
# 5. Handle zero correctly.
# Examples:
# Input: 153Output: True
# Explanation: \(1^3 + 5^3 + 3^3 = 153\)
# Input: 123Output: FalseInput: 9474Output: TrueInput: 0Output: True

def is_armstrong(n):
    if n < 0:
        return False
    if n == 0:
        return True

    temp = n
    k = 0
    while temp > 0:
        k += 1
        temp //= 10

    temp = n
    total_sum = 0
    while temp > 0:
        digit = temp % 10
        total_sum += digit ** k
        temp //= 10

    return total_sum == n

n = int(input("Enter number: "))
print(is_armstrong(n))


