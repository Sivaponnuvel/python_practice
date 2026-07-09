# 🔹 Question 1 – Context Manager: Database Connection Simulator
# Create a class:
# DatabaseConnection
# Constructor
# Accept:
# database_name
# Implement
# __enter__()
# Print:
# Connecting to student_db...
# Return the object itself.
# __exit__()
# Print:
# Connection Closed Successfully ✅
# Instance Method
# Create:
# execute_query(query)
# Print:
# Executing Query:
# SELECT * FROM students
# Program Flow
# Take database name from the user.
# Use:
# with DatabaseConnection(db_name) as db:
#     query = input("Enter Query: ")
#     db.execute_query(query)
# Example Output
# Enter Database Name: student_db
# Connecting to student_db...
# Enter Query:
# SELECT * FROM students
# Executing Query:
# SELECT * FROM students
# Connection Closed Successfully ✅
# ⚠️ Conditions
# ✅ Create a custom context manager
# ✅ Use __enter__() and __exit__()
# ✅ Return the object from __enter__()
# ✅ Use an instance method
# ❌ Don't use contextlib

class DatabaseConnection:
    def __init__(self, database_name):
        self.database_name = database_name
    def __enter__(self):
        print(f"Connecting to {self.database_name}...")
        return self
    def __exit__(self, exc_type, exc, tb):
        print("Connection Closed Successfully ✅")
    def execute_query(self, query):
        print("Executing Query:")
        print(query)

db_name = input("Enter Database Name: ")

with DatabaseConnection(db_name)as db:
    query = input("Enter Query: ")
    db.execute_query(query)


# 🔹 Question 2 – Interview Question: Longest Word in a Sentence
# Write a Python program to find the longest word in a sentence.
# Example 1
# Enter Sentence:
# Python is an amazing programming language
# Output:
# Longest Word: programming
# Length: 11
# Example 2
# Enter Sentence:
# I love coding
# Output:
# Longest Word: coding
# Length: 6
# Example 3
# Enter Sentence:
# Output:
# No Words Found ❌
# ⚠️ Conditions
# ✅ Take input from the user
# ✅ Use split()
# ✅ Use a loop to find the longest word
# ✅ Handle empty input
# ❌ Don't use max()
# ❌ Don't sort the words

sentence = input("Enter Sentence: ").strip()

if sentence == "":
    print("No Words Found ❌")
else:
    word = sentence.split()
    longest_word = word[0]
    for i in word:
        if len(i) > len(longest_word):
            longest_word = i
    print(f"Longest Word: {longest_word}")
    print(f"Length: {len(longest_word)}")