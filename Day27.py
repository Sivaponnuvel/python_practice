# 🔥 Question 1
# Write a Python program to:
# 👉 Create a function greet()
# take name as parameter
# print "Hello <name>"
# 👉 Call the function
# 🧠 Example Output
# Hello Siva

def greet(name):
    print(f"Hello {name}")
name = input("Enter your name : ")
greet(name)


# 🔥 Question 2
# Write a Python program to:
# 👉 Create a function add_numbers()
# take two numbers as parameters
# return their sum
# 👉 Call the function and print result
# 🧠 Example Output
# Sum: 30

def add_numbers(num1,num2):
    return num1 + num2
num1 = int(input("Enter the first number : "))
num2 = int(input("Enter the second number : "))
print(f"Sum: {add_numbers(num1,num2)}")