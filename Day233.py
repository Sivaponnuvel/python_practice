# Question 1: Find the First Repeated Word in a String
# Interview Topic: Strings, Lists, Sets, and Loops
# Write a Python function that finds the first word that appears more than once in a given sentence.
# Requirements
# 1. Create a function named first_repeated_word(sentence).
# 2. Treat uppercase and lowercase words as the same.
# 3. Return the first word whose second occurrence is encountered.
# 4. If no word is repeated, return None.
# 5. Ignore basic punctuation such as commas and full stops.
# Example 1
# Input:
# sentence = "Python is easy and Python is powerful"
# Expected Output:
# python
# Example 2
# Input:
# sentence = "Django makes web development easier"
# Expected Output:
# None
# Example 3
# Input:
# sentence = "Code well, test well, deploy well."
# Expected Output:
# well

def first_repeated_word(sentence):
    sentence = sentence.lower()
    for ch in ",.":
        sentence = sentence.replace(ch, "")

    words = sentence.split()

    seen = set()

    for i in words:
        if i in seen:
            return i
        seen.add(i)
    
    return None

sentence = input("Enter the sentence: ")
print(first_repeated_word(sentence))


# Question 2: Validate User Registration Data
# Interview Topic: Dictionaries, Functions, Conditional Statements, and Backend Validation
# In a Python backend application, you receive user registration data as a dictionary.
# Write a function named validate_registration(data) that checks whether the registration data is valid.
# Input Format
# data = {    "username": "siva123",    "email": "siva@gmail.com",    "age": 23,    "password": "Python@123"}
# Requirements
# 1. The username must contain at least 5 characters.
# 2. The email must contain @ and end with .com.
# 3. The age must be at least 18.
# 4. The password must contain at least 8 characters.
# 5. If all conditions are satisfied, return:"Valid registration"
# 6. If any condition fails, return a dictionary containing the error messages for all invalid fields.
# 7. Handle missing fields without raising a KeyError.
# Example 1
# Input:
# data = {    "username": "siva123",    "email": "siva@gmail.com",    "age": 23,    "password": "Python@123"}
# Expected Output:
# "Valid registration"
# Example 2
# Input:
# data = {    "username": "siv",    "email": "sivagmail.com",    "age": 16,    "password": "abc"}
# Expected Output:
# {    "username": "Username must contain at least 5 characters",    "email": "Enter a valid email address",    "age": "Age must be at least 18",    "password": "Password must contain at least 8 characters"}
# Example 3
# Input:
# data = {    "username": "siva123"}
# Expected Output:
# A dictionary containing error messages for the missing email, age, and password fields.

def validate_registration(data):
    result = {}

    username = data.get("username")
    email = data.get("email")
    age = data.get("age")
    password = data.get("password")

    if username is None:
        result["username"] = "Username is required"
    elif len(username) < 5:
        result["username"] = "Username must contain at least 5 characters"

    if email is None:
        result["email"] = "Email is required"
    elif "@" not in email or not email.endswith(".com"):
        result["email"] = "Enter a valid email address"

    if age is None:
        result["age"] = "Age is required"
    elif age < 18:
        result["age"] = "Age must be at least 18"

    if password is None:
        result["password"] = "Password is required"
    elif len(password) < 8:
        result["password"] = "Password must contain at least 8 characters"

    if result:
        return result

    return "Valid registration"

data = {
    "username": "siva123",
    "email": "siva@gmail.com",
    "age": 23,
    "password": "Python@123"
}
print(validate_registration(data))