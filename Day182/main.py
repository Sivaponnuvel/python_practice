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


