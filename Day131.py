# 🔹 Question 1 – Functions (*args): Find the Largest Number
# Write a Python program using *args to find the largest number among the given values.
# Program Flow
# Create a function named find_largest(*args).
# Accept any number of integer arguments.
# Find the largest number.
# Return the result.
# Call the function and display the output.
# Example
# Call
# find_largest(12, 45, 8, 99, 34)
# Output
# Largest Number: 99
# ⚠️ Conditions
# ✅ Use *args
# ✅ Use a loop
# ✅ Return the result
# ✅ Display the returned value
# ❌ Don't use max()
# ❌ Don't sort the values

def find_largest(*args):
    if not args:
        return None
    
    largest = args[0]
    for i in args:
        if largest < i:
            largest = i
    return largest

print(f"Largest Number: {find_largest(7, 21, 35, 77, 50)}")


