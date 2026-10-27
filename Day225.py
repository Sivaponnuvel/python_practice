# 🔹 Question 1 – Dictionary Coding Problem
# Topic: Dictionaries, Loops and Conditional Statements
# Write a Python program to merge two dictionaries. If the same key exists in both dictionaries, add their values together.
# Example 1:
# dict1 = {"a": 10, "b": 20, "c": 30}dict2 = {"b": 15, "c": 25, "d": 40}
# Expected output:
# Merged Dictionary: {'a': 10, 'b': 35, 'c': 55, 'd': 40}
# Example 2:
# dict1 = {"python": 50, "java": 30}dict2 = {"python": 20, "javascript": 40}
# Expected output:
# Merged Dictionary: {'python': 70, 'java': 30, 'javascript': 40}
# Requirements
# 1. Create the two dictionaries shown in Example 1.
# 2. Merge both dictionaries into a new dictionary.
# 3. If a key exists in both dictionaries, add their values.
# 4. If a key exists in only one dictionary, preserve its original value.
# 5. Display the merged dictionary.
# 6. Your solution should work when the dictionary values change.
# Conditions
# - Use loops and conditional statements.
# - Do not use collections.Counter.
# - Do not use external libraries.
# - Do not hardcode the merged output.
# - Do not use the dictionary union operator (|).
# - Preserve the original insertion order of keys.

dict1 = {"a": 10, "b": 20, "c": 30}
dict2 = {"b": 15, "c": 25, "d": 40}

merged = {}

for key, value in dict1.items():
    merged[key] = value

for key, value in dict2.items():
    if key in merged:
        merged[key] += value
    else:
        merged[key] = value

print(f"Merged Dictionary: {merged}")


# 🔹 Question 2 – Exception Handling Coding Problem
# Topic: Functions, try-except-else-finally and Exception Handling
# Write a Python program to perform safe division using exception handling.
# Create a function named safe_division() that accepts two numbers and performs division.
# Example 1:
# safe_division(20, 4)
# Expected output:
# Result: 5.0
# Division completed successfully
# Execution finished
# Example 2:
# safe_division(10, 0)
# Expected output:
# Error: Cannot divide by zero
# Execution finished
# Example 3:
# safe_division(10, "abc")
# Expected output:
# Error: Invalid input type
# Execution finished
# Requirements
# 1. Create a function named safe_division(a, b).
# 2. Use try to perform the division.
# 3. Handle ZeroDivisionError with an appropriate error message.
# 4. Handle TypeError when invalid input types are provided.
# 5. Use else to display the result and Division completed successfully when no exception occurs.
# 6. Use finally to display Execution finished in every case.
# 7. Test the function using all three examples.
# Conditions
# - Use try, except, else, and finally.
# - Handle ZeroDivisionError and TypeError separately.
# - Do not use a bare except.
# - Do not import libraries.
# - Do not hardcode the entire output.
# - The program should continue running after handling an exception.

def safe_division(a, b):
    try:
        result = a / b
        
    except ZeroDivisionError:
        print("Error: Cannot divide by zero")

    except TypeError:
        print("Error: Invalid input type")

    else:
        print(f"Result: {result}")
        print("Division completed successfully")
    
    finally:
        print("Execution finished")

safe_division(20, 4)
print()

safe_division(10, 0)
print()

safe_division(20, "abc")