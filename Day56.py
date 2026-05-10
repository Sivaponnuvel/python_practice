# 🔹 Question 1 – Function with Dictionary Return
# Write a Python program to:
# 👉 Create a function:
# create_user(name, age)
# 👉 Function should return dictionary like:
# {"name": name, "age": age}
# 👉 Take input from user
# 👉 Call function
# 👉 Print:
# Name
# Age
# Example Output:
# Name: Siva
# Age: 23

def create_user(name, age):
    return {"name": name, "age": age}
name = input("Enter your name: ")
age = int(input("Enter your age: "))
user = create_user(name,age)
print(f"Name: {user['name']}")
print(f"Age: {user['age']}")


# 🔹 Question 2 – List of Users
# Write a Python program to:
# 👉 Create an empty list:
# users = []
# 👉 Take details for 3 users:
# name
# age
# 👉 Store each user as dictionary inside list
# Example:
# [
#     {"name": "Siva", "age": 23},
#     {"name": "Ram", "age": 21}
# ]
# 👉 Print all users like:
# Siva - 23
# Ram - 21

users = []
for i in range(3):
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    user = {"name": name, "age": age}
    users.append(user)
for user in users:
    print(f"{user['name']} - {user['age']}")