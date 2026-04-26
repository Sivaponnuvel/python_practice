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


