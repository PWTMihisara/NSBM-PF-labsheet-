sum = 0
while True:
    print()
    no = int(input("Enter a number : "))
    sum = sum + no

    if no == -1:
        print()
        print("\033[31mExit.\033[0m")
        break
    
print(f"\033[32mtotal is :\033[0m {sum}")
print()