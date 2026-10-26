# 🔹 Question 1 – List Coding Problem
# Topic: Lists, Loops and Conditional Statements
# Write a Python program to rotate a list to the right by k positions.
# Example 1:
# nums = [1, 2, 3, 4, 5]k = 2
# Expected output:
# Rotated List: [4, 5, 1, 2, 3]
# Example 2:
# nums = [10, 20, 30, 40]k = 1
# Expected output:
# Rotated List: [40, 10, 20, 30]
# Requirements
# 1. Get a list of integers from the user.
# 2. Get the rotation count k from the user.
# 3. Rotate the list to the right by k positions.
# 4. If k is greater than the list length, handle it correctly.
# 5. Display the rotated list.
# 6. Handle an empty list without errors.
# Conditions
# - Use loops and conditional statements.
# - Do not use sort() or sorted().
# - Do not use external libraries.
# - Do not hardcode the output.
# - Do not use built-in rotation functions.
# - You may use list slicing.

nums = list(map(int, input("Enter a numbers: ").split()))
k = int(input("Enter Rotation count: "))

if len(nums) == 0:
    print("Rotated List: []")

else:
    k %= len(nums)
    roated_list = nums[-k:] + nums[:-k]
    print(f"Rotated List: {roated_list}")


# 🔹 Question 2 – OOP Coding Problem
# Topic: Classes, Inheritance, Constructors and Method Overriding
# Create a parent class named Vehicle and a child class named Car.
# Requirements
# 1. Create a parent class named Vehicle.
# 2. Initialize brand and speed using the Vehicle constructor.
# 3. Create a method named display_info() that displays the vehicle's brand and speed.
# 4. Create a child class named Car that inherits from Vehicle.
# 5. Add an additional attribute named fuel_type in the Car constructor.
# 6. Use super() to initialize the parent class attributes.
# 7. Override display_info() in Car.
# 8. Inside the overridden method, use super().display_info() to display the parent class details.
# 9. Display the car's fuel type.
# 10. Create a Car object and call display_info().
# Example:
# car = Car("Toyota", 120, "Petrol")car.display_info()
# Expected output:
# Brand: Toyota
# Speed: 120
# Fuel Type: Petrol
# Conditions
# - Use proper class inheritance.
# - Use self to access instance attributes.
# - Use super() for constructor initialization and method reuse.
# - Demonstrate method overriding.
# - Do not import libraries.
# - Do not hardcode the entire output outside the class methods.

class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed
        
    def display_info(self):
        print(f"Brand: {self.brand}")
        print(f"Speed: {self.speed}")

class Car(Vehicle):
    def __init__(self, brand, speed, fuel_type):
        super().__init__(brand, speed)
        self.fuel_type = fuel_type

    def display_info(self):
        super().display_info()
        print(f"Fuel Type: {self.fuel_type}")

car = Car("Toyota", 120, "Petrol")

car.display_info()