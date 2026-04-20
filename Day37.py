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


