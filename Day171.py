# 🔹 Question 1 – Fibonacci Series
# Write a Python program to print the Fibonacci series for n terms.
# The Fibonacci sequence starts with:
# 0 1 1 2 3 5 8 13 ...
# Program Flow
# Take the number of terms from the user.
# Generate the Fibonacci series using a loop.
# Display the result.
# Example 1
# Input:
# Enter number of terms: 7
# Output:
# Fibonacci Series:
# 0 1 1 2 3 5 8
# Example 2
# Input:
# Enter number of terms: 5
# Output:
# Fibonacci Series:
# 0 1 1 2 3
# ⚠️ Conditions
# ✅ Use input()
# ✅ Convert input to int
# ✅ Use a for loop
# ✅ Use variables to store the previous two numbers
# ❌ Don't use recursion
# ❌ Don't use any libraries
# ❌ Don't hardcode the sequence
# 💡 Hint
# Start with:
# a = 0
# b = 1
# Inside the loop, print a, then update:
# a, b = b, a + b

number = int(input("Enter number of terms: "))
a, b = 0, 1
for i in range(number):
    print(a, end=" ")
    a, b = b, a + b


