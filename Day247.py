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


# Question 2 – Handle Multiple Exceptions
# Interview Topics: Multiple except blocks, ValueError, ZeroDivisionError, try, finally.
# Write a Python program to divide two numbers and handle multiple exceptions.
# Requirements:
# 1. Get two values from the user using input().
# 2. Convert both values into integers inside the try block.
# 3. Perform division.
# 4. Handle ValueError if the user enters invalid input.
# 5. Handle ZeroDivisionError if the second number is zero.
# 6. Display the division result if successful.
# 7. Use finally to display "Calculation process finished.".
# Sample Input 1:
# Enter first number: abc
# Enter second number: 5
# Expected Output 1:
# Error: Please enter valid numbers.
# Calculation process finished.
# Sample Input 2:
# Enter first number: 50
# Enter second number: 0
# Expected Output 2:
# Error: Cannot divide by zero.
# Calculation process finished.
# Sample Input 3:
# Enter first number: 50
# Enter second number: 10
# Expected Output 3:
# Division Result: 5.0
# Calculation process finished.

try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    output = num1 / num2

except ValueError:
    print("Error: Please enter valid numbers.")

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

else:
    print(f"Division Result: {output}")

finally:
    print("Calculation process finished.")