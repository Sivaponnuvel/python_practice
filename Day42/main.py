# 🔹 Question 1
# Write a Python program to:
# 👉 Create a folder named mypackage
# 👉 Inside the folder, create:
# __init__.py
# mymath.py
# 👉 In mymath.py, create functions:
# add(a, b)
# subtract(a, b)
# 👉 In another file (main.py):
# Import the package
# Call both functions
# Take input from user
# Print results
# 🧠 Example Output:
# Addition: 15
# Subtraction: 5

from mypackage import mymath
try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
except ValueError:
    print("Invalid input ❌")
else:
    print(f"Addition: {mymath.add(num1,num2)}")
    print(f"Subtraction: {mymath.subtract(num1,num2)}")


