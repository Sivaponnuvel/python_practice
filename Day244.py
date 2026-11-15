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


# Question 2 – Employee Class and Salary Calculation
# Interview Topics: Class, Object, Constructor, Instance Methods, self.
# Create a Python class named Employee.
# Requirements:
# 1. Create a class named Employee.
# 2. Create a constructor that accepts name, basic_salary, and bonus.
# 3. Store these values using instance variables.
# 4. Create a method named calculate_total_salary() that returns the total salary.
# 5. Create another method named display_employee() to display employee details and total salary.
# 6. Create two Employee objects with different details.
# 7. Call display_employee() for both objects.
# Expected Output:
# Employee Name: Ravi
# Basic Salary: 20000
# Bonus: 5000
# Total Salary: 25000
# Employee Name: Priya
# Basic Salary: 30000
# Bonus: 7000
# Total Salary: 37000

class Employee:
    def __init__(self, name, basic_salary, bonus):
        self.name = name
        self.basic_salary = basic_salary
        self.bonus = bonus

    def calculate_total_salary(self):
        return self.basic_salary + self.bonus

    def display_employee(self):
        print(f"Employee Name: {self.name}")
        print(f"Basic Salary: {self.basic_salary}")
        print(f"Bonus: {self.bonus}")
        print(f"Total Salary: {self.calculate_total_salary()}")

emp1 = Employee("Ravi", 20000, 5000)
emp2 = Employee("Priya", 30000, 7000)

emp1.display_employee()
emp2.display_employee()