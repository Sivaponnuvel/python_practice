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


