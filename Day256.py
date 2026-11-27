# Question 1 – Reverse a Number Using While Loop
# Interview Topics: While Loop, Arithmetic Operators, Modulus, Integer Division, Conditional Statements.
# Given an integer, reverse its digits using a while loop.
# Requirements:
# 1. Get an integer from the user using input().
# 2. Reverse the given number using a while loop.
# 3. Use arithmetic operators (% and //).
# 4. Do not convert the number into a string.
# 5. Do not use built-in reverse functions.
# 6. Display the reversed number.
# Expected Output 1:
# Enter a number: 12345
# Reversed Number: 54321
# Expected Output 2:
# Enter a number: 9080
# Reversed Number: 809

number = int(input("Enter a number: "))

rev = 0

while number > 0:
    digit = number % 10
    rev = rev * 10 + digit
    number //= 10

print(f"Reversed Number: {rev}")


