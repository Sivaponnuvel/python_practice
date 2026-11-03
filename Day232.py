# 🔹 Question 1 – Find Duplicate Elements in a List
# Topic: Lists, Sets, Dictionaries and Loops
# Write a Python program to find all duplicate elements in a list and display each duplicate only once, preserving the order in which duplicates are first detected.
# Example 1
# Input:
# numbers = [10, 20, 30, 20, 40, 10, 50, 30, 20]
# Expected output:
# Duplicate Elements: [20, 10, 30]
# Example 2
# Input:
# numbers = [1, 2, 3, 4, 5]
# Expected output:
# Duplicate Elements: []
# Requirements
# 1. Get a list of integers from the user.
# 2. Identify elements that appear more than once.
# 3. Include each duplicate only once in the result.
# 4. Preserve the order in which duplicates are first detected.
# 5. Display an empty list if there are no duplicates.
# 6. Your solution must work for different input lists.
# Conditions
# - Use Python lists and loops.
# - Do not use collections.Counter.
# - Do not use numbers.count() to identify duplicates.
# - Do not sort the input list.
# - Do not hardcode the output.

numbers = list(map(int, input("Enter numbers: ").split()))

duplicates = []

for i in range(len(numbers)):
    found = False

    for j in range(i + 1, len(numbers)):
        if numbers[i] == numbers[j]:
            found = True
            break

    if found and numbers[i] not in duplicates:
        duplicates.append(numbers[i])

print(f"Duplicate Elements: {duplicates}")


# 🔹 Question 2 – Django Backend: Group Products by Category
# Topic: Functions, Lists, Dictionaries and Data Processing
# Imagine you are developing an e-commerce backend using Django. You receive product data from a database as a list of dictionaries.
# Write a function named group_products_by_category(products) that groups product names by their category.
# Example Input
# products = [    {"id": 1, "name": "Laptop", "category": "Electronics"},    {"id": 2, "name": "Mouse", "category": "Electronics"},    {"id": 3, "name": "Shirt", "category": "Clothing"},    {"id": 4, "name": "Jeans", "category": "Clothing"},    {"id": 5, "name": "Keyboard", "category": "Electronics"},    {"id": 6, "name": "Shoes", "category": "Footwear"}]
# Expected Output
# {    "Electronics": ["Laptop", "Mouse", "Keyboard"],    "Clothing": ["Shirt", "Jeans"],    "Footwear": ["Shoes"]}
# Requirements
# 1. Create the function group_products_by_category(products).
# 2. Accept a list of product dictionaries.
# 3. Group product names under their respective categories.
# 4. Add products with the same category to the same list.
# 5. Create a new category when it is encountered for the first time.
# 6. Return the grouped dictionary.
# 7. Return an empty dictionary when the input list is empty.
# 8. Do not modify the original product list.
# Conditions
# - Use dictionaries, lists, loops and conditional statements.
# - Do not import libraries.
# - Do not hardcode the expected output.
# - Your solution must work with different product records.

def group_products_by_category(products):
    grouped_dict = {}

    for i in products:
        if i['category'] not in grouped_dict:
            grouped_dict[i['category']] = []

        grouped_dict[i['category']].append(i['name'])

    return grouped_dict

products = [
    {"id": 1, "name": "Laptop", "category": "Electronics"},
    {"id": 2, "name": "Mouse", "category": "Electronics"},
    {"id": 3, "name": "Shirt", "category": "Clothing"},
    {"id": 4, "name": "Jeans", "category": "Clothing"},
    {"id": 5, "name": "Keyboard", "category": "Electronics"},
    {"id": 6, "name": "Shoes", "category": "Footwear"}
]
print(group_products_by_category(products))