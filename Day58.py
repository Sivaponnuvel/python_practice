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

