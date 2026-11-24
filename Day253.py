# Question 1 – Find the First Non-Repeating Character in a String
# Interview Topics: Strings, Loops, Character Frequency, Conditional Statements.
# Given a string, find the first character that appears only once.
# Requirements:
# 1. Get a string from the user using input().
# 2. Find the first non-repeating character.
# 3. Use loops and conditional statements.
# 4. Do not use Counter() or dictionary frequency counting.
# 5. If no non-repeating character exists, display an appropriate message.
# Expected Output 1:
# Enter a string: programming
# First Non-Repeating Character: p
# Expected Output 2:
# Enter a string: aabbcc
# No Non-Repeating Character Found

string = input("Enter a string: ")

found = False
char = ""

for i in string:
    count = 0
    for j in string:
        if i == j:
            count += 1
    if count == 1:
        found = True
        char = i
        break

if found:
    print(f"First Non-Repeating Character: {char}")
else:
    print("No Non-Repeating Character Found")


