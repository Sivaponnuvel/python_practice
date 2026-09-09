# 🔹 Question 1 – Decorator: Validate Product Price
# Create a decorator called:
# validate_price
# Apply it to:
# create_product(name, price)
# The decorator should check whether the product price is valid before the function executes.
# Program Flow
# Take product details from the user.
# Input:
# Enter product name: Laptop
# Enter price: 50000
# Output:
# Product created successfully ✅
# Product: Laptop
# Price: 50000.0
# If the price is 0 or negative:
# Input:
# Enter product name: Laptop
# Enter price: -5000
# Output:
# Invalid price ❌
# Price must be greater than 0.
# ⚠️ Conditions
# ✅ Create validate_price decorator
# ✅ Create a wrapper function
# ✅ Use @validate_price
# ✅ Use *args
# ✅ Check price inside the decorator
# ✅ Call create_product() only when price is valid
# ✅ Use input()
# ❌ Don't put price validation inside create_product()
# ❌ Don't use libraries

def validate_price(func):
    def wrapper(*args):
        price1 = args[1]
        if price1 <= 0:
            print("Invalid price ❌")
            print("Price must be greater than 0.")
        else:
            print("Product created successfully ✅")
            return func(*args)            
    return wrapper

@validate_price
def create_product(name, price):
    print(f"Product: {name}")
    print(f"Price: {price}")

name = input("Enter product name: ")
price1 = int(input("Enter price: "))
create_product(name, price1)


