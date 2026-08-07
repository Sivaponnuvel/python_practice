# 🔹 Question 1 – Sets: Find Common Elements
# Write a Python program to find the common elements between two sets.
# Program Flow
# Take the first set of integers from the user as space-separated input.
# Take the second set of integers from the user as space-separated input.
# Convert both inputs into sets.
# Display the common elements in ascending order.
# Example 1
# Input
# Enter First Set: 1 2 3 4 5
# Enter Second Set: 3 4 5 6 7
# Output
# Common Elements:
# 3 4 5
# Example 2
# Input
# Enter First Set: 1 2
# Enter Second Set: 3 4
# Output
# No Common Elements ❌
# ⚠️ Conditions
# ✅ Take input from the user
# ✅ Convert the input into sets
# ✅ Use the set intersection operator (&) or intersection()
# ✅ Display the result in ascending order
# ❌ Don't use loops to compare every element
# ❌ Don't use list comprehensions

set_1 = set(map(int, input("Enter First Set: ").split()))
set_2 = set(map(int, input("Enter Second Set: ").split()))

common = set_1 & set_2

if common:
    print("Common Elements:")
    print(*sorted(common))
else:
    print("No Common Elements ❌")


# 🔹 Question 2 – Decorators: Display Messages Before and After a Function
# Write a Python program to create a decorator that displays a message before and after executing a function.
# Program Flow
# Create a decorator named display_message.
# Before calling the original function, display:
# Function Started
# After calling the original function, display:
# Function Ended
# Create a function named greet() that displays:
# Welcome to Python
# Apply the decorator using @display_message.
# Call the greet() function.
# Expected Output
# Function Started
# Welcome to Python
# Function Ended
# ⚠️ Conditions
# ✅ Create a decorator function
# ✅ Use an inner function (wrapper)
# ✅ Use @display_message
# ✅ Call the original function inside the wrapper
# ❌ Don't call greet() inside the decorator
# ❌ Don't modify the greet() function except by using the decorator

def display_message(func):
    def wrapper():
        print("Function Started")
        func()
        print("Function Ended")
    return wrapper

@display_message
def greet():
    print("Welcome to Python")

greet()