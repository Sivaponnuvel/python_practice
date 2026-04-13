# 🔥 Question 1
# Write a Python program to:
# 👉 Create a function show_details()
# use **kwargs
# print all key-value pairs
# 🧠 Example Output
# name : Siva
# age : 21
# city : Chennai

def show_details(**kargs):
    for key , value in kargs.items():
        print(f"{key} : {value}")
name = input("Enter your name : ")
age = int(input("Enter your age : "))
city = input("Enter your city : ")
show_details(name = name,age = age,city = city)


# 🔥 Question 2
# Write a Python program to:
# 👉 Create a function get_total_marks()
# use **kwargs
# values represent marks
# calculate total marks
# 👉 Print the result
# 🧠 Example Output
# Total Marks: 250

def get_total_marks(**kargs):
    total = 0
    for i in kargs.values():
        total += i
    return f"Total Marks : {total}"
tamil = int(input("Enter your tamil mark : "))
english = int(input("Enter your english mark : "))
maths = int(input("Enter your maths mark : "))
science = int(input("Enter your science mark : "))
social = int(input("Enter your social mark : "))
print(get_total_marks(mark1 = tamil, mark2 = english, mark3 = maths, mark4 = science, mark5 = social))