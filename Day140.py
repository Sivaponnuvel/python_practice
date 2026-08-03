# 🔹 Question 1 – Exception Handling: Safe Division
# Write a Python program to perform division of two numbers using exception handling.
# Program Flow
# Take two integers from the user.
# Divide the first number by the second number.
# Display the result.
# If the user enters 0 as the second number, display:
# Cannot Divide by Zero ❌
# If the user enters an invalid value (non-integer), display:
# Invalid Input ❌
# Example 1
# Input
# Enter First Number: 20
# Enter Second Number: 4
# Output
# Result: 5.0
# Example 2
# Input
# Enter First Number: 20
# Enter Second Number: 0
# Output
# Cannot Divide by Zero ❌
# ⚠️ Conditions
# ✅ Take input from the user
# ✅ Use try
# ✅ Use except
# ✅ Handle ZeroDivisionError
# ✅ Handle ValueError
# ❌ Don't use if second_number == 0
# ❌ Don't import any libraries

try:
    num1 = int(input("Enter First Number: "))
    num2 = int(input("Enter Second Number: "))
    print(f"Result: {num1 / num2}")
except ZeroDivisionError:
    print("Cannot Divide by Zero ❌")
except ValueError:
    print("Invalid Input ❌")


