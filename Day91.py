# Question 1 – Interview Style (Strings + Dictionary)
# Write a Python program to:
# 👉 Take a sentence from user
# Example:
# python is easy and python is powerful
# 👉 Create a dictionary where:
# Key = word
# Value = position(s) where the word appears
# Example Output:
# {
#     "python": [1, 5],
#     "is": [2, 6],
#     "easy": [3],
#     "and": [4],
#     "powerful": [7]
# }
# Conditions
# ❌ Don't use collections module
# ✅ Use dictionary
# ✅ Use loops

user = input("Enter Sentence: ").split()
dictionary = {}
position = 1
for i in user:
    if i not in dictionary:
        dictionary[i] = [position]
    else:
        dictionary[i].append(position)
    position += 1
print(dictionary)


# Question 2 – OOP (Composition)
# Create two classes:
# Engine
# Car
# Engine
# Constructor:
# horsepower
# Method:
# show_engine()
# Car
# Constructor:
# brand
# engine_object
# Method:
# show_car()
# Output:
# Brand: Hyundai
# Horsepower: 120
# Example
# engine = Engine(120)
# car = Car("Hyundai", engine)
# car.show_car()
# Conditions
# ✅ Use one class object inside another class
# ✅ Don't use inheritance

class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower
    def show_engine(self):
        return self.horsepower
    
class Car:
    def __init__(self, brand, engine_object):
        self.brand = brand
        self.engine = engine_object
    def show_car(self):
        print(f"Brand: {self.brand}")
        print(f"Horsepower: {self.engine.show_engine()}")

brand = input("Enter Brand: ")
horsepower = int(input("Enter Horsepower: "))
engine = Engine(horsepower)
car = Car(brand, engine)
car.show_car()