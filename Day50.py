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


