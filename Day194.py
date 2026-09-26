# 🔹 Question 1 – Prime Number
# Write a Python program to check whether a given number is a prime number.
# A prime number is a number greater than 1 that has only two factors: 1 and itself.
# Examples
# 2 → Prime
# 3 → Prime
# 5 → Prime
# 7 → Prime
# 9 → Not Prime
# Input
# Enter a number: 7
# Expected Output
# 7 is a Prime Number ✅
# For:
# Enter a number: 9
# Expected:
# 9 is Not a Prime Number ❌
# ⚠️ Conditions
# ✅ Use input()
# ✅ Convert input to an integer
# ✅ Use a loop
# ✅ Check whether the number has any divisor other than 1 and itself
# ✅ Handle numbers less than or equal to 1
# ❌ Don't use libraries
# ❌ Don't use a predefined number
# ❌ Don't use any built-in prime-checking function

def is_prime(number):
    if number <= 1:
        return f"{number} is Not a Prime Number ❌"
    
    for i in range(2, number):
        if number % i == 0:
            return f"{number} is Not a Prime Number ❌"
                
    return f"{number} is a Prime Number ✅"

number = int(input("Enter a number: "))
print(is_prime(number))


# 🔹 Question 2 – Common Elements in Two Lists
# Write a Python program to find the common elements between two lists.
# Use:
# list1 = [1, 2, 3, 4, 5]
# list2 = [3, 4, 5, 6, 7]
# Expected Output
# Common elements: [3, 4, 5]
# ⚠️ Conditions
# ✅ Use two lists
# ✅ Use loops
# ✅ Compare elements from both lists
# ✅ Store common elements in a new list
# ✅ Display the common elements
# ❌ Don't use set()
# ❌ Don't use list intersection shortcuts
# ❌ Don't use libraries
# ❌ Don't hardcode [3, 4, 5]

list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

comman = []

for i in list1:
    for j in list2:
        if i == j:
            comman.append(i)

print(f"Common elements: {comman}")