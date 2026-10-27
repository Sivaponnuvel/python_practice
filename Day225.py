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


