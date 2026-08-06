# 🔹 Question 1 – While Loop: Reverse a Number
# Write a Python program to reverse a given number using a while loop.
# Program Flow
# Take an integer from the user.
# Reverse the digits using a while loop.
# Display the reversed number.
# Example 1
# Input
# Enter Number: 12345
# Output
# Reversed Number: 54321
# Example 2
# Input
# Enter Number: 900
# Output
# Reversed Number: 9
# ⚠️ Conditions
# ✅ Take input from the user
# ✅ Use a while loop
# ✅ Use % and //
# ❌ Don't convert the number to a string
# ❌ Don't use slicing ([::-1])

number = int(input("Enter Number: "))

rev_num = 0

while number > 0:
    digit =  number % 10
    rev_num = rev_num * 10 + digit
    number  = number // 10

print(f"Reversed Number: {rev_num}")


