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


