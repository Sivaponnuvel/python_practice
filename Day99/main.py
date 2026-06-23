# 🔹 Question 1 – OOP: Method Overriding
# Create a parent class:
# Animal
# Method
# sound()
# Print:
# Animal makes a sound
# Create child classes:
# Dog
# Cat
# Override:
# sound()
# Dog Output:
# Dog barks
# Cat Output:
# Cat meows
# Program Flow
# Take animal type from user:
# Enter Animal Type: dog
# Output:
# Dog barks
# Example 2
# Enter Animal Type: cat
# Output:
# Cat meows
# If invalid animal
# Output:
# Invalid Animal ❌
# ⚠️ Conditions
# ✅ Use inheritance
# ✅ Use method overriding
# ✅ Create object based on user input
# ❌ Don't use if-else inside sound() methods

class Animal:
    def sound(self):
        print("Animal makes a sound")
class Dog(Animal):
    def sound(self):
        print("Dog barks")
class Cat(Animal):
    def sound(self):
        print("Cat meows")

animal_type = input("Enter Animal Type: ").lower()

if animal_type == "dog":
    obj = Dog()
    obj.sound()
elif animal_type == "cat":
    obj = Cat()
    obj.sound()
else:
    print("Invalid Animal ❌")


