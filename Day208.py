# 🟢 Question 1 – JSON Handling
# Topic: Python json Module
# Create a Python program that stores the following employee data as a Python dictionary:
# employee = {    "id": 101,    "name": "Siva",    "role": "Python Developer",    "skills": ["Python", "Django", "React"]}
# Your program should:
# 1. Convert the Python dictionary into a JSON string using json.dumps().
# 2. Print the JSON string.
# 3. Convert the JSON string back into a Python dictionary using json.loads().
# 4. Print:
#    - Employee name
#    - Employee role
#    - Employee skills
# Expected Output
# JSON Data: {"id": 101, "name": "Siva", "role": "Python Developer", "skills": ["Python", "Django", "React"]}
# Employee Name: Siva
# Employee Role: Python Developer
# Employee Skills: ['Python', 'Django', 'React']

import json

employee = {
    "id": 101,
    "name": "Siva",
    "role": "Python Developer",
    "skills": ["Python", "Django", "React"]
}

json_data = json.dumps(employee)

print(f"JSON Data: {json_data}")

py_dict = json.loads(json_data)

print(f"Employee Name: {py_dict['name']}")
print(f"Employee Role: {py_dict['role']}")
print(f"Employee Skills: {py_dict['skills']}")


# 🟢 Question 2 – Functions with *args and **kwargs
# Topic: Advanced Functions
# Create a function:
# def order_summary(*items, **customer_details):
# Call the function like:
# order_summary(    "Laptop",    "Mouse",    "Keyboard",    name="Siva",    city="Villupuram",    payment="UPI")
# Your function should:
# 1. Print all ordered items using *items.
# 2. Print customer name, city and payment method using **customer_details.
# 3. Print the total number of items.
# Expected Output
# Customer Name: Siva
# City: Villupuram
# Payment: UPI
# Ordered Items:
# Laptop
# Mouse
# Keyboard
# Total Items: 3

def order_summary(*items, **customer_details):
    print(f"Customer Name: {customer_details['name']}")
    print(f"City: {customer_details['city']}")
    print(f"Payment: {customer_details['payment']}")

    print("Ordered Items:")
    for i in items:
        print(i)
    print(f"Total Items: {len(items)}")

order_summary("Laptop", "Mouse", "Keyboard",  name="Siva", city="Villupuram", payment="UPI")