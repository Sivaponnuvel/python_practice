def is_even(number):
    return number % 2 == 0

def is_prime(number):
    if number <= 1:
        return False
    for j in range(2, number):
        if number % j == 0:
            return False
    return True

def factorial(number):
    fact = 1
    for i in range(1, number+1):
        fact *= i
    return fact