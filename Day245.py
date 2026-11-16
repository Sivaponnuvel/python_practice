# Question 1 – Print Numbers from 1 to N Using While Loop
# Interview Topics: while loop, input(), Type Conversion, Increment.
# Write a Python program to print all numbers from 1 to N using a while loop.
# Input:
# Enter a number: 10
# Expected Output:
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# Conditions:
# 1. Get the number from the user using input().
# 2. Convert the input into an integer.
# 3. Use a while loop.
# 4. Print numbers starting from 1 up to N.
# 5. Do not use a for loop.

n = int(input("Enter a number: "))
i = 1

while n >= i:
    print(i)
    i += 1


# Question 2 – Calculate the Sum of Digits Using While Loop
# Interview Topics: while loop, Modulus %, Floor Division //, Variables.
# Write a Python program to calculate the sum of all digits in a given number using a while loop.
# Input:
# Enter a number: 12345
# Expected Output:
# Sum of digits: 15
# Explanation:
# 1+2+3+4+5=15
# Conditions:
# 1. Get the number from the user using input().
# 2. Convert the input into an integer.
# 3. Use a while loop to extract each digit.
# 4. Use % and // operators.
# 5. Calculate and print the sum of digits.
# 6. Do not convert the number into a string.

number = int(input("Enter a number: "))
sum_digit = 0

while number > 0:
    sum_digit += number % 10
    number //= 10

print(f"Sum of digits: {sum_digit}")