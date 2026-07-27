# 🔹 Question 1 – Functions (**kwargs): Display Employee Details
# Write a Python program using **kwargs to display employee details.
# Program Flow
# Create a function named employee_details(**kwargs).
# Accept any number of keyword arguments.
# Display each key and its corresponding value.
# Example
# Call
# employee_details(
#     id=101,
#     name="Siva",
#     age=21,
#     department="Backend",
#     salary=25000
# )
# Output
# id : 101
# name : Siva
# age : 21
# department : Backend
# salary : 25000
# ⚠️ Conditions
# ✅ Use **kwargs
# ✅ Use a loop
# ✅ Display all key-value pairs
# ❌ Don't access individual keys like kwargs["id"]
# ❌ Don't import any libraries

def employee_details(**kwargs):
    for key, values in kwargs.items():
        print(f"{key} : {values}")

employee_details(
    id=101,
    name="Siva",
    age=21,
    department="Backend",
    salary=25000
)


