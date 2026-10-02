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


