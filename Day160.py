# 🔹 Question 1 – Functions: Check Palindrome Number
# Write a Python program to check whether a number is a palindrome using a function.
# Program Flow
# Create a function named is_palindrome(number).
# Take an integer from the user.
# Reverse the number using a loop.
# Return True if the number and reversed number are the same.
# Otherwise return False.
# Display the appropriate result.
# Example 1
# Input:
# Enter Number: 121
# Output:
# Palindrome Number ✅
# Example 2
# Input:
# Enter Number: 123
# Output:
# Not a Palindrome Number ❌
# ⚠️ Conditions
# ✅ Use a function
# ✅ Function must return True or False
# ✅ Use a loop to reverse the number
# ✅ Use % and //
# ❌ Don't convert the number to a string
# ❌ Don't use slicing
# ❌ Don't import any libraries
# 💡 Hint:
# original = number
# reversed_number = 0


def is_palindrome(number):
    original = number
    reversed_number = 0
    while number > 0:
        digit = number % 10
        reversed_number = reversed_number * 10 + digit
        number //= 10
    return original == reversed_number

try:
    number = int(input("Enter Number: "))
    if is_palindrome(number):
        print("Palindrome Number ✅")
    else:
        print("Not a Palindrome Number ❌")

except ValueError:
    print("Error: Invalid input ❌")


