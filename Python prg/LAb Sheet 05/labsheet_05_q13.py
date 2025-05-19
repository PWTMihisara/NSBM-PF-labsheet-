arr=[]
counter=0
for x in range(10):
    try:
        no=int(input("Enter an integer: "))
        arr.append(no)
    except ValueError:
        print("")
        print("\033[31mInvalid input. Enter valid integers.\033[0m")
        exit()

print("")
print(f"\033[92mNumber array: {arr}\033[0m")
print(f"The 5th number is: {arr[4]}")