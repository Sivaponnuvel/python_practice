# 🔹 Question 1 – Prime Number Checker
# Write a Python program to check whether a given number is a prime number or not.
# Program Flow
# Take an integer from the user.
# Check whether the number is prime.
# Display the appropriate message.
# Example 1
# Input:
# Enter a number: 17
# Output:
# 17 is a Prime Number ✅
# Example 2
# Input:
# Enter a number: 20
# Output:
# 20 is Not a Prime Number ❌
# Example 3
# Input:
# Enter a number: 1
# Output:
# 1 is Not a Prime Number ❌
# ⚠️ Conditions
# ✅ Use input()
# ✅ Convert input to int
# ✅ Use a for loop
# ✅ Use % operator
# ✅ Use if/else
# ❌ Don't use any libraries
# ❌ Don't use any built-in prime-checking function
# ❌ Don't hardcode the answer
# 💡 Hint
# A prime number is divisible only by 1 and itself.

def is_prime(number):
    if number <= 1:
        return f"{number} is Not a Prime Number ❌"
    
    for i in range(2, number):
        if number % i == 0:
            return f"{number} is Not a Prime Number ❌"

    return f"{number} is a Prime Number ✅"

number = int(input("Enter a number: "))
print(is_prime(number))


# 🔹 Question 2 – Sum of Digits
# Write a Python program to find the sum of all digits in a given integer.
# Program Flow
# Take a number from the user and calculate the sum of its digits.
# Example 1
# Input:
# Enter a number: 12345
# Output:
# Sum of digits: 15
# Because:
# 1 + 2 + 3 + 4 + 5 = 15
# Example 2
# Input:
# Enter a number: 908
# Output:
# Sum of digits: 17
# Because:
# 9 + 0 + 8 = 17
# ⚠️ Conditions
# ✅ Use input()
# ✅ Convert input to int
# ✅ Use a while loop
# ✅ Use % operator
# ✅ Use // operator
# ❌ Don't convert the number into a string
# ❌ Don't use sum()
# ❌ Don't use any libraries
# 💡 Hint
# For a number like 123:
# 123 % 10 → 3
# 123 // 10 → 12
# Then repeat until the number becomes 0.

num = int(input("Enter a Number: "))

sum_number = 0

while num > 0:
    digit = num % 10
    sum_number += digit
    num //= 10

print(f"Sum of digits: {sum_number}")