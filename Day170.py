# 🔹 Question 1 – Number Palindrome
# Write a Python program to check whether a given number is a palindrome or not.
# A number is a palindrome if it reads the same forward and backward.
# Program Flow
# Take an integer from the user.
# Reverse the number using mathematical operations.
# Compare the original number with the reversed number.
# Display the result.
# Example 1
# Input:
# Enter a number: 121
# Output:
# 121 is a Palindrome Number ✅
# Example 2
# Input:
# Enter a number: 123
# Output:
# 123 is Not a Palindrome Number ❌
# Example 3
# Input:
# Enter a number: 1221
# Output:
# 1221 is a Palindrome Number ✅
# ⚠️ Conditions
# ✅ Use input()
# ✅ Convert input to int
# ✅ Use a while loop
# ✅ Use % operator
# ✅ Use // operator
# ❌ Don't convert the number into a string
# ❌ Don't use slicing [::-1]
# ❌ Don't use any built-in reverse function
# ❌ Don't use any libraries
# 💡 Hint
# For 121:
# 121 % 10 → 1
# 121 // 10 → 12
# 12 % 10 → 2
# 12 // 10 → 1
# 1 % 10 → 1
# 1 // 10 → 0
# Build the reversed number and compare it with the original.

number = int(input("Enter a number: "))
original = number
rev = 0
while number > 0:
    digit = number % 10
    rev = rev * 10 + digit
    number //= 10

if original == rev:
    print(f"{original} is a Palindrome Number ✅")
else:
    print(f"{original} is Not a Palindrome Number ❌")


