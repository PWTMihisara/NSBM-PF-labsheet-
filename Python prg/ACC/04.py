print("\n")
no = int(input("Enter the number : "))
rev = 0

while no > 0:
    no1 = no % 10
    rev = (rev * 10) + no1
    no = no // 10

print()    
print(f"reversed Number  : \033[32m{rev}\033[0m")
print()