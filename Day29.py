# 🔥 Question 1
# Write a Python program to:
# 👉 Create a lambda function to add two numbers
# 👉 Take two numbers from user
# 👉 Print the result
# 🧠 Example Output
# Sum: 30

x = lambda a,b : a+b
a = int(input("Enter the number : "))
b = int(input("Enter the number : "))
print(f"Sum: {x(a,b)}")


# 🔥 Question 2
# Write a Python program to:
# 👉 Take a list of numbers from user
# 👉 Use lambda with map()
# to square each number
# 👉 Print the result as a list
# 🧠 Example Output
# Input: 1 2 3 4
# Output: [1, 4, 9, 16]

s = lambda a : list(map(lambda x : x**2,a))
a = list(map(int,input("Enter the numbers : ").split()))
print(s(a))