# 🔥 Question 1
# Write a Python program to:
# 👉 Take two numbers from user
# 👉 Divide the numbers
# 👉 Handle error if:
# user enters non-number
# division by zero
# 👉 Print result if no error
# 🧠 Example Output
# Result: 5
# OR
# Error: division by zero
# OR
# Error: invalid input

try:
    number1 = int(input("Enter the 1st number : "))
    number2 = int(input("Enter the 2nd number : "))
    print(f"Result: {number1/number2}")
except ValueError:
    print("Error: invalid input")
except ZeroDivisionError:
    print("Error: division by zero")


