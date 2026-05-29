# 🔹 Question 1 – JSON Reader & Search System
# Write a Python program to:
# 👉 Create a JSON file manually named:
# users.json
# 👉 Store list of users inside file
# Example:
# [
#     {"id": 1, "name": "Siva"},
#     {"id": 2, "name": "Ram"},
#     {"id": 3, "name": "Vijay"}
# ]
# 👉 Read JSON data using Python
# 👉 Take user id from input
# 👉 Search user by id
# 👉 If found print:
# User Found:
# ID: 2
# Name: Ram
# 👉 Otherwise print:
# User not found ❌
# ⚠️ Conditions:
# ✅ Use json.load()
# ✅ Use loops
# ❌ Do not use list comprehension

import json

user_data = [
     {"id": 1, "name": "Siva"},
     {"id": 2, "name": "Arun"},
     {"id": 3, "name": "Vijay"}
]
with open("D:/Python/Own try/practice/Day75/users.json","w")as file:
    json.dump(user_data, file)
with open("D:/Python/Own try/practice/Day75/users.json","r")as file:
    read = json.load(file)

search_id = int(input("Enter Id to search: "))
found_user = None
for i in read:
    if i["id"] == search_id:
        found_user = i
        break

if found_user:
    print("User Found: ")
    print(f"ID: {found_user['id']}")
    print(f"Name: {found_user['name']}")
else:
    print("User not found ❌")


# 🔹 Question 2 – OOP Library Book System
# Write a Python program to:
# 👉 Create a class:
# Book
# 👉 Constructor should take:
# title
# author
# available_copies
# 👉 Create methods:
# borrow_book()
# return_book()
# show_details()
# 👉 Rules:
# ✅ borrow_book()
# If copies available → reduce by 1
# Otherwise print:
# Book not available ❌
# ✅ return_book()
# Increase copies by 1
# ✅ show_details()
# Print all book details
# 👉 Create object using user input
# 👉 Perform:
# show details
# borrow book
# return book
# show details again
# Example Output:
# Title: Python Basics
# Author: ABC
# Available Copies: 2
# Book Borrowed ✅
# Available Copies: 1

class Book:
    def __init__(self, title, author, available_copies):
        self.__title = title
        self.__author = author
        self.__available_copies = available_copies
    def borrow_book(self):
        if self.__available_copies > 0:
            self.__available_copies -= 1
            print("Book Borrowed ✅")
        else:
            print("Book not available ❌")
    def return_book(self):
        self.__available_copies += 1
        print("Book Returned ✅")
    def show_details(self):
        print("---Book Details---")
        print(f"Title: {self.__title}")
        print(f"Author: {self.__author}")
        print(f"Available Copies: {self.__available_copies}")

title = input("Enter Book Title: ")
author = input("Enter Author Name: ")
available_copies = int(input("Enter Available Copies: "))

book = Book(title, author, available_copies)

book.show_details()
book.borrow_book()
book.show_details()
book.return_book()
book.show_details()