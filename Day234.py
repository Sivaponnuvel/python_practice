# Question 1: Find the Most Frequent Character in a String
# Interview Topic: Strings, Dictionaries, and Loops
# Write a Python function named most_frequent_char(text) that finds the character appearing most frequently in a string.
# Requirements
# 1. Count the frequency of each character.
# 2. Ignore spaces.
# 3. Treat uppercase and lowercase characters as the same.
# 4. Return the character with the highest frequency.
# 5. If multiple characters have the same highest frequency, return the character that appears first in the original string.
# 6. If the input contains only spaces or is empty, return None.
# Example 1
# Input:
# text = "programming"
# Expected Output:
# r
# Example 2
# Input:
# text = "Hello World"
# Expected Output:
# l
# Example 3
# Input:
# text = "aabb"
# Expected Output:
# a

def most_frequent_char(text):
    text = text.lower()

    freq = {}

    for i in text:
        if i != " ":
            freq[i] = freq.get(i, 0) + 1

    if not freq:
        return None

    for i in text:
        if i != " " and freq[i] == max(freq.values()):
            return i 

text = input("Enter a text: ")
print(most_frequent_char(text))


# Question 2: Remove Duplicate Records from User Data
# Interview Topic: Dictionaries, Lists, Functions, and Backend Data Processing
# A backend application receives a list of user records. Each record contains a user ID, name, and email.
# Write a function named remove_duplicate_users(users) that removes duplicate records based on the id field.
# Requirements
# 1. Create a function named remove_duplicate_users(users).
# 2. Each user record is a dictionary.
# 3. If multiple records have the same id, keep only the first record.
# 4. Preserve the original order of unique records.
# 5. Return the resulting list.
# 6. Do not modify the original input list.
# Example 1
# Input:
# users = [    {"id": 1, "name": "Siva", "email": "siva@gmail.com"},    {"id": 2, "name": "Arun", "email": "arun@gmail.com"},    {"id": 1, "name": "Siva Kumar", "email": "sivakumar@gmail.com"},    {"id": 3, "name": "Kumar", "email": "kumar@gmail.com"},    {"id": 2, "name": "Arun Kumar", "email": "arunkumar@gmail.com"}]
# Expected Output:
# [    {"id": 1, "name": "Siva", "email": "siva@gmail.com"},    {"id": 2, "name": "Arun", "email": "arun@gmail.com"},    {"id": 3, "name": "Kumar", "email": "kumar@gmail.com"}]
# Example 2
# Input:
# users = [    {"id": 10, "name": "John", "email": "john@gmail.com"},    {"id": 20, "name": "David", "email": "david@gmail.com"}]
# Expected Output: Both records should be returned without changes.
# Example 3
# Input:
# users = []
# Expected Output:
# []

def remove_duplicate_users(users):
    remove_duplicate = []
    seen_ids = []

    for i in users:
        if i['id'] not in seen_ids:
            remove_duplicate.append(i)
            seen_ids.append(i['id'])

    return remove_duplicate

users = [
    {"id": 1, "name": "Siva", "email": "siva@gmail.com"},
    {"id": 2, "name": "Arun", "email": "arun@gmail.com"},
    {"id": 1, "name": "Siva Kumar", "email": "sivakumar@gmail.com"},
    {"id": 3, "name": "Kumar", "email": "kumar@gmail.com"},
    {"id": 2, "name": "Arun Kumar", "email": "arunkumar@gmail.com"}
]
print(remove_duplicate_users(users))