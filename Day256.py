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


# Question 2 – Check Whether a Number Is Armstrong or Not
# Interview Topics: While Loop, Arithmetic Operators, Modulus, Integer Division, Mathematical Logic.
# Given a number, check whether it is an Armstrong number using a while loop.
# An Armstrong number is a number whose sum of each digit raised to the power of the total number of digits is equal to the original number.
# Example:
# 153 has 3 digits.
# \[
# 1^3 + 5^3 + 3^3 = 153
# \]
# Therefore, 153 is an Armstrong number.
# Requirements:
# 1. Get an integer from the user using input().
# 2. Count the total number of digits using a while loop.
# 3. Extract each digit using %.
# 4. Remove the last digit using //.
# 5. Calculate the sum of digits raised to the power of the total number of digits.
# 6. Use a while loop for the calculation.
# 7. Do not convert the number into a string.
# 8. Display whether the number is an Armstrong number or not.
# Expected Output 1:
# Enter a number: 153
# 153 is an Armstrong Number
# Expected Output 2:
# Enter a number: 123
# 123 is Not an Armstrong Number
# Expected Output 3:
# Enter a number: 9474
# 9474 is an Armstrong Number

num = int(input("Enter a number: "))

original = num

count = 0
temp = num

while temp > 0:
    count += 1
    temp //= 10

armstrong = 0

while num > 0:
    digit = num % 10
    armstrong += digit ** count
    num //= 10

if original == armstrong:
    print(f"{original} is an Armstrond Number")
else:
    print(f"{original} is Not an Armstrong Number")