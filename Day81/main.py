# 🔹 Question 1 – JSON Product Inventory System
# Write a Python program to:
# 👉 Create a JSON file named:
# products.json
# 👉 Store product details as a list of dictionaries
# Example:
# [
#     {"id": 1, "name": "Laptop", "stock": 5},
#     {"id": 2, "name": "Mouse", "stock": 10}
# ]
# 👉 Create functions:
# view_products()
# update_stock(product_id, quantity)
# 👉 Function Details:
# ✅ view_products()
# Print all products
# Example:
# ID: 1
# Name: Laptop
# Stock: 5
# ✅ update_stock(product_id, quantity)
# Search product using id
# If found:
# Increase stock by given quantity
# Save updated data back into JSON file
# Print:
# Stock Updated ✅
# Otherwise:
# Product Not Found ❌
# 👉 Call all functions properly
# Example Output:
# --- Products ---
# ID: 1
# Name: Laptop
# Stock: 5
# ID: 2
# Name: Mouse
# Stock: 10
# Enter Product ID: 1
# Enter Quantity: 3
# Stock Updated ✅
# ⚠️ Conditions:
# ✅ Use json.load()
# ✅ Use json.dump()
# ✅ Use functions
# ✅ Use file handling

import json

products = [
    {"id": 1, "name": "Laptop", "stock": 5},
    {"id": 2, "name": "Mouse", "stock": 10}
]

file_path = "D:/Backend/Python/Own try/practice/Day81/products.json"

with open(file_path,"w") as file:
    json.dump(products, file, indent=4)

def view_products():
    with open(file_path,"r") as file:
        read  = json.load(file)
    print("--- Products ---")
    for i in read:
        print(f"ID: {i['id']}")
        print(f"Name: {i['name']}")
        print(f"Stock: {i['stock']}")
def update_stock(product_id, quantity):
    with open(file_path,"r") as file:
        read  = json.load(file)
    found = False
    for i in read:
        if product_id == i['id']:
            i['stock'] += quantity
            found = True
            break
    if found:
        with open(file_path,"w") as file:
            json.dump(read, file, indent=4)
        print("Stock Updated ✅")
    else:
        print("Product Not Found ❌")

view_products()
product_id = int(input("Enter Product Id: "))
quantity = int(input("Enter Quantity: "))
update_stock(product_id, quantity)


