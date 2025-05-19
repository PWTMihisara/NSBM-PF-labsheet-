print()
x = 1
inputs = []
counter = 0
while x<=10:
    try:
        no = int(input("\033[32mEnter the number :\033[0m "))
    except ValueError:
        print()
        print("Enter the value number")
        print()
        continue
    x = x+1
    inputs.append(no)

    if no%2 == 0:
        counter += 1 

print()
print(f"\033[33mInputed numbers \033[34m{inputs}\033[0m ")
print()
print(f"\033[33mEven number count : \033[34m{counter}\033[0m")
print()