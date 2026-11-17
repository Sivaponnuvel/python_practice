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


# Question 2 – Multilevel Inheritance
# Interview Topics: Multilevel Inheritance, Parent Class, Child Class, super(), Method Reusability.
# Create a Python program using multilevel inheritance.
# Requirements:
# 1. Create a parent class named Employee.
# 2. Create a constructor that accepts name.
# 3. Create a method named display_name() to display the employee name.
# 4. Create a child class named Department that inherits from Employee.
# 5. Create a constructor in Department that accepts name and department.
# 6. Use super() to call the parent constructor.
# 7. Create another child class named Salary that inherits from Department.
# 8. Create a constructor in Salary that accepts name, department, and salary.
# 9. Use super() to call the parent constructor.
# 10. Create a method named display_employee_details() to display all three details.
# 11. Get all values from the user using input().
# 12. Create a Salary object and call display_employee_details().
# Sample Input:
# Enter employee name: Ravi
# Enter department: Python Development
# Enter salary: 25000
# Expected Output:
# Employee Name: Ravi
# Department: Python Development
# Salary: 25000

class Employee:
    def __init__(self, name):
        self.name = name
    def display_name(self):
        print(f"Employee Name: {self.name}")

class Department(Employee):
    def __init__(self, name, department):
        super().__init__(name)
        self.department = department

class Salary(Department):
    def __init__(self, name, department, salary):
        super().__init__(name, department)
        self.salary = salary

    def display_employee_details(self):
        super().display_name()
        print(f"Department: {self.department}")
        print(f"Salary: {self.salary}")

emp_name = input("Enter employee name: ")
department = input("Enter department: ")
salary = int(input("Enter salary: "))

emp = Salary(emp_name, department, salary)

emp.display_employee_details()