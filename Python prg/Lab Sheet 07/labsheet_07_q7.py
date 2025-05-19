def product(no1:int, no2:float)->float:
    pro = no1 * no2
    return pro

def main():
    no1 = int(input("Enter the first number : "))
    no2 = float(input("Enter the second number : "))

    print(f"The produnct of {no1} and {no2} is : {product(no1, no2)}")

main()