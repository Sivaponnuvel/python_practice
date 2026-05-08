# 🔹 Question 1 – Student Subject Marks
# Write a Python program to:
# 👉 Take:
# student name
# Python mark
# Java mark
# 👉 Store in dictionary
# 👉 Print:
# Name
# Python mark
# Java mark
# Total marks
# Average marks
# Example Output:
# Name: Siva
# Python: 80
# Java: 70
# Total: 150
# Average: 75.0

name = input("Enter student name: ")
python = int(input("Enter python mark: "))
java = int(input("Enter java mark: "))
student = {"name": name, "Python mark": python, "Java mark": java}
total_mark = student['Python mark'] + student['Java mark']
average = total_mark / 2
print(f"Name: {student['name']}")
print(f"Python: {student['Python mark']}")
print(f"Java: {student['Java mark']}")
print(f"Total mark: {total_mark}")
print(f"Average: {average}")


# 🔹 Question 2 – Employee Dictionary
# Write a Python program to:
# 👉 Take:
# employee name
# department
# salary
# 👉 Store in dictionary
# 👉 Print all employee details
# 👉 Check:
# If salary > 20000 → print "High Salary ✅"
# Else → print "Low Salary ❌"
# Example Output:
# Name: Siva
# Department: IT
# Salary: 25000
# High Salary ✅

emp_name =  input("Enter employee name: ")
department = input("Enter employee department: ")
salary = int(input("Enter employee salary: "))
employee = {"name": emp_name, "department": department, "salary": salary}
print(f"Name: {employee['name']}")
print(f"Department: {employee['department']}")
print(f"Salary: {employee['salary']}")
if employee['salary'] > 20000:
    print("High Salary ✅")
else:
    print("Low Salary ❌")