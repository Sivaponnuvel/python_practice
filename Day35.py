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

