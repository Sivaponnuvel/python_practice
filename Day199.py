# 1. Student Grade Calculator
# Task:
# Class: Student
# Attributes: name, marks (list)
# Methods: 
# add_mark(mark) → add a mark to the list
# average() → return average marks
# display_info() → print name and average
# Challenge: If average ≥ 90 print “Grade A”, else if ≥ 75 “Grade B”, else “Grade C”.

class Student:
    def __init__(self, name):
        self.name = name
        self.marks = []

    def add_mark(self, mark):
        self.marks.extend(mark)

    def average(self):
        avg = sum(self.marks) / len(self.marks)
        return avg

    def display_info(self):
        
        print(f"Student Name: {self.name}")
        print(f"Average: {self.average()}")

        if self.average() >= 90:
            print("Grade A")
        elif self.average() >= 75:
            print("Grade B")
        else:
            print("Grade C")


name = input("Enter a name: ")
obj = Student(name)

marks = list(map(int, input("Enter a marks: ").split()))
obj.add_mark(marks)

obj.display_info()


# 2. Rectangle Area & Perimeter
# Task:
# Class: Rectangle
# Attributes: length, width
# Methods: 
# area() → length × width
# perimeter() → 2 × (length + width)
# Challenge: Create multiple rectangle objects and find the one with the largest area.

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

length1 = int(input("Enter length of Rectangle 1: "))
width1 = int(input("Enter width of Rectangle 1: "))
obj1 = Rectangle(length1, width1)

length2 = int(input("Enter length of Rectangle 2: "))
width2 = int(input("Enter width of Rectangle 2: "))
obj2 = Rectangle(length2, width2)

length3 = int(input("Enter length of Rectangle 3: "))
width3 = int(input("Enter width of Rectangle 3: "))
obj3 = Rectangle(length3, width3)

largest = max(obj1.area(), obj2.area(), obj3.area())

print(f"Maximum Area: {largest}")