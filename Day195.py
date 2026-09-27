# 🔹 Question 1 – Sum of Digits
# Write a Python program to find the sum of all digits in a given number.
# Examples
# 123 → 1 + 2 + 3 = 6
# 4567 → 4 + 5 + 6 + 7 = 22
# Input
# Enter a number: 12345
# Expected Output
# Sum of digits: 15
# ⚠️ Conditions
# ✅ Use input()
# ✅ Convert the input to an integer
# ✅ Use a while loop
# ✅ Extract digits using arithmetic logic
# ✅ Use % 10 to get the last digit
# ✅ Use // 10 to remove the last digit
# ❌ Don't convert the number into a string
# ❌ Don't use sum()
# ❌ Don't use libraries

number = int(input("Enter a number: "))

sum_num = 0

while number > 0:
    digit = number % 10
    sum_num += digit
    number //= 10

print(f"Sum of digits: {sum_num}")


