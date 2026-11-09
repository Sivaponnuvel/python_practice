# Question 1: Reverse a Number
# Interview Topic: While Loop, Arithmetic Operators
# Write a Python function named reverse_number(n) to reverse a given integer.
# Requirements:
# 1. Create a function named reverse_number(n).
# 2. Reverse the number using a loop.
# 3. Do not convert the number into a string.
# 4. Handle negative numbers while preserving the negative sign.
# 5. Return the reversed number.
# Example 1:
# Input:
# n = 12345
# Expected Output:
# 54321
# Example 2:
# Input:
# n = -456
# Expected Output:
# -654
# Example 3:
# Input:
# n = 1200
# Expected Output:
# 21
# Example 4:
# Input:
# n = 0
# Expected Output:
# 0

def reverse_number(n):
    sign = 1

    if n < 0:
        sign = -1
        n = -n

    reversed_num = 0

    while n > 0:
        digit = n % 10
        reversed_num = reversed_num * 10 + digit
        n = n // 10

    return sign * reversed_num

n = int(input("Enter number: "))
print(reverse_number(n))


