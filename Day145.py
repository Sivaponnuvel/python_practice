# 🔹 Question 1 – Decorators: Measure Function Execution
# Write a Python program to create a decorator that displays messages before and after a function executes and returns the function's result.
# Program Flow
# Create a decorator named execution_logger.
# Before executing the function, display:
# Executing Function...
# After executing the function, display:
# Function Executed Successfully
# The decorator should return the original function's result.
# Create a function named add(a, b) that returns the sum of two numbers.
# Apply the decorator using @execution_logger.
# Take two integers from the user.
# Display the returned result.
# Example
# Input
# Enter First Number: 10
# Enter Second Number: 20
# Output
# uting Function.Exec..
# Function Executed Successfully
# Result: 30
# ⚠️ Conditions
# ✅ Create a decorator
# ✅ Use an inner wrapper(*args, **kwargs)
# ✅ Return the original function's result
# ✅ Use @execution_logger
# ❌ Don't modify the add() function except by decorating it
# ❌ Don't print the result inside the decorator

def execution_logger(func):
    def wrapper(*args, **kwargs):
        print("Executing Function...")
        result = func(*args, **kwargs)
        print("Function Executed Successfully")
        return result
    return wrapper

@execution_logger
def add(a, b):
    return a + b

a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))
print(f"Result: {add(a, b)}")


# 🔹 Question 2 – Dictionary Interview Question: Word Frequency
# Write a Python program to count how many times each word appears in a sentence.
# Program Flow
# Take a sentence from the user.
# Split the sentence into words.
# Store the frequency of each word in a dictionary.
# Display each word and its count.
# Preserve the order of first occurrence.
# Example
# Input
# Enter Sentence: python is easy python is powerful
# Output
# python : 2
# is : 2
# easy : 1
# powerful : 1
# Example 2
# Input
# Enter Sentence: hello hello hello
# Output
# hello : 3
# ⚠️ Conditions
# ✅ Take input from the user
# ✅ Use a dictionary
# ✅ Use split()
# ✅ Use loops
# ✅ Preserve the order of first occurrence
# ❌ Don't use collections.Counter
# ❌ Don't import any libraries

sentence = input("Enter Sentence: ").split()
freq = {}
for i in sentence:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

for key, value in freq.items():
    print(f"{key} : {value}")