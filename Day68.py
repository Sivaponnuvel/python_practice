# 🔹 Question 1 – Function Timer Decorator
# Write a Python program to:
# 👉 Import time module
# 👉 Create a decorator:
# calculate_time(func)
# 👉 Inside decorator:
# Store start time before function call
# Store end time after function call
# Print execution time
# 👉 Create function:
# numbers()
# 👉 Inside function:
# Print numbers from 1 to 5 using loop
# 👉 Apply decorator using:
# @calculate_time
# Example Output:
# 1
# 2
# 3
# 4
# 5
# Execution Time: 0.0001 seconds

import time
def calculate_time(func):
    def wrapper():
        start_time = time.time()
        func()
        end_time = time.time()
        print(f"Execution Time: {end_time - start_time:.4f} seconds")
    return wrapper
@calculate_time
def numbers():
    for i in range(1,6):
        print(i)
numbers()


