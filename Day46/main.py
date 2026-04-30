# 🔹 Question 1
# Write a Python program to:
# 👉 Create a dictionary:
# course
# duration
# 👉 Store it in a file data.json using JSON
# 👉 Read the file
# 👉 Print the data
# 🧠 Example Output:
# {'course': 'Python', 'duration': '3 months'}

import json
a = {'course': 'Python', 'duration': '3 months'}
with open("D:/Python/Own try/practice/Day46/data.json","w") as file:
    json.dump(a, file)
with open("D:/Python/Own try/practice/Day46/data.json", "r") as file:
    read = json.load(file)
print(read)


# 🔹 Question 2
# Write a Python program to:
# 👉 Take input from user:
# name
# age
# 👉 Store it in user.json using JSON
# 👉 Read the file
# 👉 Print in format:
# 🧠 Example Output:
# Name: Siva
# Age: 23

import json
name = input("Enter your name: ")
age = int(input("Enter your age: "))
x = {'name': name, 'age': age}
with open("D:/Python/Own try/practice/Day46/user.json","w") as file:
    json.dump(x, file)
with open("D:/Python/Own try/practice/Day46/user.json","r") as file:
    a = json.load(file)
print(f"Name: {a['name']}")
print(f"Age: {a['age']}")