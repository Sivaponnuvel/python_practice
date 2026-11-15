# Question 1 – Student Class and Object
# Interview Topics: Class, Object, Constructor (__init__), Instance Variables, Methods.
# Create a Python class named Student.
# Requirements:
# 1. Create a class named Student.
# 2. Create a constructor that accepts name, age, and course.
# 3. Store these values using self.
# 4. Create a method named display_details() to display all student details.
# 5. Create two Student objects with different details.
# 6. Call display_details() for both objects.
# Expected Output:
# Student Name: Arun
# Age: 22
# Course: Python Full Stack
# Student Name: Kumar
# Age: 23
# Course: Django

class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def display_details(self):
        print(f"Student Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Course: {self.course}")

obj1 = Student("Arun", 22, "Python Full Stack")
obj2 = Student("Kumar", 23, "Django")

obj1.display_details()
obj2.display_details()


