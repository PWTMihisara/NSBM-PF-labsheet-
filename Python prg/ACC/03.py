x = 1
tot = 0

while x <= 10: 
    print()
    try:
        no = int(input(f"Enter the number {x} : "))
    except ValueError:
        print("\033[31mEnter the Valid Number.\033[0m")
        continue
    tot = tot + no
    x += 1

print()
print(f"The average is \033[32m{tot/10}\033[0m.")
print()