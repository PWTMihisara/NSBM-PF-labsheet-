arr=[]
even_count=0

for x in range(10):
    try:
        no=int(input("Enter an integer: "))
    except ValueError:
        print("")
        print("\033[31mInvalid input. Enter valid integers.\033[0m")
        exit()

    arr.append(no)
    
    if (no%2==0):
        even_count=even_count+1

print("")
print(f"\033[92mNumber array: {arr}\033[0m")
print(f"\033[92mNumber of even number: {even_count}\033[0m")