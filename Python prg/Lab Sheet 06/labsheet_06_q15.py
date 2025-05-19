import math

def round_numbers():
    number = 0.6523
    
    rounded_down = math.floor(number)
    
    rounded = round(number)
    
    print()
    print(f"The number {number} rounded down using math.floor is {rounded_down}")
    print(f"The number {number} rounded using round() is {rounded}")
    
    print("\nExplanation:")
    print("math.floor() always rounds down to the nearest whole number, regardless of the decimal part.")
    print("round() rounds to the nearest whole number, but it rounds halfway cases away from zero.")
    print()
    
round_numbers()