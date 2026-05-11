# 🔹 Question 1 – Nested Dictionary Function
# Write a Python program to:
# 👉 Create a function:
# create_student(name, age, marks)
# 👉 Function should return:
# {
#     "name": name,
#     "details": {
#         "age": age,
#         "marks": marks
#     }
# }
# 👉 Take input from user
# 👉 Call function
# 👉 Print:
# Name
# Age
# Marks
# Example Output:
# Name: Siva
# Age: 23
# Marks: 95

def create_student(name,age,marks):
    return {"name": name, "details":{"age": age, "marks": marks}}
name = input("Enter your name: ")
age = int(input("Enter your age: "))
marks = int(input("Enter mark: "))
user = create_student(name,age,marks)
print(f"Name: {user['name']}")
print(f"Age: {user['details']['age']}")
print(f"Marks: {user['details']['marks']}")


# 🔹 Question 2 – User Login Validation
# Write a Python program to:
# 👉 Create a dictionary:
# user_data = {
#     "username": "admin",
#     "password": "1234"
# }
# 👉 Take username and password from user
# Rules:
# username should match stored username
# password should match stored password
# 👉 If invalid:
# raise ValueError
# 👉 Otherwise print:
# Login Successful ✅
# 👉 Handle errors using try-except
# Example Output:
# Enter username: admin
# Enter password: 1234
# Login Successful ✅
# OR
# Error: Invalid username or password ❌

user_data = {
    "username": "admin",
    "password": "1234"
}
username = input("Enter your username: ")
password = input("Enter your password: ")
try:
    if username != user_data['username'] or password != user_data['password']:
        raise ValueError("Invalid username or password ❌")
except ValueError as e:
    print(f"Error: {e}")
else:
    print("Login Successful ✅")