def add(a, b):
    return a + b  

def subtract(a, b):
    return a - b  

def multiply(a, b):
    return a * b 


def divide(a, b):
    if b == 0:
        return None  
    return a / b  

def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")  
    if n == 0 or n == 1:
        return 1  
    return n * factorial(n - 1)  


def power(base, exponent):
    return base ** exponent  
