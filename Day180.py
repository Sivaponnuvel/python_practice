# 🔹 Question 1 – Lambda Function: Square of a Number
# Create a lambda function that takes a number and returns its square.
# Program Flow
# Input:
# Enter a number: 7
# Expected Output:
# Square of 7: 49
# ⚠️ Conditions
# ✅ Use input()
# ✅ Convert the input into an integer
# ✅ Create a lambda function
# ✅ Lambda must accept one argument
# ✅ Use the lambda function to calculate the square
# ❌ Don't use a normal def function
# ❌ Don't use libraries

result = lambda number: number ** 2

number = int(input("Enter a number: "))
print(f"Square of {number}: {result(number)}")


# 🔹 Question 2 – Prime Number
# Write a Python program to check whether a given number is a prime number.
# A prime number has exactly two factors: 1 and itself.
# Examples:
# 2 → Prime
# 7 → Prime
# 9 → Not Prime
# Program Flow
# Input:
# Enter a number: 17
# Expected Output:
# 17 is a Prime Number ✅
# For a non-prime:
# Input:
# Enter a number: 15
# Expected Output:
# 15 is Not a Prime Number ❌
# ⚠️ Conditions
# ✅ Use input()
# ✅ Convert input into an integer
# ✅ Use a loop
# ✅ Check whether the number has any divisor other than 1 and itself
# ❌ Don't use libraries
# ❌ Don't use a predefined number
# ❌ Don't use a ready-made prime-number function

def is_prime(number):
    if number <= 1:
        return f"{number} is Not a Prime Number ❌"
    for i in range(2, number):
        if number % i == 0:
            return f"{number} is Not a Prime Number ❌"
    return f"{number} is a Prime Number ✅"

num = int(input("Enter a number: "))
print(is_prime(num))