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


# 🔹 Question 2 – While Loop: Check Whether a Number is an Armstrong Number
# Write a Python program to check whether a given number is an Armstrong Number.
# An Armstrong number is a number that is equal to the sum of its digits, where each digit is raised to the power of the total number of digits.
# Example 1
# Input
# Enter Number: 153
# Output
# Armstrong Number ✅
# Explanation:
# 1³ + 5³ + 3³ = 153
# Example 2
# Input
# Enter Number: 9474
# Output
# Armstrong Number ✅
# Explanation:
# 9⁴ + 4⁴ + 7⁴ + 4⁴ = 9474
# Example 3
# Input
# Enter Number: 123
# Output
# Not an Armstrong Number ❌
# ⚠️ Conditions
# ✅ Take input from the user
# ✅ Use while loop
# ✅ Use % and // to extract digits
# ✅ Calculate the number of digits without converting the number to a string
# ❌ Don't use str()
# ❌ Don't use len()
# ❌ Don't import any libraries

num = int(input("Enter Number: "))

original = num
temp = num
count = 0

while temp > 0:
    count += 1
    temp = temp // 10

temp = original
arms_num = 0

while temp > 0:
    digit = temp % 10
    arms_num += digit ** count
    temp = temp // 10

if original == arms_num:
    print("Armstrong Number ✅")
else:
    print("Not an Armstrong Number ❌")
