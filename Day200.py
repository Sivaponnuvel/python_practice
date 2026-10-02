# 🔹 Question 1 – Factorial of a Number
# Write a Python program to find the factorial of a given number using a for loop.
# Example
# Enter a number: 5
# Factorial: 120
# Because:
# 5 × 4 × 3 × 2 × 1 = 120
# ⚠️ Conditions
# ✅ Use a for loop
# ✅ Use a variable to store the factorial
# ❌ Don't use math.factorial()
# ✅ Handle 0 correctly (0! = 1)
# 🎯 Interview focus: Explain how the factorial calculation works.

def factorial(number):
    fact = 1
    for i in range(1, number+1):
        fact *= i

    return fact

number = int(input("Enter a number: "))
print(f"Factorial: {factorial(number)}")


# 🔹 Question 2 – Star Pattern ⭐
# Write a Python program to print the following right-angled triangle star pattern.
# For n = 5:
# *
# **
# ***
# ****
# *****
# Take the number of rows from the user.
# Example
# Enter number of rows: 5
# *
# **
# ***
# ****
# *****
# ⚠️ Conditions
# ✅ Use a loop
# ✅ Take the number of rows using input()
# ❌ Don't hardcode the pattern
# ✅ Pattern should work for different values of n
# 🎯 Interview focus: Explain how the loop controls the number of stars in each row.

n = int(input("Enter number of rows: "))

for i in range(1, n+1):
    for j in range(1, i+1):
        print("*", end="")
    print()