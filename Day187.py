# 🔹 Question 1 – Factorial of a Number
# Write a Python program to find the factorial of a given number.
# Example Input:
# Enter a number: 5
# Expected Output:
# Factorial of 5: 120
# Because:
# 5 × 4 × 3 × 2 × 1 = 120
# Conditions:
# Get a number from the user.
# Create a function factorial().
# Use a loop to calculate the factorial.
# Do not use math.factorial().
# Handle 0 correctly.
# Example:
# Enter a number: 0
# Expected:
# Factorial of 0: 1

def factorial(number):
    fact = 1
    for i in range(1, number + 1):
        fact *= i
    return fact

number = int(input("Enter a number: "))
print(f"Factorial of {number}: {factorial(number)}")


# 🔹 Question 2 – Factorial of Each Digit
# Write a Python program to find the factorial of each digit in a given number.
# Example Input:
# Enter a number: 234
# Expected Output:
# Factorial of 2: 2
# Factorial of 3: 6
# Factorial of 4: 24
# Conditions:
# Get a number from the user.
# Process each digit separately.
# Create a function factorial() to calculate the factorial of a digit.
# Use a loop to calculate the factorial.
# Do not use math.factorial().
# Do not treat 234 as one number for factorial.
# Another Example:
# Enter a number: 521
# Expected:
# Factorial of 5: 120
# Factorial of 2: 2
# Factorial of 1: 1

def fact(num):
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    return fact

num = input("Enter a number: ")

for i in num:
    a = int(i)
    print(f"Factorial of {a}: {fact(a)}")