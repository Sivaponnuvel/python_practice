# 🔹 Question 1 – Decorator: Login Validation
# Create a decorator called check_login that checks whether a user is logged in before allowing access to a dashboard.
# Requirements:
# Create a decorator check_login.
# Ask the user for login status: yes or no.
# If the status is yes, allow the function to execute.
# If the status is no, display an error message.
# Create a function dashboard(username).
# Use @check_login.
# Example:
# Enter login status (yes/no): yes
# Enter username: Siva
# Expected Output:
# Login successful ✅
# Welcome to dashboard, Siva
# If the user enters:
# Enter login status (yes/no): no
# Expected:
# Please login first ❌
# Conditions:
# Must use a decorator.
# Use *args in the wrapper.
# dashboard() should not execute when the user is not logged in.

def check_login(func):
    def wrapper(*args):
        status = input("Enter login status (yes/no): ").lower()
        if status == "yes":
            print("Login successful ✅")
            print(func(*args))
        else:
            print("Please login first ❌")
    return wrapper

@check_login
def dashboard(username):
    return f"Welcome to dashboard, {username}"

username = input("Enter username: ")
dashboard(username)


# 🔹 Question 2 – OOP: Polymorphism
# Create two classes:
# Dog
# Cat
# Both classes should have the same method:
# sound()
# Requirements:
# Dog should return:
# Dog says: Bark
# Cat should return:
# Cat says: Meow
# Then create objects of both classes and call the same method:
# dog.sound()
# cat.sound()
# Expected Output:
# Dog says: Bark
# Cat says: Meow
# Conditions:
# Create two separate classes.
# Both classes must have a sound() method.
# Do not use inheritance.
# Use the same method name with different implementations.
# This should demonstrate polymorphism.

class Dog:
    def __init__(self):
        pass
    def sound(self):
        return "Bark"

class Cat:
    def __init__(self):
        pass
    def sound(self):
        return "Meow"

dog = Dog()
cat = Cat()

print(f"Dog says: {dog.sound()}")
print(f"Cat says: {cat.sound()}")