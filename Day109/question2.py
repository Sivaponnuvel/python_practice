# 🔹 Question 2 – OOP: Library Book Management (Class Variables + Static Method)
# Create a class:
# LibraryBook
# Constructor
# Accept:
# title
# author
# Class Variable
# total_books = 0
# Whenever a new object is created, increase total_books by 1.
# Static Method
# Create:
# is_valid_title(title)
# Rules:
# If title contains only spaces or is empty:
# Invalid Title ❌
# Return False.
# Otherwise return True.
# Use string methods only.
# Instance Method
# Create:
# display()
# Output:
# Title : Python Programming
# Author: Siva
# Program Flow
# Take details for 3 books.
# Before creating an object, validate the title using the static method.
# If valid:
# Create object
# Store it in a list
# Otherwise:
# Book Skipped ❌
# After all inputs:
# Display all valid books.
# Finally display:
# Total Valid Books: X
# Example Output
# Enter Title: Python
# Enter Author: James
# Enter Title:
# Enter Author: Unknown
# Invalid Title ❌
# Book Skipped ❌
# Enter Title: MySQL
# Enter Author: Scott
# --- Library Books ---
# Title : Python
# Author: James
# Title : MySQL
# Author: Scott
# Total Valid Books: 2
# ⚠️ Conditions
# ✅ Use class variable
# ✅ Use static method
# ✅ Use instance method
# ✅ Store objects in a list
# ❌ Don't use global variables
# ❌ Don't validate outside the static method

class LibraryBook:
    total_books = 0

    def __init__(self, title, author):
        self.title = title
        self.author = author
        LibraryBook.total_books += 1
    
    @staticmethod
    def is_valid_title(title):
        if title.strip() == "":
            print("Invalid Title ❌")
            return False
        return True
    
    def display(self):
        print(f"Tile  : {self.title}")
        print(f"Author: {self.author}")

books = []
for i in range(3):
    title = input("Enter Title: ")
    author = input("Enter Author: ")

    if LibraryBook.is_valid_title(title):
        book = LibraryBook(title, author)
        books.append(book)
    else:
        print("Book Skipped ❌")

print("--- Library Books ---")
for book in books:
    book.display()
print(f"Total Valid Books: {LibraryBook.total_books}")