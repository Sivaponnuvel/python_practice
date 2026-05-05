# 🔹 Question 1 – Student Details (Nested Dictionary)
# 👉 Write a Python program to:
# Take input for 2 students
# For each student store:
# name
# age
# marks
# Store data in this format:
# students = {
#     "Siva": {"age": 23, "marks": 85},
#     "Ram": {"age": 21, "marks": 90}
# }
# 👉 Do the following:
# Print all student details
# Print only names
# Print only marks
# 🧠 Example Output:
# All Students:
# Siva - Age: 23, Marks: 85
# Ram - Age: 21, Marks: 90
# Names:
# Siva
# Ram
# Marks:
# 85
# 90

n = int(input("Enter number of students: "))
students = {}
for i in range(n):
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    mark = int(input("Enter mark: "))
    students[name] = {'age': age, 'marks': mark}
print("All Students:")
for key, value in students.items():
    print(f"{key} - Age: {value['age']}, Marks: {value['marks']}")
print("Names:")
for key in students.keys():
    print(key)
print("Marks:")
for value in students.values():
    print(value["marks"])


