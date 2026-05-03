# 🔹 Question 1 – Dictionary Creation & Access
# Write a Python program to:
# 👉 Take input from user:
# name
# age
# city
# 👉 Store in dictionary
# 👉 Print:
# Full dictionary
# Only name
# Only age
# Only city
# 🧠 Example Output:
# {'name': 'Siva', 'age': 23, 'city': 'Chennai'}
# Name: Siva
# Age: 23
# City: Chennai

name = input("Enter your name: ")
age = int(input("Enter your age: "))
city = input("Enter your city: ")
person = {'name': name, 'age': age, 'city': city}
print(person)
print(f"Name: {person['name']}")
print(f"Age: {person['age']}")
print(f"City: {person['city']}")


# 🔹 Question 2 – Update & Add Key
# Write a Python program to:
# 👉 Create a dictionary:
# student = {"name": "Siva", "marks": 80}
# 👉 Do the following:
# Update marks to new value (user input)
# Add new key → "grade" (user input)
# 👉 Print updated dictionary
# 🧠 Example Output:
# {'name': 'Siva', 'marks': 90, 'grade': 'A'}

student = {"name": "Siva", "marks": 80}
new_mark = int(input("Enter marks: "))
grade = input("Enter grade: ").upper()
student["marks"] = new_mark
student["grade"] = grade
print(student)