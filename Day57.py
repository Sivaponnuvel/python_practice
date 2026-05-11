# 🔹 Question 1 – Function with List Return
# Write a Python program to:
# 👉 Create a function:
# get_numbers()
# 👉 Inside function:
# take 5 numbers from user
# store in list
# return the list
# 👉 Outside function:
# call function
# print:
# full list
# largest number
# smallest number
# Example Output:
# Numbers: [10, 20, 30, 40, 50]
# Largest: 50
# Smallest: 10

def get_numbers():
    while True:
        numbers = list(map(int,input("Enter 5 numbers separated by space: ").split()))
        if len(numbers) == 5:
            return numbers
        print("Please enter exactly 5 numbers!")
result = get_numbers()
largest_number = result[0] 
for i in result:
    if i > largest_number:
        largest_number = i
smallest_number = result[0]
for i in result:
    if i < smallest_number:
        smallest_number = i
print(f"Numbers: {result}")
print(f"Largest: {largest_number}")
print(f"Smallest: {smallest_number}")


# 🔹 Question 2 – User Data Validation
# Write a Python program to:
# 👉 Create a function:
# validate_user(name, age)
# Rules:
# name should not be empty
# age should be greater than 0
# 👉 If invalid:
# raise ValueError
# 👉 Else:
# return dictionary:
# {"name": name, "age": age}
# 👉 Take input from user
# 👉 Handle errors using try-except
# Example Output:
# Enter name: Siva
# Enter age: 23
# {'name': 'Siva', 'age': 23}
# OR
# Error: Invalid age ❌

def validate_user(name, age):
        if len(name) < 1:
            raise ValueError("Invalid name ❌")
        if age <= 0:
            raise ValueError("Invalid age ❌")
        return {"name": name, "age": age}
try:
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))    
    print(validate_user(name,age))
except ValueError as e:
    print(f"Error: {e}")