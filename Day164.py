# 🔹 Question 1 – Dictionary + Loop
# Create a dictionary named students:
# students = {
#     "Arun": 85,
#     "Bala": 72,
#     "Kumar": 90,
#     "Ravi": 65,
#     "Siva": 78
# }
# Task:
# Print only the students who scored 75 or above.
# Expected Output:
# Arun 85
# Kumar 90
# Siva 78
# ⚠️ Conditions:
# Use a for loop
# Use .items()
# Use an if condition
# Don't hardcode the names

students = {
    "Arun": 85,
    "Bala": 72,
    "Kumar": 90,
    "Ravi": 65,
    "Siva": 78
}
for key, value in students.items():
    if value > 75:
        print(f"{key} {value}")


# 🔹 Question 2 – Function + List
# Create a function:
# find_even_numbers(numbers)
# The function should accept a list of numbers and return a new list containing only the even numbers.
# Example:
# numbers = [10, 15, 22, 31, 40, 55, 68]
# print(find_even_numbers(numbers))
# Expected Output:
# [10, 22, 40, 68]
# ⚠️ Conditions:
# Use a function
# Use a for loop
# Use %
# Return the result
# Don't use filter()

def find_even_numbers(number):
    even_numbers = []
    for i in number:
        if i % 2 == 0:
            even_numbers.append(i)
    return even_numbers

numbers = [10, 15, 22, 31, 40, 55, 68]
print(find_even_numbers(numbers))