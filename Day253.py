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


# Question 2 – Move All Zeros to the End of a List
# Interview Topics: Lists, Loops, Conditional Statements, List Manipulation.
# Given a list of integers, move all zeros to the end while maintaining the original order of non-zero elements.
# Requirements:
# 1. Get the number of elements from the user.
# 2. Get integer values using input().
# 3. Store the values in a list.
# 4. Move all zeros to the end of the list.
# 5. Maintain the original order of non-zero elements.
# 6. Do not use sort() or sorted().
# 7. Display the modified list.
# Expected Output:
# Enter how many numbers: 7
# Enter number 1: 0
# Enter number 2: 1
# Enter number 3: 0
# Enter number 4: 3
# Enter number 5: 12
# Enter number 6: 0
# Enter number 7: 5
# Original List: [0, 1, 0, 3, 12, 0, 5]
# Modified List: [1, 3, 12, 5, 0, 0, 0]

numbers = []
n = int(input("Enter how many numbers: "))

for i in range(n):
    number = int(input(f"Enter number {i+1}: "))
    numbers.append(number)

new_list = []
zeros = []

for i in range(len(numbers)):
    if numbers[i] == 0:
        zeros.append(numbers[i])
    else:
        new_list.append(numbers[i])

new_list.extend(zeros)

print(f"Original List: {numbers}")
print(f"Modified List: {new_list}")