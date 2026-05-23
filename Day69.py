# 🔹 Question 1 – Repeat Function Decorator
# Write a Python program to:
# 👉 Create a decorator:
# repeat_three_times(func)
# 👉 Inside decorator:
# Call the original function 3 times using loop
# 👉 Create function:
# greet()
# 👉 Inside function print:
# Welcome Python
# 👉 Apply decorator using:
# @repeat_three_times
# Example Output:
# Welcome Python
# Welcome Python
# Welcome Python

def repeat_three_times(func):
    def wrapper():
        for i in range(3):
            func()
    return wrapper

@repeat_three_times
def greet():
    print("Welcome Python")
greet()


# 🔹 Question 2 – Uppercase Output Decorator
# Write a Python program to:
# 👉 Create a decorator:
# uppercase_result(func)
# 👉 Inside decorator:
# Convert returned string into uppercase
# 👉 Create function:
# message()
# 👉 Inside function return:
# "hello fastapi"
# 👉 Apply decorator using:
# @uppercase_result
# 👉 Print final result
# Example Output:
# HELLO FASTAPI

def uppercase_result(func):
    def wrapper():
        return func().upper()
    return wrapper

@uppercase_result
def message():
    return "hello fastapi"
print(message())