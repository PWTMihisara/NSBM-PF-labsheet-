import math

def hypotenuse(side1:float, side2:float):
    return math.sqrt(side1**2 + side2**2)

side1 = float(input("Enter the first number : "))
side2 = float(input("Enter the first number : "))

print(hypotenuse(side1, side2))