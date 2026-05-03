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


