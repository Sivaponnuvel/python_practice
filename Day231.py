# 🔹 Question 1 – String Coding Problem
# Topic: Strings, Dictionaries and Loops
# Write a Python program to find the first non-repeating character in a given string.
# Example 1
# Input:
# text = "programming"
# Expected output:
# First Non-Repeating Character: p
# Example 2
# Input:
# text = "aabbcddee"
# Expected output:
# First Non-Repeating Character: c
# Example 3
# Input:
# text = "aabbcc"
# Expected output:
# No non-repeating character found
# Requirements
# 1. Get a string from the user.
# 2. Find the frequency of each character.
# 3. Identify the first character whose frequency is exactly 1.
# 4. Preserve the original character order.
# 5. Display the first non-repeating character.
# 6. If no such character exists, display the appropriate message.
# Conditions
# - Use Python strings and dictionaries.
# - Do not use collections.Counter.
# - Do not sort the string.
# - Do not hardcode the output.
# - Your solution should work for different strings.

text = input("Enter text: ")

freq = {}

for i in text:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

for i in text:
    if freq[i] == 1:
        print(f"First Non-Repeating Character: {i}")
        break
else:
    print("No non-repeating character found")


# 🔹 Question 2 – Django Backend Logic Coding Problem
# Topic: Lists, Dictionaries, Functions and Data Validation
# Imagine you are developing a Django REST API for a product management application.
# You receive product data as a list of dictionaries. Write a Python function named get_valid_products(products) that returns only products with valid data.
# Example Input
# products = [    {"id": 1, "name": "Laptop", "price": 50000},    {"id": 2, "name": "Mouse", "price": 500},    {"id": 3, "name": "", "price": 1000},    {"id": 4, "name": "Keyboard", "price": -200},    {"id": 5, "name": "Monitor", "price": 12000},    {"id": 6, "name": "Speaker", "price": 0}]
# Expected Output
# [    {"id": 1, "name": "Laptop", "price": 50000},    {"id": 2, "name": "Mouse", "price": 500},    {"id": 5, "name": "Monitor", "price": 12000}]
# Requirements
# 1. Create a function named get_valid_products(products).
# 2. Accept a list of product dictionaries.
# 3. A product is valid only when:
#    - id is present.
#    - name is present and not empty.
#    - price is greater than zero.
# 4. Return only valid product dictionaries.
# 5. Do not modify the original product list.
# 6. Handle an empty product list by returning an empty list.
# 7. Display the returned valid products.
# Conditions
# - Use functions, lists, dictionaries and conditional statements.
# - Do not import libraries.
# - Do not hardcode the expected output.
# - Do not modify the original list.
# - Your solution should work for different product data.

def get_valid_products(products):
    valid_products = []

    for i in products:
        if 'id' in i and 'name' in i and i['name'].strip() != "" and 'price' in i and i['price'] > 0:
            valid_products.append(i)

    return valid_products

products = [
    {"id": 1, "name": "Laptop", "price": 50000},
    {"id": 2, "name": "Mouse", "price": 500},
    {"id": 3, "name": "", "price": 1000},
    {"id": 4, "name": "Keyboard", "price": -200},
    {"id": 5, "name": "Monitor", "price": 12000},
    {"id": 6, "name": "Speaker", "price": 0}
]

print(get_valid_products(products))