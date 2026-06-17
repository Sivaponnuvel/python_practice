# Question 1 – Decorator (Intermediate)
# Create a decorator:
# timer_decorator
# Before function execution store current time.
# After execution print:
# Execution Time: 0.002 seconds
# Decorate:
# generate_numbers()
# which prints numbers from 1 to 100000.

import time
def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution Time: {end_time - start_time:.3f} seconds")
    return wrapper
@timer_decorator
def generate_numbers():
    for number in range(1, 100001):
        print(number)
generate_numbers()


# Question 2 – Exception Handling
# Create custom exception:
# PasswordTooShortError
# Create function:
# register(password)
# Rules:
# less than 8 chars → raise exception
# otherwise print Registration Successful

class PasswordTooShortError(Exception):
    pass
def register(password):
    if len(password) < 8 :
        raise PasswordTooShortError("Password Too Short ❌")
    return "Registration Successful ✅"
try:
    password = input("Enter Password: ")
    print(register(password))
except PasswordTooShortError as e:
    print(e)