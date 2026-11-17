# Question 1 – Single Inheritance
# Interview Topics: Parent Class, Child Class, Inheritance, super(), Instance Methods.
# Create a Python program using single inheritance.
# Requirements:
# 1. Create a parent class named Person.
# 2. Create a constructor that accepts name and age.
# 3. Store both values using self.
# 4. Create a method named display_person() to display the person's details.
# 5. Create a child class named Student that inherits from Person.
# 6. Create a constructor in Student that accepts name, age, and course.
# 7. Use super() to call the parent class constructor.
# 8. Store course in the child class.
# 9. Create a method named display_student() to display all student details.
# 10. Get all values from the user using input().
# 11. Create a Student object and call display_student().
# Sample Input:
# Enter student name: Arun
# Enter student age: 22
# Enter student course: Python Full Stack
# Expected Output:
# Student Name: Arun
# Age: 22
# Course: Python Full Stack

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display_person(self):
        print(f"Student Name: {self.name}")
        print(f"Age: {self.age}")

class Student(Person):
    def __init__(self, name, age, course):
        super().__init__(name, age)
        self.course = course
    def display_student(self):
        super().display_person()
        print(f"Course: {self.course}")

name = input("Enter student name: ")
age = int(input("Enter student age: "))
course = input("Enter student course: ")

stu = Student(name, age, course)

stu.display_student()


