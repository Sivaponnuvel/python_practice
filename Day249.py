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


# Question 2 – Prime Number
# Interview Topics: For Loop, Conditional Statements, Modulus Operator, Boolean Variables.
# Write a Python program to check whether a given number is a prime number or not.
# Requirements:
# 1. Get an integer from the user using input().
# 2. Check whether the number is prime or not.
# 3. A prime number must be greater than 1.
# 4. Use a for loop and conditional statements.
# 5. Display the appropriate result.
# Expected Output 1:
# Enter a number: 7
# 7 is a Prime Number
# Expected Output 2:
# Enter a number: 10
# 10 is Not a Prime Number

def is_prime(num):
    if num <= 1:
        return f"{num} is Not a Prime Number"

    for i in range(2, num):
        if num % i == 0:
            return f"{num} is Not a Prime Number"
    
    return f"{num} is a Prime Number"

num = int(input("Enter a number: "))

print(is_prime(num))