# 🔹 Question 1 – Recursion: Find Sum of Digits
# Write a Python program to find the sum of digits of a number using recursion.
# Program Flow
# Create a function named sum_of_digits(number).
# Take an integer from the user.
# Use recursion to calculate the sum of all digits.
# Return the final sum.
# Example 1
# Input:
# Enter Number: 12345
# Output:
# Sum of Digits: 15
# Example 2
# Input:
# Enter Number: 987
# Output:
# Sum of Digits: 24
# ⚠️ Conditions
# ✅ Use a recursive function
# ✅ Use % and //
# ✅ Take input from the user
# ✅ Return the result
# ❌ Don't use loops
# ❌ Don't convert the number to a string
# ❌ Don't use sum()
# ❌ Don't import any libraries
# 💡 Hint:
# if number == 0:
#     return 0
# Then think about:
# number % 10
# number // 10

def sum_of_digits(number):
    if number == 0:
        return 0
    else:
        return (number % 10) + sum_of_digits(number // 10)

number = int(input("Enter Number: "))
print(f"Sum of Digits: {sum_of_digits(number)}")


