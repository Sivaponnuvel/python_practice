# 🎯 Question 1
# Write a Python program to:
# 👉 Create a class Rectangle
# 👉 Private variables:
# __length
# __width
# 👉 Methods:
# set_values(length, width)
# area() → return length × width
# perimeter() → return 2 × (length + width)
# 🧠 Example Output
# Area: 20
# Perimeter: 18

class Rectangle:
    def __init__(self):
        self.__length = None
        self.__width = None
    def set_values(self,length,width):
        self.__length = length
        self.__width = width
    def area(self):
        return self.__length * self.__width
    def perimeter(self):
        return 2 * (self.__length + self.__width)
length = int(input("Enter the length value : "))
width = int(input("Enter the width value : "))
s = Rectangle()
s.set_values(length,width)
print(f"Area : {s.area()}")
print(f"Perimeter : {s.perimeter()}")


