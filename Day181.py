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


