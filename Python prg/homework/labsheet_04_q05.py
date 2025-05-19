while True:
    print()
    mounth = int(input("\033[32mEnter the mounth number (1 - 12) : \033[0m"))
    print()

    if mounth == 1:
        days = 31
    elif mounth == 2:
        days = 28
    elif mounth == 3:
        days = 31
    elif mounth == 4:
        days = 30
    elif mounth == 5:
        days = 31
    elif mounth == 6:
        days = 30
    elif mounth == 7:
        days = 31
    elif mounth == 8:
        days = 31
    elif mounth == 9:
        days = 30
    elif mounth == 10:
        days = 31
    elif mounth == 11:
        days = 30
    elif mounth == 12:
        days = 31
    else:
        days = None

    if days is not None:
        print(f"\033[33mThis mounth is\033[0m \033[34m{mounth}\033[0m\033[33m.\033[0m \033[33mAnd this mounth has\033[0m \033[34m{days}\033[0m \033[33mdays.\033[0m")
    else:
        print("\033[31mThis is not a mounth number. please enter the mounth number\033[0m \033[33m(1-12)\033[0m\033[31m.\033[0m")