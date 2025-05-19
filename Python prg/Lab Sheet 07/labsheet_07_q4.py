def quotient_calculate(no1, no2):
    product = no1 / no2
    return product
   
no1 = int(input("Enter a number : "))
no2 = int(input("Enter a number : "))
    
print()
print(f"\033[32mquotient of {no1} and {no2} is : {quotient_calculate(no1, no2)}\033[0m")