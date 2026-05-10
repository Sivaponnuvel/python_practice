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


