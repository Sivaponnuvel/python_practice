# 🔹 Question 1
# Write a Python program to:
# 👉 Take name & age from user
# 👉 Store multiple users in a file users.json
# 👉 Structure should be like:
# [
#   {"name": "Siva", "age": 23},
#   {"name": "Ram", "age": 25}
# ]
# 👉 If file already exists →
# Read old data
# Append new user
# Save again
# 👉 Finally print all users

import json
import os
filename = "D:/Python/Own try/practice/Day47/users.json"
name = input("Enter your name: ")
age = int(input("Enter your age: "))
new_user = {"name": name, "age": age}
if os.path.exists(filename):
    try:
        with open(filename,"r") as file:
            user = json.load(file)
    except json.JSONDecodeError:
        user = []
else:
    user = []
user.append(new_user)
with open(filename,"w") as file:
    json.dump(user,file)
print("\nAll Users: ")
for i in user:
    print(f"Name: {i['name']}, Age: {i['age']}")


