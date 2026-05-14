# 🔹 Question 1 – Student Marks Analysis
# Write a Python program to:
# 👉 Create an empty list:
# students = []
# 👉 Take details for 3 students:
# name
# mark
# 👉 Store each student as dictionary inside list
# Example:
# [
#     {"name": "Siva", "mark": 95},
#     {"name": "Ram", "mark": 80}
# ]
# 👉 Print all students like:
# Siva - 95
# Ram - 80
# 👉 Find and print:
# Highest mark
# Lowest mark
# Average mark
# Example Output:
# Highest Mark: 95
# Lowest Mark: 80
# Average Mark: 87.5

students = []
for i in range(3):
    name = input("Enter your name: ")
    mark = int(input("Enter mark: "))
    students.append({"name": name, "mark": mark})
# all students
for i in students:
    print(f"{i['name']} - {i['mark']}")
# Highest mark
highest_mark = students[0]['mark']
for i in students:
    if (i['mark']) > highest_mark:
        highest_mark = i['mark']
print(f"Highest Mark: {highest_mark}")
# Lowest mark
lowest_mark = students[0]['mark']
for i in students:
    if (i['mark']) < lowest_mark:
        lowest_mark = i['mark']
print(f"Lowest Mark: {lowest_mark}")
# Average mark
average_mark = 0
for i in students:
    average_mark += i['mark']
print(f"Average Mark: {average_mark/len(students)}")


