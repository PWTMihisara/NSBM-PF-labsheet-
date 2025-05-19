print()
print("\033[32mMenu\033[0m")
print()
print("\033[34mSelect the oparator\033[0m")
print("\033[33mA : the area of a circle\033[0m")
print("\033[33mB : the circumference of a circle\033[0m")
print("\033[33mC : the volume of a sphere\033[0m")
print("\033[33mD : Exit\033[0m")

while True:
    print()
    opr = input("Enter the oparator : ")
    print()

    if opr not in ("A", "B", "C", "D", "a", "b", "c", "d"):
        print("\033[31mPlease enter valid oparator\033[0m")
        continue

    if opr.upper() == "D":
        print("\033[31mExiting the calculator.\033[0m")
        break
    
    try:
        rad = float(input("\033[35mEnter the radius : \033[0m"))
    except ValueError:
        print("\033[31mEnter a valid radius.\033[0m")
        continue

    if opr.upper() == "A":
        result = (22/7)*rad**2
    elif opr.upper() == "B":
        result = 2*(22/7)*rad
    else:
        result = (4/3)*(22/7)*rad**3
    
    print("\n")
    print(f"\033[36mThe result is :\033[0m {result}")