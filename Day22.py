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


# 🎯 Question 2
# Write a Python program to:
# 👉 Create a class Employee
# 👉 Private variables:
# __name
# __salary
# 👉 Methods:
# set_details(name, salary)
# get_details()
# increase_salary(percent)
# 👉 Increase salary based on percentage
# 🧠 Example
# Name: Siva
# Salary: 10000
# After 10% increase → 11000

class Employee:
    def __init__(self):
        self.__name = None
        self.__salary = None
    def set_details(self,name,salary):
        self.__name = name
        self.__salary = salary
    def get_details(self):
        print(f"Name : {self.__name} \nSalary : {self.__salary}")
    def increase_salary(self,percentage):
        a = self.__salary * percentage/100
        self.__salary += a
        print(f"After {percentage}% increase -> {self.__salary}")
name = input("Enter the employee name : ")
salary = int(input("Enter the employee salary : "))
percentage = int(input("Enter the increase_salary : "))
s1 = Employee()
s1.set_details(name,salary)
s1.get_details()
s1.increase_salary(percentage)