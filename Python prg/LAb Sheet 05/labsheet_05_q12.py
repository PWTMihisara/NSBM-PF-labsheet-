sum=0
while True:
    no = float(input("Enter a number: "))
    if (no==-1):
        break
    else:
        sum=sum+no
print("")
print(f"\033[92mTotal: {sum}\033[0m")