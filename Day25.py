# 🔥 Question 1 - Method Overriding
# 🎯 Task
# Write a Python program to:
# 👉 Create class Animal
# method: sound() → print "Animal makes sound"
# 👉 Create class Dog (inherits Animal)
# override method sound() → print "Dog barks"
# 👉 Create object of Dog and call method
# 🧠 Example Output
# Dog barks

class Animal:
    def sound(self):
        return "Animal makes sound"
class Dog(Animal):
    def sound(self):
        return "Dog barks"
obj = Dog()
print(f"{obj.sound()}")


# 🔥 Question 2 - Method Overriding
# Write a Python program to:
# 👉 Create class Shape
# method: area() → print "Calculating area"
# 👉 Create class Circle (inherits Shape)
# override method area() → print "Area of circle"
# 👉 Create class Rectangle (inherits Shape)
# override method area() → print "Area of rectangle"
# 👉 Create objects for Circle and Rectangle and call methods
# 🧠 Example Output
# Area of circle
# Area of rectangle

class Shape:
    def area(self):
        return "Calculating area"
class Circle(Shape):
    def area(self):
        return "Area of circle"
class Rectangle(Shape):
    def area(self):
        return "Area of rectangle"
obj1 = Circle()
obj2 = Rectangle()
print(f"{obj1.area()}")
print(f"{obj2.area()}")