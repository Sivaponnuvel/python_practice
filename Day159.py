# 🔹 Question 1 – Dictionary Interview: Find the Most Frequent Element
# Write a Python program to find the most frequent number in a list using a dictionary.
# Example 1
# Input:
# Enter Numbers: 10 20 10 30 20 10
# Output:
# Most Frequent: 10
# Frequency     : 3
# Example 2
# Input:
# Enter Numbers: 5 8 5 8 8 2
# Output:
# Most Frequent: 8
# Frequency     : 3
# Program Flow
# Take space-separated integers from the user.
# Store them in a list.
# Create a dictionary to count each number.
# Find the number with the highest frequency manually.
# Display the number and its frequency.
# ⚠️ Conditions
# ✅ Take input from the user
# ✅ Use a list
# ✅ Use a dictionary
# ✅ Use a loop to count frequencies
# ✅ Use a loop to find the highest frequency
# ❌ Don't use max()
# ❌ Don't use Counter
# ❌ Don't use collections
# ❌ Don't use sort() / sorted()
# ❌ Don't import any libraries

numbers = list(map(int, input("Enter Numbers: ").split()))

freq = {}

for i in numbers:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

freq_num = None
highest_freq = 0

for i in freq:
    if freq[i] > highest_freq:
        highest_freq = freq[i]
        freq_num = i

print(f"Most Frequent : {freq_num}")
print(f"Frequency     : {highest_freq}")

