# 🔹 Question 1 – OOP: Inheritance + Constructor + Method
# Create a parent class named Vehicle.
# Program Flow
# Create Vehicle with:
# brand
# model
# Create a method:
# display()
# It should display:
# Brand : Toyota
# Model : Innova
# Then create a child class named Car that inherits from Vehicle.
# The Car class should have an additional attribute:
# fuel_type
# Use super().__init__() to initialize brand and model.
# Override the display() method in Car.
# Input
# Enter Brand: Toyota
# Enter Model: Innova
# Enter Fuel Type: Diesel
# Output
# Car Details
# Brand     : Toyota
# Model     : Innova
# Fuel Type : Diesel
# ⚠️ Conditions
# ✅ Use a parent class Vehicle
# ✅ Use a child class Car
# ✅ Use inheritance
# ✅ Use super().__init__()
# ✅ Override display()
# ✅ Take input from the user
# ❌ Don't duplicate brand and model initialization in Car
# ❌ Don't use global variables

class Vehicle:
    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model
    def display(self):
        print(f"Brand     : {self.__brand}")
        print(f"Model     : {self.__model}")

class car(Vehicle):
    def __init__(self, brand, model, fuel):
        super().__init__(brand, model)
        self.__fuel = fuel
    def display(self):
        print("Car Details")
        super().display()
        print(f"Fuel Type : {self.__fuel}")

brand = input("Enter Brand: ")
model = input("Enter Model: ")
fuel = input("Enter Fuel Type: ")
obj = car(brand, model, fuel)

obj.display()


# 🔹 Question 2 – String Interview: Remove Duplicate Characters
# Write a Python program to remove duplicate characters from a string while preserving the first occurrence order.
# Example 1
# Enter String: programming
# Output:
# Result: progamin
# Example 2
# Enter String: banana
# Output:
# Result: ban
# Program Flow
# Take a string from the user.
# Check each character.
# Add the character only if it has not already appeared.
# Preserve the original order.
# Display the resulting string.
# ⚠️ Conditions
# ✅ Take input from the user
# ✅ Use a loop
# ✅ Use a dictionary
# ✅ Preserve first occurrence order
# ✅ Build the result manually
# ❌ Don't use set()
# ❌ Don't use dict.fromkeys()
# ❌ Don't use set as the main solution
# ❌ Don't import any libraries
# 💡 Hint
# Think about:
# seen = {}
# result = ""

string = input("Enter String: ")

seen = {}
result  = ""

for i in string:
    if i not in seen:
        seen[i] = True
        result += i

print(f"Result: {result}")