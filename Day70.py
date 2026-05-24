# 🔹 Question 1 – Decorator with Function Arguments and Return Value
# Write a Python program to:
# 👉 Create a decorator:
# check_positive(func)
# 👉 Rules inside decorator:
# If any number is less than 0:
# Negative numbers not allowed ❌
# Otherwise call original function
# 👉 Create function:
# add_numbers(a, b)
# 👉 Function should return addition result
# 👉 Apply decorator using:
# @check_positive
# 👉 Take two numbers from user
# 👉 Print final result
# Example Output:
# Enter a: 10
# Enter b: 20
# Result: 30
# OR
# Enter a: -5
# Enter b: 10
# Negative numbers not allowed ❌

def check_positive(func):
    def wrapper(a,b):
        if a < 0 or b < 0:
            print("Negative numbers not allowed ❌")
        else:
            func(a,b)
    return wrapper

@check_positive
def add_numbers(a,b):
    print(f"Result: {a+b}")
a = int(input("Enter a: "))
b = int(input("Enter b: "))
add_numbers(a,b)


# 🔹 Question 2 – Decorator for Function Call Counter
# Write a Python program to:
# 👉 Create a decorator:
# count_calls(func)
# 👉 Inside decorator:
# Count how many times function is called
# 👉 Create function:
# say_hello()
# 👉 Inside function print:
# Hello User
# 👉 Apply decorator using:
# @count_calls
# 👉 Call function 3 times
# 👉 Every time print function call count
# Example Output:
# Hello User
# Function called 1 times
# Hello User
# Function called 2 times
# Hello User
# Function called 3 times

def count_calls(func):
    count_calls.count = 0
    def wrapper():
        count_calls.count += 1
        func()
        print(f"Function called {count_calls.count} times")
    return wrapper

@count_calls
def say_hello():
    print("Hello User")
say_hello()
say_hello()
say_hello()