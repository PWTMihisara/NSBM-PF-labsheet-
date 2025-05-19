print()
while True:
    factors = []
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
            factors.append(x)
        x = x+1

    print()
    print(factors)
    print()