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


