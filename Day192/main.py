# 🔹 Question 1 – File Handling: Read and Count Lines
# Create a Python program that creates a file named:
# students.txt
# Write the following student names into the file:
# Arun
# Bala
# Kumar
# Siva
# Then read the file and count how many students are present.
# Expected Output
# Student List:
# Arun
# Bala
# Kumar
# Siva
# Total Students: 4
# ⚠️ Conditions
# ✅ Use open()
# ✅ Use file write mode
# ✅ Write the student names into the file
# ✅ Read the file using read mode
# ✅ Count the number of students
# ✅ Use with open()
# ❌ Don't use libraries
# ❌ Don't hardcode the final count 4
# ❌ Don't use a predefined list to calculate the count
# 💡 Interview focus: File opening modes, write(), readlines() and with open().

filename = "D:/Backend/Python/Own try/python_practice/Day192/students.txt"

with open(filename, "w") as file:
    file.write("Arun\n")
    file.write("Bala\n")
    file.write("Kumar\n")
    file.write("Siva\n")

with open(filename)as file:
    print("Student List:")
    print(file.read())

with open(filename)as file:
    print(f"Total Students: {len(file.readlines())}")


# 🔹 Question 2 – Modules: Create and Import a Module
# Create a Python module named:
# calculator.py
# Inside calculator.py, create two functions:
# add(a, b)
# multiply(a, b)
# The functions should return the addition and multiplication results.
# Then create another Python file named:
# main.py
# Import the calculator module and take two numbers from the user.
# Input
# Enter first number: 10
# Enter second number: 5
# Expected Output
# Addition: 15
# Multiplication: 50
# ⚠️ Conditions
# ✅ Create a separate calculator.py module
# ✅ Create add() function
# ✅ Create multiply() function
# ✅ Use import calculator
# ✅ Take values using input()
# ✅ Call the functions from main.py
# ❌ Don't write the calculation functions again inside main.py
# ❌ Don't use libraries
# 💡 Interview focus: A module is a Python file containing reusable code such as functions, classes, or variables.

from calculator import add, multiply

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print(f"Addition: {add(num1, num2)}")
print(f"Multiplication: {multiply(num1, num2)}")