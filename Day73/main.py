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


