# 🔹 Question 1 – List Interview: Find the Second Largest Unique Number
# Write a Python program to find the second largest unique number in a list.
# Example 1
# Input:
# Enter Numbers: 10 20 30 40 50
# Output:
# Second Largest: 40
# Example 2
# Input:
# Enter Numbers: 10 20 30 30 20
# Output:
# Second Largest: 20
# Program Flow
# Take space-separated integers from the user.
# Store them in a list.
# Find the largest and second largest unique numbers manually.
# Display the second largest number.
# ⚠️ Conditions
# ✅ Take input from the user
# ✅ Use a list
# ✅ Use loops
# ✅ Handle duplicate numbers
# ❌ Don't use sort()
# ❌ Don't use sorted()
# ❌ Don't use max()
# ❌ Don't convert the list into a set
# ❌ Don't import any libraries
# 💡 Hint: Think about maintaining two variables:
# largest
# second_largest

numbers = list(map(int, input("Enter Numbers: ").split()))

largest = numbers[0]

for i in numbers:
    if i > largest:
        largest = i

second = None
for i in numbers:
    if i != largest:
        if second is None or i > second:
            second = i

print(f"Second Largest: {second}")


# 🔹 Question 2 – OOP Polymorphism: Employee Salary
# Create three classes:
# Developer
# Designer
# Manager
# Each class should have a method:
# calculate_salary()
# Each class should calculate salary differently.
# Developer
# Salary = base_salary + bonus
# Designer
# Salary = base_salary + overtime_pay
# Manager
# Salary = base_salary + allowance
# Example Input
# Enter Developer Base Salary: 30000
# Enter Developer Bonus: 5000
# Enter Designer Base Salary: 25000
# Enter Designer Overtime Pay: 3000
# Enter Manager Base Salary: 40000
# Enter Manager Allowance: 8000
# Expected Output
# Developer Salary : 35000
# Designer Salary  : 28000
# Manager Salary   : 48000
# ⚠️ Conditions
# ✅ Use classes
# ✅ Use the same calculate_salary() method in all three classes
# ✅ Implement the method differently in each class
# ✅ Take input from the user
# ✅ Create objects
# ✅ Store the objects in a list
# ✅ Use a loop to call calculate_salary() for each object
# ❌ Don't use separate method names
# ❌ Don't use if/elif to calculate salaries
# ❌ Don't import any libraries

class Developer:
    def __init__(self, dev_base_salary, dev_bonus):
        self.dev_base_salary = dev_base_salary
        self.dev_bonus = dev_bonus

    def calculate_salary(self):
        return self.dev_base_salary + self.dev_bonus

class Designer:
    def __init__(self, des_base_salary, overtime_pay):
        self.des_base_salary = des_base_salary
        self.overtime_pay = overtime_pay

    def calculate_salary(self):
        return self.des_base_salary + self.overtime_pay

class Manager:
    def __init__(self, manage_base_salary, allowance):
        self.manage_base_salary = manage_base_salary
        self.allowance = allowance

    def calculate_salary(self):
        return self.manage_base_salary + self.allowance

dev_base_salary = int(input("Enter Developer Base Salary: "))
dev_bonus = int(input("Enter Developer Bonus: "))

des_base_salary = int(input("Enter Designer Base Salary: "))
overtime_pay = int(input("Enter Designer Overtime Pay: "))

manage_base_salary = int(input("Enter Manager Base Salary: "))
allowance = int(input("Enter Manager Allowance: "))

developer = Developer(dev_base_salary, dev_bonus)
designer = Designer(des_base_salary, overtime_pay)
manager = Manager(manage_base_salary, allowance)

employees = [
    ("Developer", developer),
    ("Designer", designer),
    ("Manager", manager)
]

for name, employee in employees:
    print(f"{name} Salary : {employee.calculate_salary()}")