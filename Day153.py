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


