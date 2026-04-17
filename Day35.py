# 🔥 Question 1
# Write a Python program to:
# 👉 Take a number from user
# 👉 If input is valid → print square of number (inside else)
# 👉 If invalid input → print error
# 🧠 Example Output
# Square: 25
# OR
# Error: invalid input

try:
    number = int(input("Enter the number : "))
except Exception as e:
    print(f"Error : {e}")
else:
    print(f"Square: {number**2}")


# 🔥 Question 2
# Write a Python program to:
# 👉 Take two numbers from user
# 👉 Divide them
# 👉 If no error → print result (inside else)
# 👉 Handle:
# invalid input
# division by zero
# 🧠 Example Output
# Result: 5
# OR
# Error: division by zero
# OR
# Error: invalid input

try:
    num1 = int(input("Enter the 1st number : "))
    num2 = int(input("Enter the 2nd number : "))
    result = num1/num2
except (ZeroDivisionError,ValueError) as e:
    print(f"Error: {e}")
else:
    print(f"Result: {result}")