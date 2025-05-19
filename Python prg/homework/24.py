print()
print("\033[32mDo you want to know about me.\033[0m")
print()

sel = input("Yes or NO  : ")

if sel.lower() == ("no"):
    print("\033[31mOk.. Have a Bad day.\033[0m")
    print()
    exit()
     
if sel.lower() == ("yes"):
    print()
    print("\033[32mSelect what you want to know.\033[0m")
    print()
    print(" \033[34m1.. My Name\033[0m")
    print(" \033[34m2.. My Birth Day\033[0m")
    print(" \033[34m3.. My University\033[0m")
    print(" \033[34m4.. My Wife\033[0m")
    print(" \033[34m5.. Exit\033[0m")
else:
    print("\033[31mSorry. Your choice isn't here.\033[0m")
    

while True:
    print()
    
    cho = input("\033[32mEnter your choice :\033[0m ")

    if sel == "No":
        print("OK.. Have a Bad Day.")
        break
    
    if cho not in ("1", "2", "3", "4", "5"):
        print()
        print("\033[31mSorry. Your choice isn't here. Please try again.\033[31m")
        continue

    if cho == "5":
        print()
        print("\033[31mExiting the my heyesart.\033[0m")
        print()
        break

    if cho == "1":
        print()
        print("            \033[33mP.W.Thamidu Mihisara\033[0m")
    elif cho == "2":
        print()
        print("            \033[033m2004/07/22\033[0m")
    elif cho == "3":
        print()
        print("            \033[33mNSBM Green University Town\033[0m")
    else:
        print()
        print("            \033[33mDefinitely you.\033[0m\033[31m \003\033[0m")
        print()