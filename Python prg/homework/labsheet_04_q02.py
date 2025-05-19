print()
print("\033[32mMenu\033[0m ")
print()
print(" \033[34m1 : Addition (+)\033[0m")
print(" \033[34m2 : Subtraction (-)\033[0m")
print(" \033[34m3 : Divition (/)\033[0m")
print(" \033[34m4 : Multiplication (*)\033[0m")
print(" \033[34m5\033 \033[34m :\033[0m \033[31mExit\033[0m")

while True:
    print()
    opr = (input("Enter the oparator : "))
    print()
    if opr not in ("1", "2", "3", "4", "5"):
        print("\033[31mEnter the valid oparator.\033[0m")
        continue
    if opr == ("5"):
        print("\033[31mExiting oparator.\033[0m")
        break

    try:
        no1 = float(input("\033[35mEnter the first number  :\033[0m "))
        no2 = float(input("\033[35mEnter the second number :\033[0m "))
    except ValueError:
        print("\033[31mInvalid value.\033[0m")
        continue

    if opr == ("1"):
        result = no1 + no2
    elif opr == ("2"):
        result = no1 - no2
    elif opr == ("3"):
        result = no1/no2
    else:
        result = no1*no2

    print()
    print(f"\033[33mThe result is\033[0m : {result} ")
    print()