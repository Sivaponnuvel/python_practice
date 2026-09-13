# 🔹 Question 1 – Lambda + filter(): Find Even Numbers
# Given a list of numbers, use a lambda function with filter() to find all the even numbers.
# Program Flow
# Input:
# Enter numbers separated by space: 10 15 20 25 30 35
# Expected Output:
# Even numbers: [10, 20, 30]
# ⚠️ Conditions
# ✅ Use input()
# ✅ Convert the input into a list of integers
# ✅ Use lambda
# ✅ Use filter()
# ✅ Check whether each number is even
# ❌ Don't use a normal def function
# ❌ Don't use a list comprehension
# ❌ Don't use libraries

numbers = list(map(int, input("Enter numbers separated by space: ").split()))

result = list(filter(lambda x: x % 2 == 0, numbers))

print(f"Even numbers: {result}")


# 🔹 Question 2 – Fibonacci Series
# Write a Python program to print the first N terms of the Fibonacci series.
# The Fibonacci sequence starts with:
# 0 1 1 2 3 5 8 13 ...
# Each number is obtained by adding the previous two numbers.
# Program Flow
# Input:
# Enter number of terms: 7
# Expected Output:
# Fibonacci series: 0 1 1 2 3 5 8
# ⚠️ Conditions
# ✅ Use input()
# ✅ Convert input into an integer
# ✅ Use a loop
# ✅ Use variables to store the previous two numbers
# ❌ Don't use libraries
# ❌ Don't use a predefined Fibonacci list
# ❌ Don't use recursion
# ❌ Don't use a ready-made Fibonacci function

number = int(input("Enter number of terms: "))
a, b = 0, 1

print("Fibonacci series:", end=" ")
for i in range(number):
    print(a, end=" ")
    a, b = b, a + b