# 🔹 Question 1 – Exception Handling: Safe List Index Access
# Write a Python program to access an element from a list using a user-provided index.
# Program Flow
# Create a list:
# numbers = [10, 20, 30, 40, 50]
# Ask the user to enter an index.
# Display the value at that index.
# Handle:
# Invalid integer input → ValueError
# Index outside the list → IndexError
# Example 1
# Enter Index: 2
# Output:
# Value: 30
# Example 2
# Enter Index: 10
# Output:
# Index Out of Range ❌
# Example 3
# Enter Index: abc
# Output:
# Invalid Input ❌
# ⚠️ Conditions
# ✅ Use try
# ✅ Use except ValueError
# ✅ Use except IndexError
# ✅ Take input from the user
# ✅ Use list indexing
# ❌ Don't use if to check whether the index exists
# ❌ Don't use any libraries

numbers = [10, 20, 30, 40, 50]

try:
    index = int(input("Enter Index: "))
    print(f"Value: {numbers[index]}")

except ValueError:
    print("Invalid Input")
except IndexError:
    print("Index Out of Range")


# 🔹 Question 2 – Dictionary Interview: Find the Most Frequent Element
# Write a Python program to find the most frequently occurring number in a list using a dictionary.
# Program Flow
# Take space-separated integers from the user.
# Store them in a list.
# Count the frequency of each number using a dictionary.
# Find the number with the highest frequency.
# Display the number and its frequency.
# Example 1
# Enter Numbers: 10 20 10 30 20 10
# Output:
# Most Frequent Number : 10
# Frequency            : 3
# Example 2
# Enter Numbers: 5 5 10 10 20
# Output:
# Most Frequent Number : 5
# Frequency            : 2
# If there is a tie, display the first number that reaches the highest frequency.
# ⚠️ Conditions
# ✅ Take input from the user
# ✅ Use a dictionary
# ✅ Use a loop
# ✅ Count frequencies manually
# ✅ Preserve the original order
# ❌ Don't use collections.Counter
# ❌ Don't use max(dictionary, key=dictionary.get)
# ❌ Don't sort the list
# ❌ Don't import any libraries

numbers = list(map(int, input("Enter Numbers: ").split()))

freq = {}
most_num = None
max_freq = 0

for i in numbers:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

    if freq[i] > max_freq:
        max_freq = freq[i]
        most_num = i

print(f"Most Frequent Number : {most_num}")
print(f"Frequency            : {max_freq}")