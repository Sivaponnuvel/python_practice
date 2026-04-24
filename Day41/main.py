# 🔹 Question 1
# Write a Python program to:
# 👉 Create a module named mymath.py
# 👉 Inside the module, create functions:
# add(a, b)
# subtract(a, b)
# multiply(a, b)
# 👉 In another file (main.py):
# Import the module
# Take two numbers from user
# Call all functions
# Print results
# 🧠 Example Output:
# Addition: 10
# Subtraction: 2
# Multiplication: 24

import mymath as m
try:
    number1 = int(input("Enter the 1st number: "))
    number2 = int(input("Enter the 2nd number: "))
except ValueError:
    print("Invalid input ❌")
else:
    print(f"Addition: {m.add(number1,number2)}")
    print(f"Subtraction: {m.subtract(number1,number2)}")
    print(f"Multiplication: {m.multiply(number1,number2)}")
    print(f"Division: {m.divide(number1,number2)}")


