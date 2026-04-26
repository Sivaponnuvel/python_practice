# 🔹 Question 1
# Write a Python program to:
# 👉 Create a class User
# attributes: username, password
# 👉 Create methods:
# save_user() →
# Save user details into a file users.txt
# (format: username,password)
# display_users() →
# Read file and print all users
# Rules:
# File should be created automatically if not exists
# Each user in new line
# Use file handling (open, with)
# 🧠 Example Output:
# Users List:
# siva,12345
# ram,pass123

class User:
    def __init__(self, username, password):
        self.__username = username
        self.__password = password
    def save_user(self):
        with open ("D:/Python/Own try/practice/Day44/users.txt","a") as file:
            file.write(f"{self.__username},{self.__password}\n")
    def display_users(self):
        print("Users list:")
        try:   
            with open ("D:/Python/Own try/practice/Day44/users.txt") as file:
                for i in file:
                    print(i.strip())
        except FileNotFoundError:
            print("No users found yet!")
username = input("Enter username: ")
password = input("Enter password: ")
obj = User(username,password)
obj.save_user()
obj.display_users()


# 🔹 Question 2
# Write a Python program to:
# 👉 Create a class LoginSystem
# Methods:
# register(username, password)
# Save to file
# login(username, password)
# Check from file
# If match → "Login Success"
# Else → raise error
# Rules:
# Use same users.txt file
# Handle:
# file not found
# invalid login
# 🧠 Example Output:
# Enter username: siva
# Enter password: 12345
# Login Success ✅
# OR
# Error: Invalid credentials ❌

class LoginSystem:
    def __init__(self,username,password):
        self.__username = username
        self.__password = password
    def register(self):
        try:
            with open ("D:/Python/Own try/practice/Day44/users.txt") as file:
                for i in file:
                    if i.strip() == "":
                        continue
                    name, pwd = i.strip().split(",")
                    if name == self.__username:
                        raise ValueError("User already exists! Please login.")
        except FileNotFoundError:
            pass
        with open ("D:/Python/Own try/practice/Day44/users.txt","a") as file:
            file.write(f"{self.__username},{self.__password}\n")
        print("Registered successfully! ✅")
    def login(self):
        try:
            with open ("D:/Python/Own try/practice/Day44/users.txt") as file:
                for i in file:
                    if i.strip() == "":
                        continue
                    name, pwd = i.strip().split(",")
                    if name == self.__username and pwd == self.__password:
                        print("Login Success ✅")
                        return
            raise ValueError("Invalid credentials ❌")
        except FileNotFoundError:
            print("No users found yet!")
choice = input("Enter 1 for Register / 2 for Login: ")
username1 = input("Enter username: ")
password1 = input("Enter password: ")
obj1 = LoginSystem(username1,password1)
try:
    if choice == "1":
        obj1.register()
    elif choice == "2":
        obj1.login()
    else:
        print("Invalid choice ❌")
except ValueError as e:
    print(e)