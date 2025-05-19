import math

def calculate_factorial():
    print()
    number = int(input("Enter a number : "))
    
    factorial = math.factorial(number)
    
    print()
    print(f"The factorial of {number} is {factorial}")
    print()
    
calculate_factorial()
