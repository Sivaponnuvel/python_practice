# Question 1 – Find Even and Odd Numbers in a List
# Interview Topics: Lists, for Loop, Conditional Statements, Modulus Operator.
# Write a Python program to separate even and odd numbers from a list.
# Requirements:
# 1. Get 5 integer values from the user using input().
# 2. Store all values in a list.
# 3. Create two empty lists: even_numbers and odd_numbers.
# 4. Use a for loop to iterate through the list.
# 5. Separate even and odd numbers using the modulus operator (%).
# 6. Display both lists.
# Expected Output:
# Enter number 1: 10
# Enter number 2: 15
# Enter number 3: 20
# Enter number 4: 25
# Enter number 5: 30
# Original List: [10, 15, 20, 25, 30]
# Even Numbers: [10, 20, 30]
# Odd Numbers: [15, 25]

numbers = []
even_numbers = []
odd_numbers = []

for i in range(5):
    number = int(input(f"Enter number {i+1}: "))
    numbers.append(number)

for i in numbers:
    if i % 2 == 0:
        even_numbers.append(i)
    else:
        odd_numbers.append(i)

print(f"Original List: {numbers}")
print(f"Even Numbers: {even_numbers}")
print(f"Odd Numbers: {odd_numbers}")


