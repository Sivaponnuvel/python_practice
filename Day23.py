# Question 1
# Write a Python program to:
# 👉 Create class Person
# name
# age
# method: display()
# 👉 Create class Student (inherits Person)
# add: marks
# method: display_student()
# 🧠 Example Output
# Name: Siva
# Age: 21
# Marks: 85

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display(self): 
        print(f"Name : {self.name} \nAge : {self.age}")
class Student(Person):
    def __init__(self,name,age,mark):
        super().__init__(name,age)
        self.mark = mark
    def display_student(self):
        print(f"Mark: {self.mark}")
name = input("Enter your name : ")
age = int(input("Enter your age : "))
mark = int(input("Enter the student mark : "))
s = Student(name,age,mark)
s.display()
s.display_student()


# Question 2
# Write a Python program to:
# 👉 Create class Employee
# variables: name, salary
# method: display_employee()
# 👉 Create class Manager (inherits Employee)
# add variable: department
# method: display_manager()
# 👉 Create object and display all details

class Employee:
    def __init__(self,name,salary):
        self.name = name 
        self.salary = salary
    def display_employee(self):
        print(f"Name : {self.name} \nSalary : {self.salary}")
class Manager(Employee):
    def __init__(self,name,salary,department):
        super().__init__(name, salary)
        self.department =  department
    def display_manager(self):
        print(f"Department : {self.department}")
name = input("Enter the employee name : ")
salary = int(input("Enter the employee salary : "))
department = input("Enter the employee department : ")
e = Manager(name,salary,department)
e.display_employee()
e.display_manager()