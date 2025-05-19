arr=[]

try:
    no=int(input("Enter an integer: "))
except ValueError:
    print("")
    print("\033[31mInvalid input. Enter a valid integer.\033[0m")

given_num=no
x=1
while (x<=no):
    if (no%x==0):
        arr.append(x)
    x=x+1

print("")
print(f"\033[92mAll factors of {given_num} is : {arr}\033[0m")