# Question 1 – Sum of Digits
# Interview Topics: While Loop, Modulus Operator (%), Floor Division (//), Variables.
# Write a Python program to calculate the sum of digits of a given number.
# Requirements:
# 1. Get an integer from the user using input().
# 2. Calculate the sum of all digits in the number.
# 3. Use a while loop.
# 4. Use the modulus (%) and floor division (//) operators.
# 5. Display the final sum.
# Expected Output:
# Enter a number: 12345
# Sum of digits: 15

number = int(input("Enter a number: "))

sum_number = 0

while number > 0:
    digit = number % 10
    sum_number += digit
    number //= 10

print(f"Sum of digits: {sum_number}")

