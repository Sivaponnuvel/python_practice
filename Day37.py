# 🔥 Question 1
# Write a Python program to:
# 👉 Take age from user
# 👉 If age is less than 0 →
# raise error: "Age cannot be negative"
# 👉 Otherwise print:
# "Valid age"
# 🧠 Example Output
# Valid age
# OR
# ValueError: Age cannot be negative

try:
    age = int(input("Enter your age : "))
    if age < 0 :
        raise ValueError("Age cannot be negative")
    print("Valid age")
except ValueError as e:
    print(f"ValueError: {e}")


# 🔥 Question 2
# Write a Python program to:
# 👉 Take a number from user
# 👉 If number is less than 10 →
# raise error: "Number must be >= 10"
# 👉 Otherwise print square of number
# 👉 Handle the error using try-except
# 🧠 Example Output
# Square: 100
# OR
# Error: Number must be >= 10

try:
    number = int(input("Enter the number : "))
    if number < 10:
        raise ValueError("Number must be >= 10")
except ValueError as e:
    print(f"Error: {e}")
else:
    print(f"Square: {number**2}")