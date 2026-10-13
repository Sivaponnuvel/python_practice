# 🟢 Question 1 – Nested Dictionaries and Data Processing
# Topic: Working with structured data
# Imagine you're developing a student management application. You have the following data:
# students = {    101: {"name": "Arun", "marks": [80, 75, 90]},    102: {"name": "Siva", "marks": [95, 88, 92]},    103: {"name": "Priya", "marks": [70, 85, 78]},    104: {"name": "Kumar", "marks": [60, 65, 72]}}
# Write a Python program to:
# 1. Calculate each student's total marks.
# 2. Calculate each student's average marks.
# 3. Print each student's ID, name, total, and average.
# 4. Find the student with the highest average marks and display their name and average.
# Expected output:
# Student Results:
# ID: 101 | Name: Arun | Total: 245 | Average: 81.67
# ID: 102 | Name: Siva | Total: 275 | Average: 91.67
# ID: 103 | Name: Priya | Total: 233 | Average: 77.67
# ID: 104 | Name: Kumar | Total: 197 | Average: 65.67
# Top Student: Siva
# Highest Average: 91.67
# Rules:
# - Use a for loop to process the dictionary.
# - Use sum() and len() to calculate total and average.
# - Do not hardcode the top student's name.
# - Do not use external libraries.

students = {
    101: {"name": "Arun", "marks": [80, 75, 90]},
    102: {"name": "Siva", "marks": [95, 88, 92]},
    103: {"name": "Priya", "marks": [70, 85, 78]},
    104: {"name": "Kumar", "marks": [60, 65, 72]}
}

print("Student Results:")

top_student = ""
highest_avg = None

for key,value in students.items():
    total = sum(value['marks'])
    avg = round(sum(value['marks']) / len(value['marks']), 2)

    print(f"ID: {key} | Name: {value['name']} | Total: {total} | Average: {avg}")

    if highest_avg is None or avg > highest_avg:
        top_student = value['name']
        highest_avg = avg

print(f"Top Student: {top_student}")
print(f"Highest Average: {highest_avg}")


# 🟢 Question 2 – Decorators
# Topic: Function decorators and reusable validation
# Imagine you're building an application that accepts product prices. Create a decorator called validate_price that checks whether the price is valid before the function executes.
# Start with this structure:
# def validate_price(func):
# Create a function:
# @validate_pricedef add_product(name, price):    print(f"Product: {name}")    print(f"Price: {price}")
# Your program should:
# 1. Allow the function to execute when the price is greater than 0.
# 2. Print "Invalid price!" when the price is 0 or negative.
# 3. Use the decorator to validate the price before executing add_product().
# 4. Test the function with both a valid and an invalid price.
# Expected output for testing:
# Product: Laptop
# Price: 50000
# Invalid price!
# Rules:
# - Use a decorator with @validate_price.
# - Use an inner wrapper function.
# - Use *args and **kwargs in the wrapper.
# - Do not use external libraries.

def validate_price(func):
    def wrapper(*args, **kwargs):
        price  = args[1]
        if price <= 0:
            print("Invalid price!")
        else:
            return func(*args, **kwargs)
    return wrapper

@validate_price
def add_product(name, price):
    print(f"Product: {name}")
    print(f"Price: {price}")

add_product("Laptop", 50000)
add_product("Mobile", -100)