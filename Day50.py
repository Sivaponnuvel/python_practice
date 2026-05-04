# 🔹 Question 1 – Loop Through Dictionary
# Write a Python program to:
# 👉 Create a dictionary:
# student = {"name": "Siva", "age": 23, "city": "Chennai"}
# 👉 Do the following using loop:
# Print only keys
# Print only values
# Print both key and value
# 🧠 Example Output:
# Keys:
# name
# age
# city
# Values:
# Siva
# 23
# Chennai
# Key-Value:
# name : Siva
# age : 23
# city : Chennai

name = input("Enter your name: ")
age = int(input("Enter your age: "))
city = input("Enter your city: ")
person = {'name': name, 'age': age, 'city': city}
print("Keys:")
for key in person.keys():
    print(key)
print("Values:")
for value in person.values():
    print(value)
print("Key-Value:")
for key, value in person.items():
    print(f"{key} : {value}")


# 🔹 Question 2 – Dictionary with Multiple Students
# Write a Python program to:
# 👉 Create a dictionary:
# students = {
#     "Siva": 85,
#     "Ram": 70,
#     "Arun": 90
# }
# 👉 Do the following:
# Print all students with marks
# Count how many students
# Find student with marks > 80
# 🧠 Example Output:
# All Students:
# Siva - 85
# Ram - 70
# Arun - 90
# Total Students: 3
# Above 80:
# Siva - 85
# Arun - 90

students = {}
n = int(input("How many students? "))
for i in range(n):
    name = input("Enter student name: ")
    mark = int(input("Enter mark: "))
    students[name] = mark
print("All Students:")
for key , value in students.items():
    print(f"{key} - {value}")
print(f"Total Students: {len(students)}")
print("Above 80:")
found = False
for key , value in students.items():
    if value > 80:
        print(f"{key} - {value}")
        found = True
if not found:
    print("No students above 80")