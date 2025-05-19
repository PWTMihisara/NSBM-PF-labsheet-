list = []
while True:
    no = input("Enter an integer: ")
    if no.lower() == "done":
        break
    list.append(int(no))

print("")
print(f"\033[31m{list}\033[0m")