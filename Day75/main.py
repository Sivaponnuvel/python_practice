# 🔹 Question 1 – JSON Reader & Search System
# Write a Python program to:
# 👉 Create a JSON file manually named:
# users.json
# 👉 Store list of users inside file
# Example:
# [
#     {"id": 1, "name": "Siva"},
#     {"id": 2, "name": "Ram"},
#     {"id": 3, "name": "Vijay"}
# ]
# 👉 Read JSON data using Python
# 👉 Take user id from input
# 👉 Search user by id
# 👉 If found print:
# User Found:
# ID: 2
# Name: Ram
# 👉 Otherwise print:
# User not found ❌
# ⚠️ Conditions:
# ✅ Use json.load()
# ✅ Use loops
# ❌ Do not use list comprehension

import json

user_data = [
     {"id": 1, "name": "Siva"},
     {"id": 2, "name": "Arun"},
     {"id": 3, "name": "Vijay"}
]
with open("D:/Python/Own try/practice/Day75/users.json","w")as file:
    json.dump(user_data, file)
with open("D:/Python/Own try/practice/Day75/users.json","r")as file:
    read = json.load(file)

search_id = int(input("Enter Id to search: "))
found_user = None
for i in read:
    if i["id"] == search_id:
        found_user = i
        break

if found_user:
    print("User Found: ")
    print(f"ID: {found_user['id']}")
    print(f"Name: {found_user['name']}")
else:
    print("User not found ❌")


