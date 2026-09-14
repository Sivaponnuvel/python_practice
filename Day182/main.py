# 🔹 Question 1 – File Handling: Store and Read User Data
# Write a Python program that takes a user's name and age, stores the information in a text file, and then reads the file to display the saved data.
# Program Flow
# Input:
# Enter your name: Siva
# Enter your age: 22
# Expected Output:
# Data saved successfully ✅
# Saved Data:
# Name: Siva
# Age: 22
# ⚠️ Conditions
# ✅ Use input()
# ✅ Create/open a text file
# ✅ Write the name and age into the file
# ✅ Close the file properly
# ✅ Read the data from the file
# ✅ Display the data
# ❌ Don't use libraries
# ❌ Don't use a dictionary
# ❌ Don't hardcode the name or age

filename = "D:/Backend/Python/Own try/python_practice/Day182/file.txt"

name = input("Enter your name: ")
age = input("Enter your age: ")

with open(filename, "w")as file:
    file.write(name + "\n")
    file.write(age + "\n")
    print("Data saved successfully ✅")

with open(filename)as file:
    lines = file.readlines()
    print("Saved Data: ")
    print(f"Name: {lines[0].strip()}")
    print(f"Age: {lines[1].strip()}")


# 🔹 Question 2 – Modules: Create and Use Your Own Module
# Create a Python module named:
# calculator.py
# Inside the module, create these functions:
# add(a, b)
# multiply(a, b)
# Then create another Python file:
# main.py
# Import the calculator module and use both functions.
# Program Flow
# Input:
# Enter first number: 10
# Enter second number: 5
# Expected Output:
# Addition: 15
# Multiplication: 50
# ⚠️ Conditions
# ✅ Create calculator.py
# ✅ Create add() function inside the module
# ✅ Create multiply() function inside the module
# ✅ Create main.py
# ✅ Import the module
# ✅ Take numbers using input()
# ✅ Convert them to integers
# ✅ Call both module functions
# ❌ Don't use libraries
# ❌ Don't write the calculation directly in main.py
# ❌ Don't use predefined numbers

from calculator import add, multiply

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print(f"Addition: {add(num1, num2)}")
print(f"Multiplication: {multiply(num1, num2)}")