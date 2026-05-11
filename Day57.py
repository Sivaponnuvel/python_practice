# 🔹 Question 1 – Function with List Return
# Write a Python program to:
# 👉 Create a function:
# get_numbers()
# 👉 Inside function:
# take 5 numbers from user
# store in list
# return the list
# 👉 Outside function:
# call function
# print:
# full list
# largest number
# smallest number
# Example Output:
# Numbers: [10, 20, 30, 40, 50]
# Largest: 50
# Smallest: 10

def get_numbers():
    while True:
        numbers = list(map(int,input("Enter 5 numbers separated by space: ").split()))
        if len(numbers) == 5:
            return numbers
        print("Please enter exactly 5 numbers!")
result = get_numbers()
largest_number = result[0] 
for i in result:
    if i > largest_number:
        largest_number = i
smallest_number = result[0]
for i in result:
    if i < smallest_number:
        smallest_number = i
print(f"Numbers: {result}")
print(f"Largest: {largest_number}")
print(f"Smallest: {smallest_number}")


