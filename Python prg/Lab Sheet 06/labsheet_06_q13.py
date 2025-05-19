import math

def calculate_hypotenuse(a, b):
    hypotenuse = math.sqrt(a**2 + b**2)
    return hypotenuse

def main():
    side1 = 3
    side2 = 4
    
    hypotenuse = calculate_hypotenuse(side1, side2)
    
    print(f"The length of the hypotenuse is: {hypotenuse}")

if __name__ == "__main__":
    main()
