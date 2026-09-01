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


