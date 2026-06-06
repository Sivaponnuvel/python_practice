def square(number):
    return number ** 2

def cube(number):
    return number ** 3

def factorial(number):
    fact = 1
    for i in range(1,number+1):
        fact *= i
    return fact