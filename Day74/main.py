# 🔹 Question 1 – File Compare System
# Write a Python program to:
# 👉 Create 2 text files:
# file1.txt
# file2.txt
# 👉 Write some content inside both files manually
# 👉 Read both files
# 👉 Compare contents line by line
# 👉 Print:
# If lines are same:
# Line 1: Same ✅
# If lines are different:
# Line 2: Different ❌
# Example Output:
# Line 1: Same ✅
# Line 2: Different ❌
# Line 3: Same ✅
# ⚠️ Conditions:
# ✅ Use file handling
# ✅ Use loops
# ❌ Do not use external libraries

with open("D:/Python/Own try/practice/Day74/file1.txt")as file:
    file1 = file.readlines()
with open("D:/Python/Own try/practice/Day74/file2.txt")as file:
    file2 = file.readlines()
for i in range(len(file1)):
    if file1[i].strip() == file2[i].strip():
        print(f"Line {i+1}: Same ✅")
    else:
        print(f"Line {i+1}: Different ❌")


# 🔹 Question 2 – Exception Handling Calculator
# Write a Python program to:
# 👉 Create a calculator using functions:
# add(a, b)
# subtract(a, b)
# multiply(a, b)
# divide(a, b)
# 👉 Take:
# operation from user
# two numbers
# 👉 Handle exceptions:
# If user enters invalid number:
# Invalid Number ❌
# If user divides by zero:
# Cannot divide by zero ❌
# If user enters invalid operation:
# Invalid Operation ❌
# Example Output:
# Choose Operation: /
# Enter a: 10
# Enter b: 2
# Result: 5.0
# OR
# Choose Operation: /
# Enter a: 10
# Enter b: 0
# Cannot divide by zero ❌

def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    return a/ b

try:
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    operation = input("Choose Operation(+,-,*,/): ")
    if operation == "+":
        print(f"Addition: {add(a, b)}")
    elif operation == "-":
        print(f"Subtraction: {subtract(a, b)}")
    elif operation == "*":
        print(f"Multiplication: {multiply(a, b)}")
    elif operation == "/":
        print(f"Division: {divide(a, b)}")
    else:
        print("Invalid Operation ❌")
except ValueError:
    print("Invalid Number ❌")
except ZeroDivisionError:
    print("Cannot divide by zero ❌")