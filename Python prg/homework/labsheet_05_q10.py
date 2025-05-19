print()
while True:
    try:
        no = int(input("\033[32mEnter a number : \033[0m"))
    except ValueError:
        print()
        print("\033[31mEnter  the valied number.\033[0m")
        print()    
        continue
        print()
    x = 1
    counter = 0

    while x<=no:
        if(no%x == 0):
            counter = counter + 1
        x = x + 1

    if counter == 2:
        print()
        print(f"\033[32mNumber {no} is a prime number.\033[0m")
    else:
        print()
        print(f"\033[31mNumber {no} is not a prime number.\033[0m")
    print()