# Question 1 – Handle ZeroDivisionError
# Interview Topics: try, except, else, finally, ZeroDivisionError.
# Write a Python program to divide two numbers using exception handling.
# Requirements:
# 1. Get two numbers from the user using input().
# 2. Convert both values into integers.
# 3. Use a try block to perform division.
# 4. Handle ZeroDivisionError using except.
# 5. If division is successful, display the result using else.
# 6. Use finally to display "Program execution completed.".
# Sample Input 1:
# Enter first number: 20
# Enter second number: 5
# Expected Output 1:
# Division Result: 4.0
# Program execution completed.
# Sample Input 2:
# Enter first number: 20
# Enter second number: 0
# Expected Output 2:
# Error: Cannot divide by zero.
# Program execution completed.

try:
    number1 = int(input("Enter first number: "))
    number2 = int(input("Enter second number: "))

    result = number1 / number2

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

else:
    print(f"Division Result: {result}")

finally:
    print("Program execution completed.")


