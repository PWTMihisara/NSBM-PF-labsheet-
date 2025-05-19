print()
x = 1
inputs = []
while x<=10:
    no = int(input("\033[32mEnter the number :\033[0m "))
    x = x+1
    inputs.append(no)

print()
print(f"\033[33mInputed numbers\033[om \033[34m{inputs}\033[0m ")
print()