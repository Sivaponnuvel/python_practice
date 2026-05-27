# 🔹 Question 1 – JSON File Writer
# Write a Python program to:
# 👉 Import json module
# 👉 Take user details:
# name
# age
# city
# 👉 Store details inside dictionary
# Example:
# {
#     "name": "Siva",
#     "age": 23,
#     "city": "Chennai"
# }
# 👉 Write dictionary into a JSON file named:
# user.json
# 👉 Print:
# Data stored successfully ✅
# ⚠️ Conditions:
# ✅ Use json.dump()
# ✅ Use file handling

import json
name = input("Enter your name: ")
age = int(input("Enter your age: "))
city = input("Enter your city: ")
user = {"name": name, "age": age, "city": city}
with open("D:/Python/Own try/practice/Day73/user.json","w") as file:
    json.dump(user, file)
print("Data stored successfully ✅")


# 🔹 Question 2 – Exception Handling with File Reading
# Write a Python program to:
# 👉 Ask filename from user
# 👉 Try to open and read file
# 👉 Print file content
# 👉 Handle errors using exception handling
# Rules:
# If file does not exist:
# File not found ❌
# If any other error occurs:
# Something went wrong ❌
# Example Output:
# Enter filename: notes.txt
# Python is easy
# FastAPI is powerful
# OR
# Enter filename: data.txt
# File not found ❌

import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

try:
    user = input("Enter filename: ")
    with open(user) as file:
        content = file.read()
    if content:
        print(content)
    else:
        print("File is empty")
except FileNotFoundError:
    print("File not found ❌")
except Exception:
    print("Something went wrong ❌") 