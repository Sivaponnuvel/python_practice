# 🔹 Question 1 – Modules & Packages: Calculator Package
# Create the following structure:
# calculator/
# │
# ├── __init__.py
# ├── arithmetic.py
# └── main.py
# arithmetic.py
# Create the following functions:
# add(a, b)
# subtract(a, b)
# multiply(a, b)
# divide(a, b)
# Rules:
# divide() should return "Cannot divide by zero ❌" if the second number is 0.
# Otherwise return the result.
# main.py
# Import all functions from arithmetic.py.
# Display the menu:
# 1. Add
# 2. Subtract
# 3. Multiply
# 4. Divide
# Take:
# Enter Choice:
# Enter First Number:
# Enter Second Number:
# Call the corresponding function and display the result.
# Example Output 1
# 1. Add
# 2. Subtract
# 3. Multiply
# 4. Divide
# Enter Choice: 3
# Enter First Number: 15
# Enter Second Number: 4
# Result: 60
# Example Output 2
# Enter Choice: 4
# Enter First Number: 20
# Enter Second Number: 0
# Cannot divide by zero ❌
# ⚠️ Conditions
# ✅ Create your own package
# ✅ Use separate module
# ✅ Import functions into main.py
# ❌ Don't write all functions in one file

from arithmetic import add, subtract, multiply, divide

print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = int(input("Enter Choice: "))
a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))

if choice == 1:
    print(f"Result: {add(a, b)}")
elif choice == 2:
    print(f"Result: {subtract(a, b)}")
elif choice == 3:
    print(f"Result: {multiply(a, b)}")
elif choice == 4:
    result = divide(a, b)
    if result == "Cannot divide by zero ❌":
        print(result)
    else:
        print(f"Result: {result}")
else:
    print("Wrong Choice")