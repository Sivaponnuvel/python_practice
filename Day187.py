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


